# transcriptocr

Here's the English version of the `README.md` for your GitHub project:

---

# 🧮 AutoGrade OCR

> No more manually typing scores into a calculator! Just upload a screenshot — this tool will automatically read the text and help you calculate what score you need on your next exam.

---

## 📌 Overview

**AutoGrade OCR** is a lightweight tool designed to help students (and teachers) calculate the scores they need on upcoming exams — just by analyzing a screenshot of their grade summary.
Instead of typing scores into a calculator manually, this tool uses **OCR (Optical Character Recognition)** to extract text from images and process the data automatically.

---

## ✨ Features

* Extracts text from screenshots using Tesseract OCR
* Simple web interface using Gradio
* Ready for further expansion into auto-grade calculators or progress trackers

---

## 🔧 Requirements

* Python 3.8+
* Tesseract OCR (installed separately)

### Python Dependencies

Install required packages:

```bash
pip install gradio pytesseract pillow
```

---

## ⚙️ Installation

1. **Install Tesseract OCR**

Download and install from the [official repo](https://github.com/tesseract-ocr/tesseract), or use this default Windows path:

```
C:/Users/yourname/AppData/Local/Programs/Tesseract-OCR/tesseract.exe
```

2. **Update the path in `transcriptorc.py`**

```python
pytesseract.pytesseract.tesseract_cmd = r'C:/Your/Path/To/tesseract.exe'
```

---

## 🚀 Usage

1. Put your screenshot as `sample.png` in the same folder
2. Run the OCR script:

```bash
python transcriptorc.py
```

You’ll see the extracted text printed in the terminal.

3. To launch the basic Gradio web interface (currently a placeholder):

```bash
python app.py
```

This opens a simple greeting interface. You can extend this interface to include OCR-based grading soon.

---

## 📁 Project Structure

```
├── app.py              # Gradio interface (currently basic placeholder)
├── transcriptorc.py    # OCR logic using Tesseract
├── sample.png          # Your screenshot goes here
```

---

## 🚧 To-Do / Planned Features

* Extract numerical data from OCR text
* Calculate required future exam scores based on user goals
* Visualize progress toward grade goals
* Allow direct screen capture upload

---

## 👤 Author

**Seonwoo Kang**
sunwoo99999@gmail.com
Building smart tools to make learning and life easier.
Feel free to contribute, fork, or reach out with ideas!

---

Let me know if you'd like this as a downloadable `README.md` file, or if you plan to change the Gradio interface to calculate scores automatically — I can update this accordingly.
