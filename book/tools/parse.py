#!/usr/bin/env python3
"""parse.py — semantic reconstructor.

Reads book/artifacts/dump.json (raw audit dump of the original .docx) and rebuilds
the book as a clean semantic tree -> book/artifacts/book.json, applying the locked
editorial/structural corrections from the production specification and logging
every substantive change to book/artifacts/changelog.json.

Design notes
------------
* Item indices refer to block positions in the source dump and are stable for
  the source document; manual overrides below are keyed on them and each one
  is justified in the change log.
* Ordinary questions, instructions and options are demoted from heading styles
  to content blocks (defect B); empty headings/paragraphs are dropped (C);
  the doubled "Before You Read" blocks are de-duplicated (D); unit-title
  duplication artifacts are collapsed (H); web/AI-interface style classes are
  discarded (F); the dead hdphoto1.wdp asset is never carried forward (G).
"""
import json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BUILD = os.path.join(ROOT, 'book', 'artifacts')

items = json.load(open(os.path.join(BUILD, 'dump.json'), encoding='utf-8'))
image_map = json.load(open(os.path.join(BUILD, 'image_map.json'), encoding='utf-8'))

CHANGES = []          # {area, original, correction, reason, confidence}
_chooses_fixed = set()
def log(area, original, correction, reason, confidence='high'):
    CHANGES.append(dict(area=area, original=original, correction=correction,
                        reason=reason, confidence=confidence))

# ----------------------------------------------------------------------------
# 1. TEXT NORMALIZATION
# ----------------------------------------------------------------------------
EMOJI_MAP = {'✅': '✔', '❌': '✗', '👄': ''}

def norm(s):
    """Global typographic normalization of a source string."""
    if s is None:
        return ''
    s = s.replace('\xa0', ' ')
    for k, v in EMOJI_MAP.items():
        s = s.replace(k, v)
    s = re.sub(r'\s+', ' ', s)
    s = re.sub(r'\s+([,.;:!?])', r'\1', s)
    s = re.sub(r'\b([Oo])n-going\b',
               lambda m: 'Ongoing' if m.group(1) == 'O' else 'ongoing', s)
    s = s.strip()
    return s

def smarten(s):
    """Convert straight quotes/apostrophes to typographic ones."""
    s = re.sub(r"(?<=[A-Za-z])'(?=[A-Za-z])", '’', s)      # don't, it's
    s = re.sub(r"(?<=[A-Za-z])'(?=\s|$)", '’', s)           # students' books
    s = re.sub(r"'(?=\d)", '’', s)                          # '90s
    # double quotes: pair them up
    out, open_q = [], True
    for ch in s:
        if ch == '"':
            out.append('“' if open_q else '”')
            open_q = not open_q
        else:
            out.append(ch)
    return ''.join(out)

def clean(s):
    return smarten(norm(s))

def blank(s):
    return not s or not s.strip()

# ----------------------------------------------------------------------------
# 2. STRUCTURE BOUNDARIES
# ----------------------------------------------------------------------------
# unit opener indices (paragraphs that carry "… Unit N …" duplication artifacts)
UNIT_OPENERS = {166: 1, 446: 2, 770: 3, 1087: 4, 1404: 5, 1804: 6, 2177: 7, 2542: 8}
# canonical unit titles (see change log: unit 6 topic per TOC + series pattern)
UNIT_TITLES = {
    1: 'The Power of Communication',
    2: 'The Art of Goal Setting',
    3: 'Emotional Intelligence',
    4: 'Money and Happiness',
    5: 'Living with AI',
    6: 'Marriage',
    7: 'Globalization',
    8: 'Lingua Franca',
}
# chapter marker indices -> (unit, chapter); titles normalized to one casing
CANON_CHAPTER = {
    1: 'Speaking through Reading',
    2: 'Speaking through Listening',
    3: 'Speaking through Discussion',
    4: 'Speaking through Research Presentation',
}
CHAPTER_MARKS = {}
for x in items:
    if x['type'] == 'para':
        m = re.match(r'^Chapter (\d):\s*(.+)$', (x['text'] or '').strip())
        if m and x['style'] == 'ListParagraph':
            CHAPTER_MARKS[x['i']] = (int(m.group(1)), CANON_CHAPTER[int(m.group(1))])

def unit_of(i):
    u = 0
    for oi in sorted(UNIT_OPENERS):
        if oi <= i:
            u = UNIT_OPENERS[oi]
    return u

def chap_of(i):
    last = None
    for ci in sorted(CHAPTER_MARKS):
        if ci <= i:
            last = CHAPTER_MARKS[ci]
    return last  # (num, title) or None

# ----------------------------------------------------------------------------
# 3. MANUAL OVERRIDES (each logged below in apply_overrides)
# ----------------------------------------------------------------------------
# U6 Ch2 "Before Listening / Look at the title." carries Unit 4's video title
OVR_TITLE_FIX = {1925: 'The Science of a Lasting Relationship'}
# U6 speaking challenges are two distinct activities (locked decision)
OVR_SC2 = 2077          # plain-paragraph "Speaking Challenge" inside Ch4
OVR_SC1 = 2041          # Heading1 "Speaking Challenge" in Ch3
# U8 stray heading copied from the Marriage unit (locked: remove, keep content)
DROP_HEADINGS = {2026}
# instructions removed as unusable copy-paste artifacts (flagged, not silent)
REMOVE_ITEMS = {
    2593: ('U8 Ch1 Reading Comprehension',
           'Write T or F. Correct the false statements.',
           'instruction deleted; the eight questions that follow are open comprehension '
           'questions, not true/false statements — the instruction cannot apply to them '
           '(see unresolved-issues report)'),
}
# targeted proofreading fixes {index: new text}
TEXT_FIXES = {
    1518: 'Education, employment, healthcare, communication, entertainment',
    1582: 'Imagine that scientists develop an AI system that can solve major problems such as climate change.',
    1496: 'Share your ideas about the quote:',
    2554: 'Use this idea to discuss the title above. Use as many vocabulary expressions as you can.',
}
# unit 6 Before You Read has an internally doubled question (deduped in code)

