# 🎥 YouTube Video Downloader

A powerful GUI-based YouTube Video & Playlist Downloader built with Python and Tkinter.

---

## ✨ Features

- 🔗 Supports both **YouTube videos and playlists**
- 🖼️ **Thumbnail preview** before downloading
- 🎚️ Choose quality: **720p / 1080p / 1440p**
- 📁 Select custom **download location**
- 📊 Progress bar for live download status
- 📜 Log area to show status and errors
- ✅ Automatically resets UI after each download

---

## ⚙️ Requirements

Make sure you have the following installed:

- **Python 3.8+**
- Python libraries:
  - `yt-dlp`
  - `Pillow`
  - `requests`
  - `tkinter` (comes with Python)

---

## 🧑‍💻 Installation Guide

### ✅ 1. Install Python

1. Download Python from [python.org](https://www.python.org/downloads/)
2. During installation, **check** ✅ **"Add Python to PATH"**
3. Confirm it's installed:

```bash
python --version
```

---

### 📁 2. Clone or Download the Project

#### Option A: Clone via Git

```bash
git clone https://github.com/adarshh-s/youtube-video-downloader.git
cd youtube-video-downloader
```

### 📦 3. Create and Activate a Virtual Environment (Recommended)

```bash
python -m venv venv
venv\Scripts\activate
```

> Mac/Linux:
>
> ```bash
> source venv/bin/activate
> ```

---

### 📥 4. Install All Dependencies

Install libraries individually:

```bash
pip install yt-dlp pillow requests
```

✅ Or install from `requirements.txt` if available:

```bash
pip install -r requirements.txt
```

---

### ▶️ 5. Run the App

```bash
python youtube_downloader.py
```

🎉 Enjoy downloading videos and playlists easily!

---

## 🛠️ Convert to `.exe` (For Windows Users)

Use **PyInstaller** to convert Python script to executable.

### Step 1: Install PyInstaller

```bash
pip install pyinstaller
```

### Step 2: Create Executable

```bash
pyinstaller --noconfirm --onefile --windowed  youtube_downloader.py
```

After it finishes, go to `dist/` folder to find your `.exe` file.

---

## 📂 Project Structure

```
youtube-downloader/
├── youtube_downloader.py
├── requirements.txt
├── README.md
```

---

## 👨‍💻 Author

**Adarsh**  
Built with ❤️ and Python  
GitHub: [@adarshh-s](https://github.com/adarshh-s)

---
