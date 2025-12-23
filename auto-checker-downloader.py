import yt_dlp
import pprint

from redis.commands.search.reducers import tolist

def download_videos(to_download: list[str]) -> str :
    #Download options for 1080p
    download_opts = {
        'format': "bestvideo[height<=1080]+bestaudio/best",
        'merge_output_format': 'mkv',

        # Subtitles
        'write_subs': True,
        'writeautomaticsubs': True,
        'subtitleslangs': ['all'],
        'subtitlesformat': 'vtt',

        # Postprocessors
        'postprocessors': [
            {
                'key': 'FFmpegSubtitlesConvertor',
                'format': 'srt'
            },
            {
                'key': 'FFmpegMetadata',
            }
        ],

        # Metadata
        'addmetadata': True,
        'embed_metadata': True,
        'writemetadata': True,
        'embed_thumbnail': True,
    }
    return "Done"

to_download = []
downloaded = []
#URL to the playlist to download
url="https://www.youtube.com/playlist?list=PLVvRUZy9YzBnAQBgTWkNb3VLtvEwUeZuF"

#testing url
# url = "https://www.youtube.com/playlist?list=PLVvRUZy9YzBmhLaC3B1UuViWf0M1i2OW4"


ytdlp_options={
    'quiet' : True,
    'extract_flat' : True
}

with yt_dlp.YoutubeDL(ytdlp_options) as ytdl :
    #info url to extract info['entries']['title']
    info = ytdl.extract_info(url, download=False)
#print([titles['url'] for titles in info['entries']])

#file with links downloaded
try :
    with open("./text-files/downloaded.txt", "r", encoding="utf-8") as file:
        try :
            #read each line and add it to a list, most likely the url ending
            for line in file :
                downloaded.append(line.strip())
        except:
            print("nothing to read")
except :
    print("file not found, creating it ..")
    with open("./text-files/downloaded.txt", "w") as file:
        print("downloaded file created")
print(downloaded)
to_download_entries = {entry["url"].strip():entry['title'].strip() for entry in info["entries"] if entry["title"].strip() not in downloaded}
to_download = list(to_download_entries.keys())
# print(to_download , "\n",to_download_entries)

#code with ytdlp download

with open("./text-files/downloaded.txt", "a" ,encoding="utf-8") as file :
    for title in to_download_entries.values():
        file.write(title.strip() + "\n")

