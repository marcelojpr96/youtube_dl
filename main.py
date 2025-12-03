import yt_dlp


def get_valid_choice(prompt, options):
    while True:
        choice = input(prompt).lower().strip()
        if choice in options:
            return choice
        print(f"Invalid. Choose from: {', '.join(options)}")


def get_valid_number(prompt, max_num):
    while True:
        try:
            num = int(input(prompt))
            if 1 <= num <= max_num:
                return num
            print(f"Pick 1-{max_num}")
        except ValueError:
            print("Enter a number!")


print("\nYouTube Downloader\n")

while True:
    url = input("\nEnter YouTube URL (or 'quit'): ").strip()
    if url.lower() == "quit":
        break

    # Extract info
    extract_opts = {
        "quiet": True,
        "extractor_args": {"youtube": {"player_client": ["default"]}},
    }

    with yt_dlp.YoutubeDL(extract_opts) as ydl:
        info = ydl.extract_info(url, download=False)

    is_playlist = "entries" in info
    title = info.get("title", "Unknown")
    duration = info.get("duration") or 0

    print(f"\nTitle: {title}")
    print(f"Duration: {duration//60}:{duration%60:02d}")

    # Video or Audio
    mode = get_valid_choice("\nVideo or Audio? (v/a): ", ["v", "a"])

    # VIDEO MODE
    if mode == "v":
        print("\n" + "="*50)
        print("VIDEO QUALITY OPTIONS")
        print("="*50)
        print(f"{'#':<5} {'Quality':<20} {'Description':<25}")
        print("-"*50)
        print(f"{'1':<5} {'Best Available':<20} {'Highest quality (auto)':<25}")
        print(f"{'2':<5} {'1080p Max':<20} {'Full HD':<25}")
        print(f"{'3':<5} {'1440p Max':<20} {'2K':<25}")
        print(f"{'4':<5} {'2160p Max':<20} {'4K':<25}")
        print("="*50)

        q = get_valid_number("\nPick (1-4): ", 4)

        if q == 1:
            format_sel = "bestvideo+bestaudio/best"
        elif q == 2:
            format_sel = "bestvideo[height<=1080]+bestaudio/best"
        elif q == 3:
            format_sel = "bestvideo[height<=1440]+bestaudio/best"
        else:
            format_sel = "bestvideo[height<=2160]+bestaudio/best"

        download_opts = {
            'format': format_sel,
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

    # AUDIO MODE
    else:
        audio_formats = [
            f for f in info.get("formats", [])
            if f.get("vcodec") == "none" and f.get("acodec") != "none"
        ]

        audio_formats = sorted(
            audio_formats, key=lambda x: x.get("abr", 0), reverse=True
        )[:5]

        print("\n" + "="*60)
        print("AUDIO QUALITY OPTIONS")
        print("="*60)
        print(f"{'#':<5} {'Bitrate':<15} {'Format ID':<15} {'Size':<15}")
        print("-"*60)
        
        for i, f in enumerate(audio_formats, 1):
            abr = f.get("abr", "?")
            fid = f['format_id']
            size = f.get("filesize_approx")
            size_str = f"~{size/1e6:.1f}MB" if size else "Unknown"
            print(f"{i:<5} {str(abr) + ' kbps':<15} {fid:<15} {size_str:<15}")
        
        print("="*60)

        pick = input("\nChoose (number or format_id): ")
        if pick.isdigit():
            pick = audio_formats[int(pick) - 1]["format_id"]

        download_opts = {
            "format": pick,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "0",
                },
                {"key": "FFmpegMetadata"},
            ],
            "embed_thumbnail": True,
            "writemetadata": True,
        }

    # Playlist handling
    pl = get_valid_choice("\nDownload entire playlist? (y/n): ", ["y", "n"])
    download_opts["noplaylist"] = (pl == "n")
    download_opts["outtmpl"] = (
        "~/Downloads/Youtube/%(playlist_title)s/%(playlist_index)03d - %(title)s.%(ext)s"
        if pl == "y"
        else "~/Downloads/Youtube/videos/%(title)s.%(ext)s"
    )

    # Download
    print("\nDownloading...")
    with yt_dlp.YoutubeDL(download_opts) as ydl:
        ydl.download([url])
    print("\nDownload complete!")

    again = get_valid_choice("\nAnother download? (y/n): ", ["y", "n"])
    if again == "n":
        break

print("\nDone!")
