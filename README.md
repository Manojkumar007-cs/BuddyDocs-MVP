# 🧠 BuddyDocs – Smart Document & Form Assistant

BuddyDocs is an AI-powered tool that automates form filling and document extraction using OCR.  
Designed for students, job seekers, and institutions who struggle with repetitive paperwork.

---

## 🔍 Problem Statement

Manual form filling is boring, error-prone, and time-consuming.  
People often re-enter the same data across government, education, or job forms.

---

## 💡 Solution

BuddyDocs uses OCR + smart profile data to:
- 🧾 Extract text from scanned forms (images)
- 🧠 Match fields with user data automatically
- 📝 Fill and generate clean HTML forms

---

## 🚀 Features

- OCR using Tesseract
- Auto field-matching from scanned images
- Smart profile-based form autofill
- HTML form export
- Future-ready: PDF, signature, cloud sync

---

## ⚙️ Tech Stack

| Layer      | Technology               |
|------------|---------------------------|
| Backend    | Python, Flask             |
| OCR        | pytesseract + Tesseract OCR |
| Frontend   | HTML + Jinja Templates    |
| Storage    | JSON files (local MVP)    |
| Dev Tools  | Git, VS Code, Virtualenv  |

---

## 🛠 How to Run Locally

```bash
git clone https://github.com/Manojkumar007-cs/BuddyDocs-MVP.git
cd BuddyDocs-MVP
python -m venv .venv
.venv\Scripts\activate     # (or source .venv/bin/activate on Mac)
pip install -r requirements.txt
python app.py
