# 🛡️ Clipboard Screenshot Redactor — Privacy-first Tool Using OCR

Welcome to this privacy-first automation project that monitors your clipboard for screenshots and **redacts credit card numbers** in real time using **OCR (Tesseract)** and **OpenCV**.

This tool is built for **developers, privacy engineers, and organizations** to protect sensitive visual information from accidental sharing or misuse.

---

## 📚 What This Project Does

✅ Monitors clipboard for screenshots (from Snipping Tool, Win+Shift+S, etc.)  
✅ Uses OCR (Tesseract) to extract and analyze text from screenshots  
✅ Detects and redacts credit card numbers like `1234 5678 9102 3456`  
✅ Replaces detected digits with `XXXX` in the image  
✅ Detects if **Snipping Tool or Snip & Sketch** is opened  
✅ Optionally **auto-closes Snipping Tool** to prevent saving unredacted screenshots  
✅ Shows optional Windows toast alerts when Snipping Tool is opened  

---

## 📦 Prerequisites

### 🧱 Install Python dependencies:
```bash
pip install pytesseract pillow opencv-python pywin32 psutil win10toast
```

## 🧠 Install Tesseract OCR

Download and install Tesseract OCR for Windows from:  
🔗 [Tesseract Installer – UB Mannheim build](https://github.com/UB-Mannheim/tesseract/wiki)

After installation, either:

- ✅ Add Tesseract to your system PATH  
**OR**  
- ✅ Set the path manually in the script:

```bash
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

## 🔍 How to Run

### 1. Clone the repository:
```bash
git clone https://github.com/your-username/clipboard-redactor.git
cd clipboard-redactor
python screenshot_redactor.py
```

Redacted screenshots will be saved in the current folder as PNG files like:
## 🛠️ Configuration
In screenshot_redactor.py, you can configure the following:

```python
AUTO_KILL_SNIPPING_TOOL = True  # ✅ Automatically closes Snipping Tool
SHOW_TOAST = True               # 🔔 Show popup notification when Snipping Tool opens
DEBUG = True                    # 🐞 Show debug logs in terminal
```

To allow users to save screenshots manually, set:
```python
AUTO_KILL_SNIPPING_TOOL = False
```

## 🔐 What It Redacts

✅ Credit card numbers in formats like:

1234567890123456

1234 5678 9012 3456

1234-5678-9012-3456

Want to redact phone numbers, emails, or names?
Extend the regex patterns in the redact_pii_in_image() function.

##📊 Sample Code Snippet

```python
card_pattern = re.compile(r'(?:\d{4}[ \-]?){3}\d{4}')
matches = list(card_pattern.finditer(full_text))

for i, word in words:
    if word in parts:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 255), -1)
        cv2.putText(image, "XXXX", (text_x, text_y), font, font_scale, (0, 0, 0), thickness)
```

## 🧩 Contributing

This project is beginner-friendly and privacy-focused. You can:

- Add support for more PII types (emails, phone numbers)

- Improve accuracy with NLP-based entity recognition

- Create a system tray version

- Package as an .exe using PyInstaller

- Add log reporting and audit trails

## ⭐ Credits
Maintained by [@s-aparnaa](https://github.com/s-aparnaa) 
Inspired by the need for secure screenshot workflows in enterprise environments.

### 🧰 Libraries Used

- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) – Optical character recognition engine
- [OpenCV](https://opencv.org/) – Computer vision library for image processing
- [psutil](https://github.com/giampaolo/psutil) – Process monitoring and system utilities
- [win10toast](https://github.com/jithurjacob/Windows-10-Toast-Notifications) – Windows 10 toast notifications
