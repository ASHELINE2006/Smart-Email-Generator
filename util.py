def extract_keywords(text):
    words = text.lower().split()
    important = []

    keyword_list = [
        "urgent", "project", "leave", "salary",
        "meeting", "issue", "application"
    ]

    for w in words:
        if w in keyword_list:
            important.append(w)

    return important
