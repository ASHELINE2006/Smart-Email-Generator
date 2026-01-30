from email_engine import generate_email

print("=== Intermediate Smart Email Generator ===")

email_type = input("Email Type (leave/complaint/meeting): ").lower()
tone = input("Tone (formal/semi-formal/casual): ").lower()

sender = input("Your Name: ")
receiver = input("Receiver Name: ")

extra_data = {}

if email_type == "leave":
    extra_data["reason"] = input("Reason: ")
    extra_data["days"] = input("Days: ")
    extra_data["start_date"] = input("Start Date: ")

elif email_type == "complaint":
    extra_data["issue"] = input("Issue: ")
    extra_data["impact"] = input("Impact: ")

elif email_type == "meeting":
    extra_data["topic"] = input("Meeting Topic: ")

subject, email = generate_email(
    email_type,
    tone,
    sender,
    receiver,
    **extra_data
)

print("\nSubject:", subject)
print("\nEmail:\n", email)
