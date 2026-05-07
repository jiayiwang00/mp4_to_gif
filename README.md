# MP4 to GIF Converter

English | [简体中文](./README_cn.md)

This Python script converts all `.mp4` files in the current folder into `.gif` files.

The converted GIF files will be saved into a folder named `gif/`.  
If the `gif/` folder does not exist, the script will create it automatically.

---

## 1. Create a Virtual Environment

macOS / Linux:

```bash
python3 -m venv .venv
```

Windows:

```bash
python -m venv .venv
```

## 2. Activate the Virtual Environment

macOS / Linux:

```bash
source .venv/bin/activate
```

Windows PowerShell:

```bash
.venv\Scripts\Activate.ps1
```

## 3. Install Dependencies

```bash
pip install --upgrade pip
pip install moviepy
```

## 4. Run the Script

```bash
python mp4_to_gif.py
```

Put your `.mp4` files in this folder, for example:

```text
mp4_to_gif/
├── video1.mp4
├── video2.mp4
└── demo.mp4
```

---

# 5. Project Structure

```text
mp4ToGif/
├── video1.mp4
├── video2.mp4
├── convert_all_mp4_to_gif.py
├── README.md
└── gif/
    ├── video1.gif
    └── video2.gif
```