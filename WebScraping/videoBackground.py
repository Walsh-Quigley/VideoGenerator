import os
from moviepy.editor import *
import csv
from moviepy.video.fx.all import crop

def vidGenerator():
    # Check if the base video exists
    if os.path.exists('./video/Vid.mp4'):
        # Access the base video
        video = VideoFileClip('./video/Vid.mp4')
        # Create a subclip of seconds (x, y)
        video = video.subclip(0, 75)
    else:
        print("Base video './video/Vid.mp4' not found. Exiting.")
        return

    # Check if the audio file exists
    if os.path.exists("./narration/final.mp3"):
        audioclip = AudioFileClip("./narration/final.mp3")
        videoclip = video.set_audio(audioclip)
    else:
        print("Audio file './narration/final.mp3' not found. Proceeding without audio.")
        videoclip = video

    # Check if the CSV file exists
    if os.path.exists('./images/lengths.csv'):
        with open('./images/lengths.csv') as csvfile:
            reader = csv.reader(csvfile)
            rawLengths = list(reader)
        lengths = rawLengths[0]
    else:
        print("CSV file './images/lengths.csv' not found. Using default lengths.")
        lengths = [5, 5, 5]  # Example default lengths

    start = 0
    # Replace range with len(lengths)
    for i in range(len(lengths)):
        image_path = f'./images/body{i}.png'
        
        # Check if the image file exists
        if os.path.exists(image_path):
            cat = (ImageClip(image_path)
                    .set_start(start)
                    .set_duration(int(lengths[i])) 
                    .set_position(("center", "center")) 
            )
            videoclip = CompositeVideoClip([videoclip, cat])
        else:
            print(f"Image file '{image_path}' not found. Skipping this image.")
        
        start += int(lengths[i])

    # Optionally crop the video
    videoclip = crop(videoclip, width=550, x_center=1920/2)

    # Export the final video
    videoclip.write_videofile('./output/finished.mp4')