from pytubefix import YouTube 
from pytubefix.cli import on_progress

try:
    yt_url = input("Enter YouTube URL: ")
    yt = YouTube(yt_url , on_progress_callback=on_progress)
except ValueError as e:
    print(f"Error: {e}")
    exit(1)

user_need = input("for audio inter a - for video inter v")
while user_need not in ["a", "v"]:
    print("Invalid input. Please enter 'a' for audio or 'v' for video.")
    user_need = input("for audio inter a - for video inter v")

if user_need == "v":
    resolutions = yt.streams.filter(file_extension='mp4')
    available_resolutions = []

    for stream in resolutions:
        if stream.resolution is not None:  
            available_resolutions.append(stream.resolution)

    num_resolutions = []

    print("Available resolutions:")
    for res in available_resolutions:
        num_resolutions.append(int(res[:-1]))
        print(f"- {res}p")

    resolution = 0
    while resolution not in num_resolutions:
        try:
            resolution = int(input(f"Select resolution {num_resolutions}: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
    FPSs = yt.streams.filter(res=f'{resolution}p')

    available_FPSs = []

    for stream in FPSs:
        if stream.fps is not None:  
            available_FPSs.append(stream.fps)
    
    print("Available FPSs:")
    for fps in available_FPSs:
        print(f"- {fps} FPS")
    
    Video_FPS = 0
    while Video_FPS not in available_FPSs:
        try:
            Video_FPS = int(input(f"Select FPS {available_FPSs}: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
    print(f"Selected resolution: {resolution}p {Video_FPS}fps and file size: {yt.streams.filter(res=f'{resolution}p').filter(fps=Video_FPS).first().filesize / (1024 * 1024):.2f} MB")
    
    
    download = input("are u sure to download this (yes/no) ? ")
    while download.lower() not in ["yes", "no"]:
        print("Invalid input. Please enter 'yes' or 'no'.")
        download = input("are u sure to download this (yes/no) ? ")

    if download.lower() == "yes":
        try:
            print(yt.title)
            yt.streams.filter(res=f'{resolution}p').filter(fps=Video_FPS).first().download()
            print("Download completed successfully.")
        except Exception as e:
            print(f"An error occurred during download: {e}")
            exit(1)
    elif download.lower() == "no":
        print("bye")
        exit(0)

elif user_need == "a":
    download_audio = input("are u sure to download this (yes/no) ? ")

    while download_audio.lower() not in ["yes", "no"]:
        print("Invalid input. Please enter 'yes' or 'no'.")
        download_audio = input("are u sure to download this (yes/no) ? ")

    if download_audio.lower() == "yes":
        try:
            print(yt.title , f"{yt.streams.get_audio_only().filesize / (1024 * 1024):.2f} MB")
            yt.streams.get_audio_only().download(filename=f"{yt.title}_audio.mp3")
            print("Audio download completed successfully.")

        except Exception as e:
            print(f"An error occurred during audio download: {e}")
            exit(1)

    elif download_audio.lower() == "no":
        print("bye")
        exit(0)