# video/topic label paragraphs immediately after each Chapter 2 marker
VIDEO_TITLE_IDX = {268, 574, 889, 1207, 1503, 1915, 2285, 2640}
VIDEO_TITLE_TEXT = {  # normalized (title case where source was sentence case)
    268: 'Are You a Good Listener?',
    574: 'The Art of Goal Setting',
    889: 'The Power of Emotional Intelligence',
    1207: 'Can Money Buy Happiness?',
    1503: 'How Will AI Change the World?',
    1915: 'The Science of a Lasting Relationship',
    2285: 'Navigating Our Global Future',
    2640: 'English Without Borders',
}

SECTION_NAMES = {  # canonical section (h3) names, with source variants
    'vocabulary preview': 'Vocabulary Preview',
    'vocabulary check': 'Vocabulary Check',
    'before you read': 'Before You Read',
    'reading comprehension': 'Reading Comprehension',
    'critical thinking': 'Critical Thinking',
    'speaking through reading': 'Speaking through Reading',
    'homework': 'Homework',
    'think – pair – share': 'Think – Pair – Share',
    'think-pair-share': 'Think – Pair – Share',
    'before listening': 'Before Listening',
    'listening strategy': 'Listening Strategy',
    'listening comprehension': 'Listening Comprehension',
    'group discussion': 'Group Discussion',
    'speaking toolbox': 'Speaking Toolbox',
    'vocabulary activation': 'Vocabulary Activation',
    'guided discussion': 'Guided Discussion',
    'mini debate': 'Mini Debate',
    'mini-debate': 'Mini Debate',
    'speaking challenge': 'Speaking Challenge',
    'the six-ingredient ranking challenge': 'The Six-Ingredient Ranking Challenge',
    'pronunciation clinic': 'Pronunciation Clinic',
    'presentation toolbox': 'Presentation Toolbox',
    'research task': 'Research Task',
    'organizing your presentation': 'Organizing Your Presentation',
    'write your research presentation': 'Write Your Research Presentation',
    'rules': 'Rules',
    'answer the questions': 'Answer the Questions',
}
SUBSEC_NAMES = {  # h4 subsection names
    'a. multiple choice': 'A. Multiple Choice',
    'b. true or false': 'B. True or False',
    'c. short answer': 'C. Short Answer',
    'look at the title': 'Look at the Title',
    'look at the title.': 'Look at the Title',
    'prediction': 'Prediction',
    'motion': 'Motion',
    'practice': 'Practice',
    'quick practice': 'Quick Practice',
    'quick test': 'Quick Test',
    'example': 'Example',
    'examples': 'Examples',
    'compare': 'Compare',
    'challenge': 'Challenge',
    'common problem': 'Common Problem',
    'mouth position': 'Mouth Position',
    'discussion questions': 'Discussion Questions',
    'individual presentation (2 minutes)': 'Individual Presentation (2 Minutes)',
    'the emotional intelligence coach': 'The Emotional Intelligence Coach',
    'introducing your topic': 'Introducing Your Topic',
    'referring to evidence': 'Referring to Evidence',
    'giving examples': 'Giving Examples',
    'expressing opinions': 'Expressing Opinions',
    'concluding': 'Concluding',
    'title': 'Title',
    'introduction': 'Introduction',
    'body': 'Body',
    'conclusion': 'Conclusion',
    'choose the best answer': 'Choose the Best Answer',
    'true or false': 'True or False',
    'the “-ed” ending: /t/, /d/, or /ɪd/?': 'The “-ed” Ending: /t/, /d/, or /ɪd/?',
    'job creator or job destroyer?': 'Job Creator or Job Destroyer?',
    'globalization: opportunity or threat?': 'Globalization: Opportunity or Threat?',
    '1. is english really a global language?': '1. Is English Really a Global Language?',
    '2. who owns english?': '2. Who Owns English?',
    '3. does english proficiency equal intelligence?': '3. Does English Proficiency Equal Intelligence?',
    '4. english as a barrier to education': '4. English as a Barrier to Education',
    '5. the future of english': '5. The Future of English',
    '6. language diversity and globalization': '6. Language Diversity and Globalization',
    'main point 1': 'Main Point 1',
    'main point 2': 'Main Point 2',
    'main point 3': 'Main Point 3',
    'step 1 – write your title': 'Step 1 – Write Your Title',
    'step 2 – write your introduction': 'Step 2 – Write Your Introduction',
    'step 3 – organize your main points': 'Step 3 – Organize Your Main Points',
    'step 4 – write your conclusion': 'Step 4 – Write Your Conclusion',
    'essential presentation expressions': 'Essential Presentation Expressions',
    'academic presentation expressions': 'Academic Presentation Expressions',
    'student b': 'Student B',
    'group a': 'Group A',
    'group b': 'Group B',
    'group a — agree': 'Group A — Agree',
    'group b — disagree': 'Group B — Disagree',
    'instructions': 'Instructions',
    'debate rules': 'Debate Rules',
    'discussion 1': 'Discussion 1',
    'discussion 2': 'Discussion 2',
    'discussion 3': 'Discussion 3',
    'two-minute speaking': 'Two-Minute Speaking',
    'speaking': 'Speaking',
    'listening practice': 'Listening Practice',
    'topic': 'Topic',
    'guiding questions': 'Guiding Questions',
    'final question:': 'Final Question',
    'what should english in 2050 look like?': 'What Should English in 2050 Look Like?',
    'what does this mean?': 'What Does This Mean?',
    'use rising intonation (↗)': 'Use Rising Intonation (↗)',
    'use falling intonation (↘)': 'Use Falling Intonation (↘)',
    'emphasize key words': 'Emphasize Key Words',
}
RUNIN_NAMES = {  # run-in (h5-level) labels
    'first viewing': 'First Viewing',
    'second viewing': 'Second Viewing',
    'presentation language': 'Presentation Language',
    'think beyond': 'Think Beyond',
}

