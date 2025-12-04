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


#file with links downloaded
try :
    with open("./text-files/downloaded.txt", "r") as file:
        try :
            #read each line and add it to a list, most likely the url ending
            for line in file :
                print(line)
        except:
            print("nothing to read")
except :
    print("file not found, creating it ..")
    with open("./text-files/downloaded.txt", "w") as file:
        print("donwloaded file created")
        
#file with links to download
try :
    with open("./text-files/to-download.txt", "r") as file:
        try :
            for line in file :
                print(line)
        except:
            print("nothing to read")
except :
    
    print("file not found, creating it ..")
    with open("./text-files/to-download.txt", "w") as file:
        print("to download file created")