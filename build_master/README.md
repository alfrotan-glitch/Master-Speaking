# Master Speaking publication workflow

The **independent** root manuscript, \`Master Speaking.docx\`, is the source of truth for this publication experiment. It is a different book from the separately maintained 16-lesson \`Grammar for Special Speaking\` publication.

Run \`python tools/build_master_publication.py\` with LibreOffice Writer and Pandoc installed and the dependencies in \`build_spec/requirements.txt\`. This creates an editable metadata-corrected Word copy, A4 PDF, reflowable EPUB3 and self-contained HTML in \`proof/\`; it **does not edit the original**.

The pipeline checks file integrity, document length, A4 PDF pages, EPUB package structure, and basic text preservation, and writes \`docs/master-speaking-publication-audit.md\`. All files in \`proof/\` are **proofs, not approved final releases**. Before publishing or selling the manuscript, visually proof every page, test the ebook in multiple readers, inspect image/alt-text fidelity and table pagination, confirm copyright permissions, verify all listening assets and links, and complete an expert content and teacher review. Do not equate a successful conversion with correct educational content or rights clearance.

## Twenty-angle release audit

Run `python tools/quality_audit_20.py` after generating the Master Speaking proofs and the Student/Teacher grammar books. Its evidence report is in [docs/quality-audit-20-dimensions.md](../docs/quality-audit-20-dimensions.md). A clean structural run does not certify the human-reviewed criteria or close image-alt, copyright, classroom/pilot, print-proof, and listening/media gates.
