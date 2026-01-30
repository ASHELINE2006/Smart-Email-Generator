def get_closing(tone):
    closings = {
        "formal": "Sincerely,",
        "semi-formal": "Regards,",
        "casual": "Thanks,"
    }
    return closings.get(tone, "Regards,")
