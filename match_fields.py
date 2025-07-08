import json

# Load extracted OCR text
with open("output.txt", "r", encoding="utf-8") as f:
    form_text = f.read().lower()

# Load saved user profile
with open("user_profile.json", "r", encoding="utf-8") as f:
    user_profile = json.load(f)

# Define keywords for each field
field_keywords = {
    "name": ["name", "full name", "applicant name"],
    "dob": ["dob", "date of birth", "birth date"],
    "email": ["email", "e-mail", "email id"],
    "phone": ["phone", "mobile", "contact number"],
    "address": ["address", "residential address", "permanent address"]
}

# Match fields
matched_fields = {}
for field, keywords in field_keywords.items():
    for keyword in keywords:
        if keyword in form_text:
            matched_fields[field] = user_profile[field]
            break

# Save matched fields to use in HTML fill
with open("matched_fields.json", "w", encoding="utf-8") as f:
    json.dump(matched_fields, f, indent=4)

print("✅ Matched fields saved to matched_fields.json")
