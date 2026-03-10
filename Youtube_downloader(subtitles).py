import yt_dlp
import re
import os

def download_subtitle(link):
    
    ydl_opts = {
        'writesubtitles': True,
        'writeautomaticsub': True,
        'subtitlesformat': 'vtt/best',
        'subtitleslangs': ['en-US', 'en-GB', 'en-IN', 'en-AU', 'en-CA', 'en', 'hi'],
        'skip_download': True,
        'outtmpl': '%(title).200s.%(ext)s',
        'no_warnings': True,
        'noplaylist': False,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("Fetching video subtitle information...")
            ydl.download([link])
            print("Download complete!")
            print(f"Files should be visible here: {os.getcwd()}")
            
    except Exception:
        print("Error downloading video: Please try again/later or Update to the latest version of YouTube Downloader")
        
def main_menu():
    while True:
        print("\n============================== YouTube Subtitle Downloader ==============================")
        print("                     =========== by Shreyashish Mitra ===========                          ")
        link = input("Enter the link to download (or type 'exit'): ").strip()
        
        if re.match(r'^https?://', link):
            print("Starting downloading...")
            download_subtitle(link)

        elif link == 'exit':
            print('Exiting Programme Bye bye...')
            break
        
        else:
            print("Invalid input. Please enter a valid YouTube link.")

if __name__ == "__main__":
    main_menu()
