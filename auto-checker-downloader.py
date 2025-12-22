import yt_dlp
import pprint


to_download = []
downloaded = []
url="https://www.youtube.com/playlist?list=PLVvRUZy9YzBnAQBgTWkNb3VLtvEwUeZuF"
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
                downloaded.append(line.strip())
        except:
            print("nothing to read")
except :
    print("file not found, creating it ..")
    with open("./text-files/downloaded.txt", "w") as file:
        print("donwloaded file created")

to_download = [entry["title"].strip() for entry in info["entries"] if entry["title"].strip() not in downloaded]
print(to_download)
#file with links to download
try :
    with open("./text-files/to-download.txt", "w") as file:
        try :
            for entry in to_download: 
                file.write(f"{entry.strip()}\n")
                print(f"written to file {entry}")
        except Exception as e:
            print("nothing to read, ", e)
except :
    
    print("file not found, creating it ..")
    with open("./text-files/to-download.txt", "w") as file:
        print("to download file created")
        

#download the remaining links