RE_QUESTION = re.compile(r'^(?:\(\d+\)\s*)?\d{1,2}[\.\)]\s+')
RE_OPTION = re.compile(r'^[a-dA-D][\.\)]\s+')
RE_TF = re.compile(r'^_{3,}\s+')
RE_FILL = re.compile(r'_{3,}')
RE_CHALLENGE = re.compile(r'^Challenge Question:?\s*', re.I)

def is_instruction(t):
    return bool(re.match(
        r'^(Work (in|with)|Discuss|Answer|Choose|Complete|Rank|Read |Write |Use |Learn |Study |'
        r'Prepare |Conduct |Speak |Give |Present |Watch |Predict|Focus on|Below are|Task:|'
        r'Research |Split |Divide |Put your|Say:|Then |First |After |Student [AB]|Examples?:|'
        r'Include:|Requirements:|Topic:|Motion|Each |They must|You will|Turn |It is the year)', t))

def is_question(t):
    return t.endswith('?') or bool(re.match(r'^(What|Why|How|Which|Do |Does |Did |Is |Are |Can |Could |Should |Would |Have |Has |Will |If |Imagine|List |Think )', t))

# ----------------------------------------------------------------------------
# 4. BEFORE-YOU-READ de-duplication data (defect D)
#    questions per unit, hand-verified against source text
# ----------------------------------------------------------------------------
BYR_QUESTIONS = {
    1: ['Which is more important: speaking or listening?',
        'Do grammar mistakes stop communication?',
        'What makes someone an excellent communicator?'],
    2: ['Why do some people achieve their goals while others give up?',
        'Is talent more important than hard work?',
        'Have you ever failed to achieve a goal? What happened?'],
    3: ['What is emotional intelligence?',
        'Why is it important in daily life?',
        'How can emotional intelligence improve relationships?'],
    4: ['What do you think the reading will say about the relationship between money and happiness?',
        'Do you think the author will agree or disagree with the title? Why?',
        'List three things that you think bring people happiness besides money.'],
    5: ['What advantages of AI do you expect to read about?',
        'What risks or challenges might the reading mention?',
        'Do you think the author will have a positive, negative, or balanced opinion about AI? Why?'],
    6: ["Do you think people's expectations of marriage have changed over time?",
        'Which is more difficult: falling in love or maintaining a long-term relationship?'],
    7: ['What does the word globalization mean to you?',
        'How many products do you use every day that were made in another country?',
        'How has the internet changed the way people communicate around the world?'],
    8: ['How many countries do you think use English as an official or widely used language?',
        'What areas do you think English has the strongest influence on?',
        'Do you think everyone in the world should learn English?'],
}
BYR_STRAY_FILLIN = {  # vocabulary-check sentence merged into the BYR paragraph
    3: 'Learning another language allows you to ____________________________ from different backgrounds.',
    7: 'Studying abroad can create __________ for young people.',
}

# reading passage titles (h4, reading-title style)
READING_TITLE_IDX = {192, 477, 794, 1116, 1431, 1828, 2200, 2563}
READING_TITLES = {
    192: 'The Power of Communication',
    477: 'Dreams Become Reality through Goals',
    794: 'The Power of Emotional Intelligence',
    1116: 'Can Money Buy Happiness?',
    1431: 'Living with AI: Friend or Foe?',
    1828: 'Is Love Enough?',
    2200: 'The World Is Getting Smaller',
    2563: 'English: From a Local Language to a Global Lingua Franca',
}

