import json

# Load matched fields
with open("matched_fields.json", "r", encoding="utf-8") as f:
    matched_fields = json.load(f)

# Load HTML template
with open("templates/blank_form.html", "r", encoding="utf-8") as f:
    html_template = f.read()

# Replace placeholders
for field, value in matched_fields.items():
    html_template = html_template.replace(f"{{{{ {field} }}}}", value)

# Save filled form
with open("filled_form.html", "w", encoding="utf-8") as f:
    f.write(html_template)

print("✅ Form filled and saved as filled_form.html")
