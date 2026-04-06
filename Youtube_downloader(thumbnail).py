import yt_dlp
import re
import os

def download_thumbnail(link):
    ydl_opts = {
        'skip_download': True,
        'writethumbnail': True,
        'convertthumbnails': 'png',
        'outtmpl': '%(title).200s.%(ext)s',
        'no_warnings': True,
        'noplaylist': False,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("Fetching video thumbnail information...")
            ydl.download([link])
            print("Download complete!")
            print(f"Files should be visible here: {os.getcwd()}")
            
    except Exception:
        print("Error downloading video: Please try again/later or Update to the latest version of YouTube Downloader")

def main_menu():
    while True:
        print("\n============================== YouTube Thumbnail Downloader ==============================")
        print("                     =========== by Shreyashish Mitra ===========                           ")
        link = input("Enter the link to download (or type 'exit'): ").strip()

        if re.match(r'^https?://', link):
            print("Starting downloading...")
            download_thumbnail(link)

        elif link == 'exit':
            print('Exiting Programme Bye bye...')
            break
        
        else:
            print("Invalid input. Please enter a valid YouTube link.")

if __name__ == "__main__":
    main_menu()
