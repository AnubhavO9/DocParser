# 📄 DocParse

A simple web app to extract and search text from documents using OCR.

## 🚀 Features

* Upload files (JPG, PNG, PDF, TXT)
* Extract text using Tesseract OCR
* Search keywords inside documents

## 🛠️ Tech Stack

Python, Flask, OpenCV, PyPDF2, Tesseract OCR

## ⚙️ Setup

```bash
git clone <repo-url>
cd DocParse
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## 🔥 Tesseract Setup (Windows)

Install Tesseract and add in `app.py`:

```python
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

## ▶️ Run

```bash
python app.py
```

Open: http://127.0.0.1:5000/
