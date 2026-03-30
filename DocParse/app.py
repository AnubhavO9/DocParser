from flask import Flask, render_template, request
import pytesseract
import cv2
import os
from PyPDF2 import PdfReader

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def extract_text_from_image(file_path):
    image = cv2.imread(file_path)

    if image is None:
        return ""

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)[1]

    text = pytesseract.image_to_string(gray)
    return text


def extract_text_from_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""

    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted + "\n"

    return text


def extract_text(file_path):
    extension = os.path.splitext(file_path)[1].lower()

    if extension in [".jpg", ".jpeg", ".png"]:
        return extract_text_from_image(file_path)

    elif extension == ".pdf":
        return extract_text_from_pdf(file_path)

    elif extension == ".txt":
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()

    return ""


@app.route("/", methods=["GET", "POST"])
def home():
    result = ""

    if request.method == "POST":
        uploaded_file = request.files["file"]
        search_text = request.form["search_text"]

        if uploaded_file:
            file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.filename)
            uploaded_file.save(file_path)

            extracted_text = extract_text(file_path)

            matched_lines = []

            for line in extracted_text.splitlines():
                if search_text.lower() in line.lower():
                    matched_lines.append(line.strip())

            if matched_lines:
                result = matched_lines
            else:
                result = ["searched data is not present"]

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)