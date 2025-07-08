import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

image = Image.open("form.png")
text = pytesseract.image_to_string(image, lang='eng')

with open("output.txt", "w", encoding="utf-8") as f:
    f.write(text)

print("✅ Text extracted and saved to output.txt")


