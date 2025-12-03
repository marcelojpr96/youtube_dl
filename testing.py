import yt_dlp
import pprint


to_download = []
downloaded = []
url = "https://www.youtube.com/playlist?list=PLVvRUZy9YzBnAQBgTWkNb3VLtvEwUeZuF"
ytdlp_options={
    'quiet' : True,
    'extract_flat' : True
}

with yt_dlp.YoutubeDL(ytdlp_options) as ytdl :
    info = ytdl.extract_info(url, download=False)

pprint.pp(info['entries'])
for entry in info['entries'] :
    print(entry['title'])

try :
    with open("downloaded.txt", "r") as file:
        try :
            for line in file :
                print(line)
        except:
            print("nothing to read")
except :
    print("file not found, creating it ..")
    with open("downloaded.txt", "w") as file:
        print("file created")
        
with open("To-download.txt", "r") as file:
    try :
        for line in file :
            print(line)
    except:
        print("nothing to read")