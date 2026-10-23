#!/usr/bin/env python3
"""Read-only content, evidence and media audit of the independent coursebook.

Makes editorial checks actionable without presenting heuristics as a language edit.
"""
from __future__ import annotations
import re
from collections import Counter
from pathlib import Path
from urllib.parse import urlsplit

from docx import Document
from docx.opc.constants import RELATIONSHIP_TYPE as RT

ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/"Master Speaking.docx"
OUT=ROOT/"docs"/"master-speaking-content-evidence.md"

TOPICS=[
    "The Power of Communication","Are You a Good Listener?",
    "The Importance of Communication","Dreams Become Reality through Goals",
    "The Power of Emotional Intelligence","Can Money Buy Happiness?",
    "Living with AI: Friend or Foe?","Job Creator or Job Destroyer?",
    "Is Love Enough?","The World Is Getting Smaller",
    "Globalization: Opportunity or Threat?",
    "English: From a Local Language to a Global Lingua Franca"
]

def norm(s):
    return re.sub(r"[^a-z0-9]+"," ",s.casefold()).strip()

def main():
    doc=Document(SOURCE)
    paras=[p.text.strip() for p in doc.paragraphs if p.text.strip()]
    source_urls=[]
    for rel in doc.part.rels.values():
        if rel.is_external:
            target=str(rel.target_ref)
            source_urls.append(target)
    links_from_text=re.findall(r"https?://[^\s<>\"]+", "\n".join(paras), flags=re.I)
    urls=list(dict.fromkeys(source_urls+links_from_text))
    media_related=[(i,p) for i,p in enumerate(paras,1) if re.search(
        r"(?i)\b(?:listen(?:ing)?|watch(?:ing)?|audio|video|podcast|recording|transcript)\b",p)]
    unsupported_claims=[(i,p) for i,p in enumerate(paras,1) if re.search(
        r"(?i)\b(?:research (?:suggests|shows|proves|indicates)|studies (?:show|suggest)|according to (?:research|scientists|a study)|scientists (?:say|have found)|survey (?:found|shows))\b",p)]
    unresolved=[(i,p) for i,p in enumerate(paras,1) if re.search(
        r"(?i)(?:\bTBD\b|\bTODO\b|\[insert\b|\blorem ipsum\b|\bplaceholder\b|www\.[a-z]|(?:week|day)\s*\d+)",p)]
    groups={}
    for topic in TOPICS:
        needle=norm(topic)
        hits=[i for i,p in enumerate(paras) if norm(p)==needle]
        sample=[]
        for hit in hits[:2]:
            relevant=[]
            for line in paras[hit+1:hit+18]:
                if norm(line) in [norm(t) for t in TOPICS]:
                    break
                if len(line)>80:
                    relevant.append(line[:260])
                if len(relevant)>=2:
                    break
            sample.extend(relevant)
        groups[topic]=(len(hits),sample[:3])
    # Look for significant exact repetitions; repeated short section labels are normal.
    repeated=Counter(p for p in paras if len(p)>100)
    repeats=[(cnt,txt) for txt,cnt in repeated.items() if cnt>=3]
    output=[
        "# Master Speaking — content/evidence inventory",
        "",
        "> Machine-extracted REVIEW QUEUE, not an editorial verdict. URLs are unverified; research claims and media instructions are flagged for qualified human checking.",
        "",
        f"- Non-empty body paragraphs: **{len(paras)}**",
        f"- Embedded external relationship URLs: **{len(source_urls)}**",
        f"- Unique URLs (relationships + written): **{len(urls)}**",
        f"- Audio/video/listening-reference paragraphs: **{len(media_related)}**",
        f"- Research/evidence-claim paragraphs: **{len(unsupported_claims)}**",
        f"- Placeholder/scheduling/web-string candidates: **{len(unresolved)}**",
        f"- Paragraphs over 100 characters repeated at least 3 times: **{len(repeats)}**",
        "",
        "## Topic sequence and representative learner text",
        "",
    ]
    for topic,(hits,examples) in groups.items():
        output += [f"### {topic}","",f"Occurrences as stand-alone body paragraphs: **{hits}**",""]
        output += ["> "+sample.replace("\n"," ").replace("|","/") for sample in examples] or ["*No qualifying adjacent longer paragraph extracted.*"]
        output.append("")
    output += ["## Recorded external links (availability and rights not automatically verified)",""]
    if urls:
        for url in urls[:100]:
            domain=urlsplit(url).netloc or "(relative or unparsed)"
            output.append(f"- {domain}: {url.replace(')', '%29')[:240]}")
    else:
        output.append("- **No external relationship or written HTTP link found in the scanned text.** Check how learners obtain the listening/video inputs before publishing.")
    output += ["","## Research/citation assertions needing checking",""]
    for n,p in unsupported_claims[:60]:
        output.append(f"- Body paragraph {n}: {p[:330]}")
    if not unsupported_claims:
        output.append("- No keyword-pattern matches; this does not mean all factual claims are verified.")
    output += ["","## Listening/media instruction sampling",""]
    for n,p in media_related[:45]:
        output.append(f"- Body paragraph {n}: {p[:250]}")
    output += ["","## Placeholder, repeated-text and scheduling candidates",""]
    for n,p in unresolved[:35]:
        output.append(f"- Body paragraph {n}: {p[:220]}")
    for count,p in sorted(repeats,reverse=True)[:20]:
        output.append(f"- Repeated {count}×: {p[:220]}")
    if not unresolved and not repeats:
        output.append("- None flagged by the specified heuristics.")
    output += ["","## Editorial action checklist","",
               "- Confirm every listening and video reference has a playable, legally usable asset, backup transcript and learner-facing access path.",
               "- Cross-check factual and research assertions against dated, cited primary sources; delete unsubstantiated claims.",
               "- Inspect all lesson-to-lesson repetitions and explicit lesson schedule labels for intentionality.",
               "- Re-read all open speaking prompts and model exchanges for linguistic naturalness, accessibility and assessment alignment.",
               ""]
    OUT.write_text("\n".join(output),encoding="utf-8")
    print(f"MASTER CONTENT INVENTORY: links={len(urls)}, media mentions={len(media_related)}, evidence claims={len(unsupported_claims)}, source excerpts={len(groups)}.")
    print("Report:",OUT)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
