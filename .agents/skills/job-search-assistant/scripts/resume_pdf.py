"""Export a structured résumé to PDF and verify its extracted text."""

import argparse
import hashlib
import io
import json
from pathlib import Path
import unicodedata
from xml.sax.saxutils import escape

from pypdf import PdfReader
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont, TTFError
from reportlab.platypus import Paragraph, SimpleDocTemplate


def read_text(value):
    if not isinstance(value, str) or not value.strip():
        raise ValueError("Résumé text fields must be nonempty strings.")
    return " ".join(value.split())


def read_list(value):
    if not isinstance(value, list):
        raise ValueError("Contact, sections, entries, and bullets must be lists.")
    return value


def resume_lines(draft):
    yield "name", read_text(draft["name"])
    contact = read_list(draft["contact"])
    if contact:
        yield "contact", " | ".join(read_text(item) for item in contact)
    if draft.get("summary"):
        yield "summary", read_text(draft["summary"])
    sections = read_list(draft["sections"])
    if not sections:
        raise ValueError("The résumé needs at least one section.")
    for section in sections:
        yield "section", read_text(section["heading"])
        entries = read_list(section["entries"])
        if not entries:
            raise ValueError("Each résumé section needs at least one entry.")
        for entry in entries:
            yield "title", read_text(entry["title"])
            if entry.get("details"):
                yield "details", read_text(entry["details"])
            for bullet in read_list(entry.get("bullets", [])):
                yield "bullet", read_text(bullet)


def normalize(text):
    return " ".join(unicodedata.normalize("NFKC", text).split())


def build_pdf(lines, regular_path, bold_path):
    regular, bold = "Helvetica", "Helvetica-Bold"
    if regular_path and bold_path:
        regular, bold = "ResumeRegular", "ResumeBold"
        pdfmetrics.registerFont(TTFont(regular, str(regular_path)))
        pdfmetrics.registerFont(TTFont(bold, str(bold_path)))

    base = ParagraphStyle(
        "Base", fontName=regular, fontSize=10.5, leading=14, alignment=TA_LEFT
    )
    styles = {
        "name": ParagraphStyle("Name", parent=base, fontName=bold, fontSize=22,
                               leading=26, spaceAfter=5, keepWithNext=True),
        "contact": ParagraphStyle("Contact", parent=base, spaceAfter=9),
        "summary": ParagraphStyle("Summary", parent=base, spaceAfter=7),
        "section": ParagraphStyle("Section", parent=base, fontName=bold, fontSize=12,
                                  spaceBefore=10, spaceAfter=4, keepWithNext=True),
        "title": ParagraphStyle("Title", parent=base, fontName=bold, spaceBefore=4,
                                keepWithNext=True),
        "details": ParagraphStyle("Details", parent=base, spaceAfter=3,
                                  keepWithNext=True),
        "bullet": ParagraphStyle("Bullet", parent=base, leftIndent=13,
                                 bulletIndent=1, spaceAfter=4),
    }

    story = []
    for role, text in lines:
        style = styles[role]
        bullet = "•" if role == "bullet" else None
        characters = text + (bullet or "")
        if regular_path:
            font = pdfmetrics.getFont(style.fontName)
            missing = {character for character in characters if not font.face.charToGlyph.get(ord(character))}
            if missing:
                raise ValueError(f"{style.fontName} lacks these characters: {''.join(sorted(missing))}")
        else:
            try:
                characters.encode("cp1252")
            except UnicodeEncodeError as error:
                raise ValueError("Use --font and --bold-font to render these characters.") from error
        story.append(Paragraph(escape(text), style, bulletText=bullet))

    buffer = io.BytesIO()
    document = SimpleDocTemplate(
        buffer, pagesize=(612, 792), title=f"{lines[0][1]} - Resume",
        leftMargin=46, rightMargin=46, topMargin=43, bottomMargin=43,
    )
    document.build(story)
    return buffer


def verify_pdf(buffer, lines):
    buffer.seek(0)
    pages = PdfReader(buffer).pages
    text = normalize(" ".join(page.extract_text() or "" for page in pages))
    cursor = 0
    for role, value in lines:
        phrase = normalize(value)
        found = text.find(phrase, cursor)
        if found == -1:
            raise ValueError(f"PDF text extraction failed at the {role} field.")
        cursor = found + len(phrase)
    return len(pages)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("draft", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--font", type=Path, help="Regular TrueType font")
    parser.add_argument("--bold-font", type=Path, help="Bold TrueType font")
    args = parser.parse_args()
    if bool(args.font) != bool(args.bold_font):
        parser.error("--font and --bold-font must be supplied together.")
    if args.output.suffix.lower() != ".pdf":
        parser.error("The output filename must end in .pdf.")

    try:
        draft = json.loads(args.draft.read_text(encoding="utf-8"))
        lines = list(resume_lines(draft))
        buffer = build_pdf(lines, args.font, args.bold_font)
        page_count = verify_pdf(buffer, lines)
        payload = buffer.getvalue()
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with args.output.open("xb") as output_file:
            output_file.write(payload)
    except (KeyError, AttributeError, TypeError, ValueError, OSError, TTFError) as error:
        parser.exit(1, f"PDF not exported: {error}\n")

    print(f"Verified extracted text on {page_count} page(s): {args.output}")
    print(f"SHA-256: {hashlib.sha256(payload).hexdigest()}")


if __name__ == "__main__":
    main()