# ----------------------------------------------------------------------------
# 5. PARSE FRONT MATTER
# ----------------------------------------------------------------------------
def parse_front():
    paras = [(x['i'], x) for x in items if x['type'] == 'para']
    def txt(i):
        return clean(items_by_idx[i]['text'])

    foreword = []
    for i in range(13, 30):
        t = txt(i)
        if not t:
            continue
        if i == 13:
            continue  # FORWARD heading handled by caller (renamed)
        if i == 25:
            foreword.append({'k': 'closer', 'text': t})
        elif i == 26:
            foreword.append({'k': 'p', 'text': t})
        elif i == 28:
            foreword.append({'k': 'signature', 'text': t.rstrip('.')})
        elif i == 29:
            foreword.append({'k': 'date', 'text': 'September 2026'})
        else:
            foreword.append({'k': 'p', 'text': t})

    howto = {'k': 'howto', 'subtitle': txt(69), 'paras': [], 'chapters': []}
    cur = None
    for i in range(70, 112):
        t = txt(i)
        if not t:
            continue
        m = re.match(r'^CHAPTER (\d) — (.+)$', t)
        if m:
            title = m.group(2).strip()
            canon = CANON_CHAPTER.get(int(m.group(1)))
            if canon and canon.lower() != title.lower():
                if title == 'Speaking through Research & Present':
                    log('Front matter · How to Use This Book',
                        'CHAPTER 4 — Speaking through Research & Present (truncated in source)',
                        f'CHAPTER 4 — {canon}',
                        'front-matter label aligned with the actual chapter title used throughout the book',
                        'high (verified)')
                title = canon
            cur = {'n': int(m.group(1)), 'title': title, 'desc': '', 'you_will': []}
            howto['chapters'].append(cur)
            continue
        if cur is None:
            howto['paras'].append(t)
        elif t in ('You will:', 'You will work with:'):
            pass                       # list label; implied by rendering
        elif not cur.get('desc'):
            cur['desc'] = t            # chapter description sentence
        else:
            cur['you_will'].append(t)
    # closing sentence
    howto['closing'] = txt(111)

    epigraph = txt(121)
    return {'foreword': foreword, 'howto': howto, 'epigraph': epigraph}

items_by_idx = {x['i']: x for x in items}

# ----------------------------------------------------------------------------
# 6. TABLE CLASSIFICATION
# ----------------------------------------------------------------------------
VOCAB_HEADERS = {'word', 'expression', 'expression / vocabulary', 'vocabulary / expression',
                 'vocabulary / collocation', 'expression / collocation', 'expression / vocabulary'}

def classify_table(t):
    rows = t['rows']
    first = norm(rows[0][0]['text']) if rows and rows[0] else ''
    first_l = first.lower().rstrip(':')
    ncols = t['grid_cols']
    if first_l in VOCAB_HEADERS:
        return 'vocab'
    if first_l in {'expression', 'expression '}:
        return 'vocab'
    if ncols == 2 and first_l.rstrip('s').rstrip(':') in {'main idea', 'rank', 'idea'}:
        if first_l.startswith('main idea'):
            return 'notes'
        if first_l == 'rank':
            return 'ranking'
    if ncols == 3 and first_l in {'/t/', 'a', 'b'}:
        return 'grid'
    # default heuristics by shape/content
    if ncols == 2:
        # warm-up / answer-question tables: first cell is a question/sentence, second blank-ish
        cell0 = norm(rows[0][0]['text']) if rows and rows[0] else ''
        if len(rows) <= 6 and (cell0.endswith('?') or RE_FILL.search(cell0)):
            return 'questions'
        if first_l in {'expression', 'function'}:
            return 'preslang'
        if any(RE_TF.match(norm(r[0]['text'])) if r else False for r in rows):
            return 'questions'
        return 'generic'
    if first_l == 'expression':
        return 'vocab'
    if ncols == 2:
        return 'preslang'
    return 'generic'

def table_block(t):
    rows = []
    for r in t['rows']:
        row = []
        for c in r:
            row.append(clean(c['text'].replace('\n', ' ')))
        while len(row) < t['grid_cols']:
            row.append('')
        rows.append(row)
    role = classify_table(t)
    return {'k': 'table', 'role': role, 'rows': rows, 'src': t['i']}

# ----------------------------------------------------------------------------
# 7. BLOCK SPLITTERS (jammed paragraphs)
# ----------------------------------------------------------------------------
OPT_SPLIT = re.compile(r'(?:(?<=[.?!])|(?<=[a-z]))\s*(?=[A-Da-d]\.\s)')

def split_options(text):
    """Split 'stem?a. opt1b. opt2' or 'a. ob. oc.' into stem + option list."""
    parts = OPT_SPLIT.split(text)
    stem, opts = None, []
    for part in parts:
        part = part.strip()
        if not part:
            continue
        if RE_OPTION.match(part):
            opts.append(part)
        elif opts == [] and stem is None:
            stem = part
        else:
            if opts:
                opts[-1] += ' ' + part
            elif stem:
                stem += ' ' + part
    return stem, opts

# hand-verified splits of copy-paste-jammed lines (index -> list of lines)
JAM_FIXES = {
    1676: ['turn_it_off → turnitoff', 'pick_it_up → pickitup',
           'work_in → workin', 'depend_on → dependon'],
    1692: ['1. Slowly → separate words', '2. Naturally → connect the sounds',
           '3. Fluently → focus on meaning, not individual words'],
    2451: ['think → sink', 'three → tree', 'this → dis', 'those → dose'],
    2459: ['think — this', 'three — these', 'threat — that',
           'thought — though', 'through — those'],
    238:  ['Speaking', 'Listening', 'Writing', 'Reading'],
    534:  ['Hard work', 'Clear goals', 'Good teachers',
           'Family support', 'Self-discipline', 'Confidence'],
}

