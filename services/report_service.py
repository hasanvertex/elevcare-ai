
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def create_report(filename, title, items):

    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()

    story = [
        Paragraph(title, styles["Title"]),
        Spacer(1,20)
    ]

    for item in items:
        story.append(
            Paragraph(str(item), styles["Normal"])
        )

    doc.build(story)
