# QR Generator

A simple desktop application built with Python that generates QR codes from user input URLs or text. The app features a graphical user interface (GUI) using Tkinter and creates QR codes using the `qrcode` library. Generated QR codes are saved as an image (`qr.png`) and displayed within the application.

---

## Features

- User-friendly GUI for entering the URL or text.
- Generates QR codes on button click.
- Displays the generated QR code image inside the app.
- Saves the QR code as a PNG file (`qr.png`).
- Fixed window size to maintain layout consistency.

---

## Requirements

- Python 3.x
- `qrcode` library
- `Pillow` (PIL Fork) library for image handling
- Tkinter (usually comes pre-installed with Python)

You can install the required Python packages using pip:

```bash
pip install qrcode[pil] Pillow