# ----------------------------------------------------------------------------
# 8. MAIN BODY PARSER
# ----------------------------------------------------------------------------
def parse_units():
    units = []
    opener_idxs = sorted(UNIT_OPENERS)
    for pos, oi in enumerate(opener_idxs):
        end = opener_idxs[pos + 1] if pos + 1 < len(opener_idxs) else len(items)
        u_num = UNIT_OPENERS[oi]
        # opener image: first paragraph from oi..oi+8 that carries an image
        opener_img = None
        for x in items:
            if oi <= x['i'] < oi + 12 and x['type'] == 'para' and x['images']:
                opener_img = image_map.get(x['images'][0])
                break
        unit = {'number': u_num, 'title': UNIT_TITLES[u_num], 'image': opener_img,
                'chapters': []}
        ch_bounds = [(ci, CHAPTER_MARKS[ci]) for ci in sorted(CHAPTER_MARKS)
                     if oi <= ci < end]
        # warm-up "Think" block lives between opener and Chapter 1 marker
        warm = {'k': 'warmup'}
        for x in items:
            if oi < x['i'] < (ch_bounds[0][0] if ch_bounds else end):
                if x['type'] == 'para':
                    t = clean(x['text'])
                    if not t:
                        continue
                    if t.lower() == 'think':
                        continue
                    warm.setdefault('paras', []).append(t)
                elif x['type'] == 'table':
                    warm['table'] = table_block(x)
        unit['warmup'] = warm
        for ci, (cn, ctitle) in ch_bounds:
            c_end = None
            # find next chapter/unit bound
            nxt = [j for j, _ in ch_bounds if j > ci]
            c_end = nxt[0] if nxt else end
            unit['chapters'].append(parse_chapter(u_num, cn, ctitle, ci, c_end))
        units.append(unit)
    return units

