import yt_dlp 
import re

def download_video(link, resolution):
    # Format selection based on user input
    format_string = (
        f"(bestvideo[vcodec!*=av01][fps>=60][height<={resolution}]+bestaudio[ext=m4a])/"
        f"(bestvideo[vcodec!*=av01][height<={resolution}]+bestaudio[ext=m4a])/"
        f"best[ext=mp4][fps>=60][height<={resolution}]"
    )

    ydl_opts = {
        'format': format_string,
	'javascript': 'node',
	'writesubtitles': True,
        'writeautomaticsub': True,
        'writethumbnail': True,
        'sub_lang': ['en-US', 'en-GB', 'en-IN', 'en-AU', 'en-CA', 'en', 'hi'],
        'outtmpl': '%(title).200s.%(ext)s',
        'postprocessors': [{
                'key': 'FFmpegMetadata',  # Key to activate metadata embedding
            },
            {
                'key': 'EmbedThumbnail',  # Optional: Also embed the video thumbnail
                'already_have_thumbnail': False # Let yt-dlp manage the thumbnail file
            }],
        'merge_output_format': 'mp4',    # Merge video and audio into an MP4 file
        'windowsfilenames': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"Fetching video information... (Max Resolution: {resolution}p)")
            ydl.download([link])
            print("Download complete!")
    except yt_dlp.utils.DownloadError as e:
        print("Error downloading video:", e)
        
def main_menu():
    while True:
        print("\n============================== YouTube Video Downloader ==============================")
        print("                     =========== by Shreyashish Mitra ===========                       ")
        link = input("Enter the link to download (or type 'exit'): ").strip()
        resolution = input("Enter the max resolution (e.g., 720, 1080, 1440): ").strip()

        if link and resolution.isdigit():
            print(f"Starting download at {resolution}p resolution...")
            download_video(link, resolution)

        elif link == 'exit':
            print('Exiting Programme Bye bye...')
            break

        else:
            print("Invalid input. Please enter a valid link and resolution.")
            
if __name__ == "__main__":
    main_menu()
