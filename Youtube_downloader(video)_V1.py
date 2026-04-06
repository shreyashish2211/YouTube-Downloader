import yt_dlp
import os

def download_video(link, resolution):
    format_string = (
        f"(bestvideo[height<={resolution}]+bestaudio)/"
        f"(bestvideo[height<={resolution}]+bestaudio)/"
        f"best[height<={resolution}]"
    )

    ydl_opts = {
        'format': format_string,
        'javascript': 'node',
        'outtmpl': '%(title).200s.%(ext)s',
        'postprocessors': [{
                'key': 'FFmpegMetadata',  # Key to activate metadata embedding
            },
            {
                'key': 'EmbedThumbnail',  # Optional: Also embed the video thumbnail
                'already_have_thumbnail': False # Let yt-dlp manage the thumbnail file
            }],
        'writethumbnail': True,
        'merge_output_format': 'mp4',    # Merge video and audio into an MP4 file
        'windowsfilenames': True,
        'no_warnings': True,
        'noplaylist': False,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Fetching video information... (Max Resolution: {resolution}p)")
            ydl.download([link])
            print("Download complete!")
            print(f"Files should be visible here: {os.getcwd()}")
            
    except Exception:
        print("Error downloading video: Please try again/later or Update to the latest version of YouTube Downloader")

def main_menu():
    while True:
        print("\n============================== YouTube Video Downloader ==============================")
        print("                     =========== by Shreyashish Mitra ===========                       ")
        link = input("Enter the link to download (or type 'exit'): ").strip()

        if link == 'exit':
            print('Exiting Programme Bye bye...')
            break
        
        resolution = input("Enter the max resolution (e.g., 720, 1080, 1440): ").strip()

        if link and resolution.isdigit():
            print(f"Starting download at {resolution}p resolution...")
            download_video(link, resolution)

        else:
            print("Invalid input. Please enter a valid link and resolution.")
if __name__ == "__main__":
    main_menu()
