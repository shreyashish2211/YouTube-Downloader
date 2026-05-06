# __YouTube Downloader__ 

__A safe, efficient, and user-friendly tool for downloading YouTube content across different platforms.__

---

## __General Instructions__

1. **Safety First:** This application doesn't contain any malware or viruses. It was created solely for downloading YouTube content safely. I have no intention of making any virus or malware to harm others. I have even shared the source code you can check it out.
2. **Copy URL:** Copy the URL link of the YouTube video you want to download.
3. **Paste URL:** Paste the URL link into "Enter the link to download." when you start the app.
4. **Resolution:** Choose the appropriate resolution you want to have while downloading video.
5. **Choose the appropriate downloader option:**
   - `Youtube_downloader(audio):` Downloads only the audio in `.mp3` format.
   - `Youtube_downloader(subtitles):` Downloads only the Subtitles i.e. English and Hindi subtitles.
   - `Youtube_downloader(thumbnail):` Downloads thumbnails in `.webp` format. (If you need JPG/PNG, use any Photo editing app or an online converter)
   - `Youtube_downloader(video)_V1:` Downloads video with audio (no subtitles).
   - `Youtube_downloader(video)_V2:` Downloads video with audio and subtitles. By default, it downloads English subtitles and auto-generated English subtitles.
6.  **Exit:** Type exit when you are done.
7. **Linux Usage:** If using the compiled binary, navigate to the directory in your terminal and run the program using ./app_name.

---

## __Requirements__

* **Compatibility:** __This works in Windows i.e Windows 10 & 11 and Linux (I can't make macOS build).__
* __If you use the source code instead of the compiled app, you must install the following:__
    * `yt-dlp` library and `yt-dlp-ejs` dependency.
    * `FFmpeg`
    * `Node.js`
* __Installation via Windows, open Terminal or PowerShell(preferably as Administrator) and run this command:__
  ```
  winget install FFmpeg
  ```
  ```
  winget install Nodejs
  ```
* __Installation via Linux, open Terminal and run these command:__

   - For Fedora, CentOS, and RHEL linux distros
     ```
     sudo dnf swap 'ffmpeg-free' 'ffmpeg' --allowerasing
     ```
     ```
     sudo dnf install nodejs
     ```
   - For Ubuntu, Debian, Mint, and Kali Linux distros
     ```
     sudo apt install ffmpeg
     ```
     ```
     sudo apt install nodejs npm 
     ```
   - For other Linux distros/macOS search in the internet 

> [!Note]
> The program may show a security warning the first time you run the compiled app __*on Windows*__. If this happens, click on
>* **More info -> Run anyway.**

---

## __Tips__

- Running PowerShell or Terminal as Administrator is recommended, though not always required(for windows users).
- If subtitles are not available in English/Hindi and even auto-generate English/Hindi, the downloader will try to download auto translated onces but that doesn't work that often.
- Ensure your internet connection is stable and good for faster and more reliable downloads.
- `Youtube_downloader(video)_V2` may fail in downloading some videos and subtitles so use `Youtube_downloader(video)_V1` for video and `Youtube_downloade(subtitles)` for subtitles, to add the subtitles  in the video. **Use this when `Youtube_downloader(video)_V2` fails.**
- If anytime the downloader fails randomly try to download it again and again, then also if it fails please make sure to download the latest build which i will be providing in Github.

---

## Star History

<a href="https://www.star-history.com/?repos=YouTube-Downloader%2FYouTube-Downloader&type=date&logscale=&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/image?repos=YouTube-Downloader/YouTube-Downloader&type=date&theme=dark&logscale&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/image?repos=YouTube-Downloader/YouTube-Downloader&type=date&logscale&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/image?repos=YouTube-Downloader/YouTube-Downloader&type=date&logscale&legend=top-left" />
 </picture>
</a>

Thank you for checking out this project!
