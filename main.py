import os
from pytubefix import YouTube
from pytubefix.cli import on_progress

url = input("YouTube video ka link paste karein: ")
choice = input("Kya download karna hai? (Type 'mp3' or 'mp4'): ").lower()

try:
    yt = YouTube(url, on_progress_callback=on_progress)
    print(f"\nVideo Mil Gayi: {yt.title}")

    base_folder = "Downloads"
    
    if choice == 'mp3':
        target_folder = os.path.join(base_folder, "MP3")
        print("Audio (MP3) download ho raha hai...")
        stream = yt.streams.get_audio_only()
    else:
        target_folder = os.path.join(base_folder, "MP4")
        print("Video (MP4) download ho raha hai...")
        stream = yt.streams.get_highest_resolution()

    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    print("Downloading... Please wait.")
    out_file = stream.download(output_path=target_folder)

    if choice == 'mp3':
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        if os.path.exists(new_file): 
            os.remove(new_file)
        os.rename(out_file, new_file)
        print(f"\n✅ MP3 Download Complete! Saved in: {target_folder}")
    else:
        print(f"\n✅ MP4 Download Complete! Saved in: {target_folder}")

except Exception as e:
    print(f"Ek error aaya: {e}")