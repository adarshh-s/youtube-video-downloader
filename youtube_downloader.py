import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import threading
import yt_dlp
import os
import requests
from PIL import Image, ImageTk
from io import BytesIO

class YouTubeDownloaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Video Downloader")
        self.root.geometry("600x600")
        self.root.resizable(False, False)

        # Variables
        self.download_path = tk.StringVar()
        self.quality_var = tk.StringVar(value="1080")

        # URL Input
        tk.Label(root, text="🎥 Paste YouTube video or playlist URL:", font=("Arial", 12)).pack(pady=10)
        self.url_entry = tk.Entry(root, width=70)
        self.url_entry.pack(pady=5)

        # Thumbnail Preview
        self.thumbnail_label = tk.Label(root)
        self.thumbnail_label.pack(pady=5)

        # Quality Selection
        tk.Label(root, text="Select Quality:", font=("Arial", 11)).pack(pady=5)
        quality_frame = tk.Frame(root)
        quality_frame.pack()
        for q in ["720", "1080", "1440"]:
            ttk.Radiobutton(quality_frame, text=f"{q}p", value=q, variable=self.quality_var).pack(side=tk.LEFT, padx=10)

        # Folder Selection
        folder_frame = tk.Frame(root)
        folder_frame.pack(pady=10)
        tk.Entry(folder_frame, textvariable=self.download_path, width=50, state="readonly").pack(side=tk.LEFT, padx=5)
        ttk.Button(folder_frame, text="📁 Choose Folder", command=self.select_folder).pack(side=tk.LEFT)

        # Progress Bar
        self.progress = ttk.Progressbar(root, orient='horizontal', length=500, mode='determinate')
        self.progress.pack(pady=15)

        # Log Area
        self.log_text = tk.Text(root, height=8, width=72, bg="#f0f0f0")
        self.log_text.pack(pady=5)

        # Download Button
        self.download_button = ttk.Button(root, text="⬇️ Download", command=self.start_download)
        self.download_button.pack(pady=10)

    def select_folder(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.download_path.set(folder_selected)

    def log(self, message):
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)

    def show_thumbnail(self, url):
        try:
            ydl_opts = {'quiet': True, 'skip_download': True}
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(url, download=False)
                thumbnail_url = info_dict.get('thumbnail')

                if thumbnail_url:
                    response = requests.get(thumbnail_url)
                    image_data = Image.open(BytesIO(response.content))
                    image_data = image_data.resize((320, 180))  # Resize for display
                    tk_image = ImageTk.PhotoImage(image_data)

                    self.thumbnail_label.configure(image=tk_image)
                    self.thumbnail_label.image = tk_image
        except Exception as e:
            self.log(f"⚠️ Couldn't load thumbnail: {e}")

    def start_download(self):
        url = self.url_entry.get()
        folder = self.download_path.get()

        if not url.strip():
            messagebox.showwarning("Warning", "Please enter a YouTube URL.")
            return
        if not folder:
            messagebox.showwarning("Warning", "Please choose a download folder.")
            return

        self.show_thumbnail(url)  # Show thumbnail first
        self.download_button.config(state=tk.DISABLED)
        self.progress['value'] = 0
        self.log("📦 Starting download...")
        threading.Thread(target=self.download_video, args=(url, folder)).start()

    def progress_hook(self, d):
        if d['status'] == 'downloading':
            percent = d.get('_percent_str', '0.0%').strip().replace('%', '')
            try:
                self.progress['value'] = float(percent)
            except:
                pass
        elif d['status'] == 'finished':
            self.log("✅ Download completed!\n")

    def download_video(self, url, folder):
        quality = self.quality_var.get()
        self.log(f"📽 Downloading at {quality}p quality...")

        options = {
            'format': f'bestvideo[height<={quality}]+bestaudio/best[height<={quality}]',
            'merge_output_format': 'mp4',
            'outtmpl': os.path.join(folder, '%(title)s.%(ext)s'),
            'progress_hooks': [self.progress_hook],
            'noplaylist': False  # Enables playlist download
        }

        try:
            with yt_dlp.YoutubeDL(options) as ydl:
                ydl.download([url])
        except Exception as e:
            self.log(f"❌ Error: {e}")
        finally:
            self.download_button.config(state=tk.NORMAL)

# Launch the App
if __name__ == "__main__":
    root = tk.Tk()
    app = YouTubeDownloaderApp(root)
    root.mainloop()
