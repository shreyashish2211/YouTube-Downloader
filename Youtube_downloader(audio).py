import yt_dlp
import re
import os

def download_audio(link):
    ydl_opts = {
        'format': 'bestaudio/best',  # Download only the best audio quality
        'outtmpl': '%(title)s.%(ext)s',  # Save file name for the video title
        'writethumbnail': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',       # Extract audio directly
            'preferredcodec': 'mp3',           # Convert to mp3
            'preferredquality': '320',         # Set mp3 quality
        },
        {
            'key': 'FFmpegMetadata',  # Key to activate metadata embedding
        },
        {
            'key': 'EmbedThumbnail',  # Optional: Also embed the video thumbnail
            'already_have_thumbnail': False # Let yt-dlp manage the thumbnail file
        }],
        'no_warnings': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("Fetching information...")
            ydl.download([link])
            print("Download complete!")
            print(f"Files should be visible here: {os.getcwd()}")
    except yt_dlp.utils.DownloadError as e:
        print("Error downloading Audio:", e)

def main_menu():
    while True:  
        print("\n============================== YouTube Audio Downloader ==============================")
        print("                     =========== by Shreyashish Mitra ===========                           ")
        link = input("Enter the link to download (or type 'exit'): ").strip()
        
        if re.match(r'^https?://', link):
            print("Starting downloading...")
            download_audio(link)

        elif link == 'exit':
            print('Exiting Programme Bye bye...')
            break
        
        else:   
            print("Invalid input. Please enter a valid YouTube link.")
            
if __name__ == "__main__":
    main_menu()
