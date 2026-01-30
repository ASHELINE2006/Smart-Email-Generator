EMAIL_TEMPLATES = {
    "leave": """
Dear {receiver},

I would like to request leave due to {reason}. 
I will be unavailable for {days} days starting from {start_date}.

Please let me know if any arrangements are needed.

{closing}
{sender}
""",

    "complaint": """
Dear {receiver},

I am writing to bring to your notice an issue regarding {issue}. 
This has caused inconvenience because {impact}.

Kindly take necessary action.

{closing}
{sender}
""",

    "meeting": """
Dear {receiver},

I would like to schedule a meeting regarding {topic}. 
Please let me know your availability.

{closing}
{sender}
"""
}
