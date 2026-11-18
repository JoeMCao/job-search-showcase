# Résumé and review packet

Read the selected posting and confirmed experience. Identify the main requirements and cite the source résumé or a candidate-confirmed detail for each major claim. Preserve actual titles, dates, scope, and outcomes. Use the posting's language where it matches the experience. Leave unsupported requirements visible as gaps.

Generate an editable JSON draft and a text-based PDF in the selected role folder, for example `resume-r1.json` and `resume-r1.pdf`. Match the résumé to the role while retaining enough context to make each claim intelligible. Include relevant employment, education, and skills from the confirmed record.

The PDF exporter accepts this format. Omit `summary`, `details`, or `bullets` when unused.

```json
{
  "name": "Maya Chen",
  "contact": ["Portland, OR", "maya.chen@example.invalid"],
  "summary": "Product manager with experience improving self-serve setup.",
  "sections": [{
    "heading": "Experience",
    "entries": [{
      "title": "Product Manager, Mallowdesk",
      "details": "Sep 2022 to present",
      "bullets": ["Shipped a workspace setup checklist with Design and Engineering."]
    }]
  }]
}
```

Use the bundled Python environment if it has `reportlab` and `pypdf`. Otherwise use a local virtual environment and install `requirements.txt`. From the repository root, run:

```sh
python .agents/skills/job-search-assistant/scripts/resume_pdf.py path/to/resume-r1.json path/to/resume-r1.pdf
```

Use canonical contact URLs without tracking parameters. If your résumé needs characters outside Windows-1252, use `--font path/to/regular.ttf --bold-font path/to/bold.ttf` with fonts that cover them. Export verifies that the PDF contains the draft's text in reading order. Render and inspect each page for clipping, unwanted wraps, and unreadable glyphs. If visual review is unavailable, mark it pending and ask the candidate to verify the PDF. Preserve the editable draft if PDF generation fails and report the exact blocker.

Write a brief PDF grade in the review packet. Give each item 0 (failed), 1 (partial), or 2 (passed), with one concrete reason. Mark untested checks as pending and leave the total pending until all five have scores.

| Check | What earns 2 |
| --- | --- |
| Evidence | The source supports every material claim and metric. |
| Fit | The strongest relevant evidence is easy to find, and any gaps are explained in the packet. |
| Specificity | Bullets distinguish what the candidate did from the outcomes they observed. |
| Text extraction | The PDF text check passes, with clear section order and complete content. |
| Layout | All pages are legible with no clipping or overlapping text. |

Resolve unsupported claims or PDF failures before presenting the file as ready. Include the PDF path and SHA-256, the requirement-to-evidence notes, proposed answers to visible screening questions, and fields needing candidate input. Save the packet with the same revision number as the PDF. Candidate approval applies to the specified revision.