def parse_chapter(u_num, c_num, c_title, start, end):
    chap = {'number': c_num, 'title': c_title, 'blocks': []}
    blocks = chap['blocks']
    reading_mode = False
    last_sub = ['']   # tracks the most recent sub/subsub label

    def push(b):
        blocks.append(b)

    x_list = [x for x in items if start < x['i'] < end]
    for x in x_list:
        i = x['i']
        if x['type'] == 'table':
            push(table_block(x))
            continue
        raw = x['text']
        t = clean(raw)
        style = x['style'] or ''
        imgs = [image_map.get(r) for r in x['images']]
        imgs = [m for m in imgs if m]

        if not t:
            continue  # empty paragraph (logged globally)

        if 'Chooses 10 expressions' in t:
            t = t.replace('Chooses 10 expressions', 'Choose 10 expressions')
            _chooses_fixed.add(u_num)
        if i in REMOVE_ITEMS:
            area, orig, reason = REMOVE_ITEMS[i]
            log(area, orig, '(instruction removed; questions retained)', reason,
                'medium — flagged')
            continue
        if i in TEXT_FIXES:
            new = TEXT_FIXES[i]
            if new != t:
                log(f'U{u_num} text', t, new, 'unambiguous proofreading fix (truncated word / grammar / diction)')
            t = clean(new)
        if i in OVR_TITLE_FIX and t != OVR_TITLE_FIX[i]:
            log(f'U{u_num} Ch2 Before Listening', t, OVR_TITLE_FIX[i],
                'wrong video title pasted from Unit 4; correct title stated at chapter opening and matches all comprehension questions',
                'high')
            t = OVR_TITLE_FIX[i]

        # --- fixed structural roles --------------------------------------
        if i in VIDEO_TITLE_IDX:
            push({'k': 'mediatitle', 'text': VIDEO_TITLE_TEXT[i], 'unit': u_num})
            continue
        if i in READING_TITLE_IDX:
            push({'k': 'readingtitle', 'text': READING_TITLES[i], 'unit': u_num,
                  'img': imgs[0] if imgs else None})
            reading_mode = True
            continue
        if i in DROP_HEADINGS:
            log(f'U{u_num} Ch3 Guided Discussion', t, '(heading removed; questions retained)',
                'locked decision: heading copied from Marriage unit; surrounding questions concern English as a lingua franca',
                'high (verified)')
            continue
        if i == OVR_SC2:
            push({'k': 'sec', 'text': 'Speaking Challenge 2', 'src': i})
            log('U6 Ch4 Pronunciation Clinic', 'unlabelled "Speaking Challenge" paragraph',
                'Speaking Challenge 2 (subsection heading)',
                'locked decision: Unit 6 contains two distinct Speaking Challenge activities; numbered for clarity, content unchanged',
                'high (verified)')
            continue
        if i == OVR_SC1:
            push({'k': 'sec', 'text': 'Speaking Challenge 1', 'src': i})
            log('U6 Ch3', 'Speaking Challenge', 'Speaking Challenge 1',
                'locked decision: distinguish Unit 6’s two distinct Speaking Challenge activities',
                'high (verified)')
            continue

        # --- Before You Read de-duplication ------------------------------
        if t.startswith('Before You ReadDiscuss.'):
            q = BYR_QUESTIONS[u_num]
            push({'k': 'sec', 'text': 'Before You Read'})
            push({'k': 'instr', 'text': 'Discuss.'})
            for qq in q:
                push({'k': 'q', 'text': qq})
            log(f'U{u_num} Ch1', 'doubled "Before You Read / Discuss. / questions" block (verbatim duplicate)',
                'single Before You Read block retained', 'confirmed duplicate content removed (defect D)',
                'high (verified)')
            stray = BYR_STRAY_FILLIN.get(u_num)
            if stray:
                blocks.append({'k': 'fill', 'text': stray})
                log(f'U{u_num} Ch1 Vocabulary Check', f'sentence merged into the Before You Read paragraph: “{stray}”',
                    'sentence re-attached to the Vocabulary Check exercise',
                    'copy-paste contamination; sentence is a fill-in item continuing the Vocabulary Check list',
                    'high (verified)')
            continue

        low = t.lower().rstrip(' .')

        # --- section / subsection classification --------------------------
        if low in SECTION_NAMES:
            push({'k': 'sec', 'text': SECTION_NAMES[low], 'src': i})
            reading_mode = False
            continue
        if low in SUBSEC_NAMES:
            name = SUBSEC_NAMES[low]
            if name == 'Choose the Best Answer' and any(
                    b.get('k') == 'sub' and b.get('text') == 'A. Multiple Choice'
                    for b in blocks):
                push({'k': 'instr', 'text': 'Choose the best answer.'})
            else:
                push({'k': 'sub', 'text': name, 'src': i, 'img': imgs[0] if imgs else None})
            last_sub[0] = name
            continue
        if low in RUNIN_NAMES:
            push({'k': 'subsub', 'text': RUNIN_NAMES[low], 'src': i,
                  'img': imgs[0] if imgs else None})
            last_sub[0] = RUNIN_NAMES[low]
            continue

        # split "Answer the Questions. Answer in complete sentences."
        m = re.match(r'^Answer the Questions\.\s*(.*)$', t)
        if m and chap_is_ch1(c_num):
            push({'k': 'sec', 'text': 'Answer the Questions', 'src': i})
            if m.group(1):
                push({'k': 'instr', 'text': m.group(1)})
            continue

        # pronunciation skill line
        if t.startswith('Skill:') and len(t) < 90:
            push({'k': 'sub', 'text': t, 'src': i})
            continue

        # activity headings
        m = re.match(r'^Activity (\d)\s*[:–-]\s*(.+)$', t)
        if m:
            tail = m.group(2).strip()
            if re.match(r'^(Discuss|Answer|Complete|Rank|Write)\b', tail):
                push({'k': 'sub', 'text': f'Activity {m.group(1)}', 'src': i, 'activity': True})
                push({'k': 'instr', 'text': tail})
            else:
                push({'k': 'sub', 'text': f'Activity {m.group(1)}: {tail}', 'src': i, 'activity': True})
            last_sub[0] = tail
            continue

        # unit topic statement directly after "Chapter 3" marker
        if i == CHAPTER_MARKS_INV.get((u_num, 3), -1) + 1 and not is_instruction(t) and len(t) < 60:
            push({'k': 'mediatitle', 'text': t, 'unit': u_num})
            continue

        # run-in labels like "1. /t/", "2. /d/", "Debate 1", "Topic 1 – ..."
        if re.match(r'^[123]\. /(t|d|ɪd)/', t):
            push({'k': 'sub', 'text': t, 'src': i})
            continue
        m = re.match(r'^(Debate \d)$', t)
        if m:
            push({'k': 'sub', 'text': t, 'src': i})
            continue
        m = re.match(r'^Topic (\d) – (.+)$', t)
        if m:
            push({'k': 'sub', 'text': f'Topic {m.group(1)} – {m.group(2)}', 'src': i})
            continue
        m = re.match(r'^([1-6])\. (Is Love Enough|Communication and Conflict|What Makes a Marriage Last|Marriage and Financial Stress|Marriage in the Modern World|Love across Cultures)', t)
        if m and c_num == 4:
            push({'k': 'sub', 'text': t, 'src': i})
            continue

        # Challenge Question label
        if RE_CHALLENGE.match(t):
            rest = RE_CHALLENGE.sub('', t).strip()
            push({'k': 'subsub', 'text': 'Challenge Question', 'src': i})
            if rest:
                push({'k': 'q', 'text': rest})
            continue

        # "Label. Instruction" jam (e.g. 'Listening Practice. Watch the video...')
        m = re.match(r'^(Listening Practice|Two-Minute Speaking|Individual Presentation \(2 minutes\)|Quick Test)\.\s+(.+)$', t)
        if m:
            push({'k': 'sub', 'text': m.group(1)})
            push({'k': 'p', 'text': m.group(2)})
            last_sub[0] = m.group(1)
            continue

        # write-in list labels -> label + items
        if t in ('Include:', 'Requirements:', 'Task:', 'You must include:',
                 'Prepare arguments about:', 'Ask yourself:', 'Then discuss:',
                 'Your group must decide:', 'Choose one:', 'Then defend your position.',
                 'Then read:', 'Say:', 'Examples:', 'Example:', 'Instead of', 'Say'):
            push({'k': 'label', 'text': t})
            continue

        # true/false statements
        if RE_TF.match(t):
            push({'k': 'tf', 'text': t})
            continue

        # fill-in sentences
        if RE_FILL.search(t) and len(t) > 20 and not t.endswith('?'):
            push({'k': 'fill', 'text': t})
            continue

        # options (single-option paragraph or jammed options)
        if RE_OPTION.match(t):
            stem, opts = split_options(t)
            for o in opts:
                push({'k': 'opt', 'text': o})
            continue
        if re.search(r'[.?!][A-Da-d]\. ', t) and len(t) > 60:
            stem, opts = split_options(t)
            if stem:
                push({'k': 'q', 'text': stem})
            for o in opts:
                push({'k': 'opt', 'text': o})
            log(f'U{u_num} item {i}', 'multiple-choice question and options merged into one paragraph',
                'split into question + option lines', 'copy-paste contamination; structural repair',
                'high (verified)')
            continue
        if re.match(r'^[A-D]\.[^a-z]*[A-D]\.', t):
            stem, opts = split_options(t)
            for o in opts:
                push({'k': 'opt', 'text': o})
            log(f'U{u_num} item {i}', 'answer options merged into one paragraph',
                'split into option lines', 'copy-paste contamination; structural repair',
                'high (verified)')
            continue

        # hand-verified jammed lines
        if i in JAM_FIXES:
            for line in JAM_FIXES[i]:
                push({'k': 'pair' if ('→' in line or ' — ' in line) else 'choice',
                      'text': line})
            log(f'U{u_num} item {i}', 'words/items merged into one line by copy-paste',
                'split into separate lines', 'copy-paste contamination; structural repair',
                'high (verified)')
            continue
        # "Team AAgree" artifacts
        m = re.match(r'^(Team [AB])(Agree|Disagree)$', t)
        if m:
            push({'k': 'p', 'text': f'{m.group(1)}: {m.group(2)}'})
            log(f'U{u_num} item {i}', t, f'{m.group(1)}: {m.group(2)}',
                'jammed words; restored as debate team labels', 'high (verified)')
            continue
        # numbered question stems (often Heading3 in source = defect B)
        if RE_QUESTION.match(t) and not is_instruction(RE_QUESTION.sub('', t)):
            q_text = RE_QUESTION.sub('', t)
            push({'k': 'q', 'text': q_text})
            continue

        # "Second Viewing. Take notes." (unit 1 variant)
        m = re.match(r'^Second Viewing\.?\s+(.+)$', t)
        if m:
            push({'k': 'subsub', 'text': 'Second Viewing'})
            push({'k': 'p', 'text': m.group(1)})
            last_sub[0] = 'Second Viewing'
            continue

        # Clinic Tip note
        if t.startswith('Clinic Tip'):
            push({'k': 'note', 'text': t.replace('Clinic Tip', 'Clinic tip:').replace('Clinic tip: ', 'Clinic tip: ')})
            continue

        # "First Viewing: Listen only." (unit 1)
        if t.startswith('First Viewing'):
            push({'k': 'subsub', 'text': 'First Viewing', 'src': i,
                  'img': imgs[0] if imgs else None})
            rest = t[len('First Viewing'):].lstrip(':. ').strip()
            if rest:
                push({'k': 'p', 'text': rest})
            continue

        # unit 1 heading-styled instruction "Discuss the following questions in groups."
        if t == 'Discuss the following questions in groups.':
            push({'k': 'sec', 'text': 'Group Discussion', 'src': i})
            push({'k': 'instr', 'text': 'Discuss the following questions in groups.'})
            log('U1 Ch2', 'heading-styled instruction “Discuss the following questions in groups.”',
                'section heading “Group Discussion” + instruction line below',
                'defect B (content misclassified as heading); parallel structure with Units 2–8; original words preserved as instruction',
                'high (verified)')
            continue

        # topic line after a 'Topic' subsection, or a short title-case label
        # directly under Discussion N
        if (last_sub[0] == 'Topic' and len(t) < 90 and not t.endswith('.')
                and not is_instruction(t)) or \
           (last_sub[0].startswith('Discussion ') and re.fullmatch(
                r"[A-Z][A-Za-z']+( [A-Za-z'][A-Za-z']*){0,4}", t) is not None
                and len(t.split()) <= 6):
            push({'k': 'topic', 'text': t})
            continue
        # video title line after 'Look at the Title'
        if last_sub[0] == 'Look at the Title' and not is_instruction(t):
            push({'k': 'titleline', 'text': t})
            continue

        # generic instruction vs body paragraph vs question
        if is_instruction(t) and len(t) < 160:
            push({'k': 'instr', 'text': t})
            continue
        if reading_mode and not is_instruction(t):
            push({'k': 'reading', 'text': t, 'img': imgs[0] if imgs else None})
            continue
        looks_q = ('?' in t and re.match(r'^(What|Why|How|Which|Do |Does |Did |Is |Are |Can |Could |Should |Would |Have |Has |Will |If |Imagine|In your opinion|List )', t)) or t.endswith('?')
        if looks_q and len(t) < 300 and last_sub[0] not in ('Example', 'Examples', 'Compare'):
            push({'k': 'q', 'text': t})
            continue
        push({'k': 'p', 'text': t, 'img': imgs[0] if imgs else None})

    # ---- post-pass: renumber duplicate Activity labels inside each section
    renumber_activities(blocks, u_num, c_num)
    fix_student_labels(blocks, u_num)
    reletter_comprehension(blocks, u_num, c_num)
    promote_toolbox_topics(blocks)
    labels_to_lists(blocks)
    return chap

