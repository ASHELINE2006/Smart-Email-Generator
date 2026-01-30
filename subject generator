def generate_subject(email_type, keywords):
    base = {
        "leave": "Leave Request",
        "complaint": "Complaint Regarding",
        "meeting": "Meeting Request",
        "job": "Application for Position"
    }

    subject = base.get(email_type, "Regarding")

    if keywords:
        subject += " - " + keywords[0].title()

    return subject
