# __YouTube Downloader__ 

---

## __General Instructions__

1. This application doesn't contain any malware or viruses. It was created solely for downloading YouTube content safely. I have no intention of making any  virus or malware to harm others.
2. Copy the URL link of the YouTube video you want to download.
3. Paste the URL link into "Enter the link to download." when you start the app.
4. Choose the appropriate resolution you want to have while downloading video.
5. Choose the appropriate downloader option:
   - **Youtube_downloader(audio):** Downloads only the audio in wav format(takes alot of disk space).
   - **Youtube_downloader(audio_alt):** Same as Youtube_downloader(audio) but the difference is it saves in mp3 format (takes less disk space).
   - **Youtube_downloader(subtitles):** Downloads only the Subtitles.
   - **Youtube_downloader(thumbnail):** Downloads only Thumbnails, but the only drawback is that its in webp format (I have tried my best in the code to convert it to other picture formats but it                                              doesn't work while downloading the thumbnail). So you have to use a webp to other picture fromat converter online or just use Microsoft photos to convert, or                                            any other photo editing app you use.
   - **Youtube_downloader(video)_V1:** Downloads video with audio (no subtitles).
   - **Youtube_downloader(video)_V2:** Downloads video with audio and subtitles. By default, it downloads English subtitles and auto-generated English subtitles.

---

## __Requirements__

- __This works only in Windows as this is a Windows build(I can't make other os builds).__
- __Make sure you have FFmpeg installed.__
- __To install via Windows, open Terminal or PowerShell(preferably as Administrator) and run this command:__
  ```
  winget install FFmpeg
  ```
- __The program may show a security warning the first time you run it. If this happens, click on More info -> Run anyway.__

---

## __Tips__

- Running PowerShell or Terminal as Administrator is recommended, though not always required.
- If subtitles are not available in English and even auto-generate English, the downloader will try to download auto translated onces.
- Ensure your internet connection is stable and good for faster and more reliable downloads.
- Youtube_downloader(video)_V2 may some fail in downloading videos and subtitles so use Youtube_downloader(video)_V1 for video and Youtube_downloade(subtitles) for subtitles, to add the subtitles  in the video. **Use this when Youtube_downloader(video)_V2 fails.**
- If anytime the downloader fails randomly trying do download it again and again, then also if it fails please make sure to update FFmpeg and download the latest build which i will be providing in Github.

Thank you for downloading