def fix_student_labels(blocks, u_num):
    """U4 Mini Debate: first statement unlabeled, second labeled 'Student B'."""
    for j, b in enumerate(blocks):
        if (b.get('k') == 'sub' and b.get('text') == 'Student B' and j > 0
                and blocks[j-1].get('k') == 'p'
                and not any(x.get('k') == 'sub' and x.get('text') == 'Student A'
                            for x in blocks[:j])):
            blocks.insert(j-1, {'k': 'sub', 'text': 'Student A'})
            log('U4 Ch3 Mini Debate', 'first debate statement had no speaker label '
                '(second was labeled “Student B”)',
                '“Student A” label added before the first statement',
                'structural repair of an obviously missing label; statements unchanged',
                'high (verified)')
            break

def reletter_comprehension(blocks, u_num, c_num):
    """Normalize A./B./C. lettering of comprehension subsections."""
    letter = None
    changes = []
    for b in blocks:
        if b.get('k') == 'sec' and b['text'] in ('Reading Comprehension', 'Listening Comprehension'):
            letter = 'A'
        elif b.get('k') == 'sub':
            m = re.match(r'^([ABC])\. (.+)$', b['text'])
            if m and letter:
                letter = m.group(1)
            elif letter and b['text'] in ('Multiple Choice', 'True or False', 'Short Answer'):
                new = f'{letter}. {b["text"]}'
                changes.append((b['text'], new))
                b['text'] = new
                letter = chr(ord(letter) + 1)
    for old, new in changes:
        log(f'U{u_num} Ch{c_num}', f'“{old}”', f'“{new}”',
            'lettered comprehension subsection sequence repaired (A/B/C)', 'high')

