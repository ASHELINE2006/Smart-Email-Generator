from email_data import EMAIL_TEMPLATES
from subject_generator import generate_subject
from tone_adjuster import get_closing
from utils import extract_keywords


def generate_email(email_type, tone, sender, receiver, **kwargs):

    template = EMAIL_TEMPLATES.get(email_type)

    if not template:
        return "Email type not supported"

    closing = get_closing(tone)

    body = template.format(
        receiver=receiver,
        closing=closing,
        sender=sender,
        **kwargs
    )

    keywords = extract_keywords(body)
    subject = generate_subject(email_type, keywords)

    return subject, body