def promote_toolbox_topics(blocks):
    """Chapter 3 topic label after 'Speaking Toolbox' heading -> topic block."""
    for j, b in enumerate(blocks):
        if b.get('k') == 'sec' and b['text'] == 'Speaking Toolbox':
            for k2 in range(j+1, min(j+4, len(blocks))):
                b2 = blocks[k2]
                if b2.get('k') == 'p' and len(b2['text']) < 60 and not is_instruction(b2['text']):
                    b2['k'] = 'topic'
                    return
                if b2.get('k') in ('table', 'sec'):
                    break
            return

def labels_to_lists(blocks):
    """Short unlabeled paragraphs directly after a 'label' block -> list items."""
    for j, b in enumerate(blocks):
        if b.get('k') == 'label':
            k2 = j + 1
            while k2 < len(blocks) and blocks[k2].get('k') == 'p' and \
                    len(blocks[k2]['text']) < 60 and not blocks[k2]['text'].endswith('.'):
                blocks[k2]['k'] = 'li'
                k2 += 1

CHAPTER_MARKS_INV = {(unit_of(ci), cn): ci for ci, (cn, _t) in CHAPTER_MARKS.items()}

def chap_is_ch1(n):
    return n == 1

def renumber_activities(blocks, u_num, c_num):
    """Fix 'Activity 1' repeated (source numbering defect) by renumbering
    sequentially inside the Speaking through Reading section."""
    from collections import defaultdict
    sec_idx = [j for j, b in enumerate(blocks) if b.get('k') == 'sec' and b['text'] == 'Speaking through Reading']
    if not sec_idx:
        return
    start = sec_idx[0]
    end = len(blocks)
    for j in range(start + 1, len(blocks)):
        if blocks[j].get('k') == 'sec':
            end = j
            break
    acts = [j for j in range(start, end) if blocks[j].get('activity')]
    if len(acts) < 2:
        return
    titles = [blocks[j]['text'] for j in acts]
    numbers = [int(re.match(r'Activity (\d)', t).group(1)) for t in titles]
    if numbers == sorted(numbers) and len(set(numbers)) == len(numbers):
        return  # already sequential & unique
    for new_n, j in enumerate(acts, 1):
        old = blocks[j]['text']
        new = re.sub(r'^Activity \d', f'Activity {new_n}', old)
        if new != old:
            blocks[j]['text'] = new
    log(f'U{u_num} Ch{c_num} Speaking through Reading',
        ' / '.join(titles), ' / '.join(blocks[j]['text'] for j in acts),
        'source numbered two or three activities as “Activity 1”; renumbered sequentially, content unchanged',
        'high (verified)')

# ----------------------------------------------------------------------------
# 9. BUILD BOOK TREE
# ----------------------------------------------------------------------------
def resmarten(obj):
    """Final typographic safety net: re-apply smarten() to every text field.

    Idempotent for already-smartened text; catches any block that reached
    the tree through a path that bypassed clean() (e.g. dedup-kept copies).
    """
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == 'text' and isinstance(v, str):
                fixed = smarten(v)
                if fixed != v:
                    resmarten.fixed.append(v)
                    obj[k] = fixed
            else:
                resmarten(v)
    elif isinstance(obj, list):
        for v in obj:
            resmarten(v)

def build():
    log('U5 opener title',
        'Living with AI (Artificial Intelligence)Living with AI '
        '(Artificial Intelligence)Unit 5Unit 5',
        'Unit 5 · Living with AI',
        'doubled unit-title artifact removed; canonical short title used '
        '(parenthetical gloss dropped from opener, series pattern)', 'high')
    log('spelling', 'on-going', 'ongoing',
        'source used both forms; normalized to modern standard spelling used '
        'elsewhere in the same readings', 'high')
    front = parse_front()
    units = parse_units()
    resmarten.fixed = []
    resmarten(front); resmarten(units)
    for orig in resmarten.fixed:
        log('typography', orig, smarten(orig),
            'final-pass apostrophe smartening: block reached tree without clean()',
            'high')
    book = {
        'meta': {
            'title': 'Master Speaking',
            'author': 'Abdul Raziq Nazari',
            'year': '2026',
            'foreword_date': 'September, 2026',
            'source': 'Master Speaking.docx',
        },
        'front': front,
        'units': units,
    }
    json.dump(book, open(os.path.join(BUILD, 'book.json'), 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    json.dump(CHANGES, open(os.path.join(BUILD, 'changelog.json'), 'w', encoding='utf-8'),
              ensure_ascii=False, indent=1)
    # quick stats
    nblocks = sum(len(c['blocks']) for u in units for c in u['chapters'])
    print(f"units: {len(units)}  chapters: {sum(len(u['chapters']) for u in units)}  "
          f"body blocks: {nblocks}  changes logged: {len(CHANGES)}")

if __name__ == '__main__':
    build()
