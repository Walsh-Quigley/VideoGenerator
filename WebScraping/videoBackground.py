import os
from moviepy.editor import *
import csv
from moviepy.video.fx.all import crop

def vidGenerator():
    #Check to verify base video exists
    if os.path.exists('./video/Vid.mp4'):
        # Access the base video
        video = VideoFileClip('./video/Vid.mp4')
        # Create a subclip of seconds (x, y)
        video = video.subclip(0, 75)
    else:
        #error handling in case video does not exist
        print("Base video './video/Vid.mp4' not found. Exiting.")
        return

    # Check if the audio file exists
    if os.path.exists("./narration/final.mp3"):
        audioclip = AudioFileClip("./narration/final.mp3")
        videoclip = video.set_audio(audioclip)
    else:
        #error handling in case audio does not exist
        print("Audio file './narration/final.mp3' not found. Proceeding without audio.")
        videoclip = video

    # Check if the CSV file exists
    if os.path.exists('./images/lengths.csv'):
        with open('./images/lengths.csv') as csvfile:
            reader = csv.reader(csvfile)
            rawLengths = list(reader)
        lengths = rawLengths[0]
    else:
        #error hadnling in case CSV file does not exist
        print("CSV file './images/lengths.csv' not found. Using default lengths.")
        # Example default lengths
        lengths = [5, 5, 5]  

    #creates a counter to maintain splice beginning
    start = 0
    # Replace range with len(lengths)
    for i in range(len(lengths)):
        #find correct image
        image_path = f'./images/body{i}.png'
        #Check if the image file exists
        if os.path.exists(image_path):
            #if path exists, overlay images starting at correct time, ending at correct time, and positioned correctly
            cat = (ImageClip(image_path)
                    .set_start(start)
                    .set_duration(int(lengths[i])) 
                    .set_position(("center", "center")) 
            )
            #save video to variable
            videoclip = CompositeVideoClip([videoclip, cat])
        else:
            #error handling if the image does not exist
            print(f"Image file '{image_path}' not found. Skipping this image.")
        #maintains counter to continue to splice in correct area
        start += int(lengths[i])

    #Optionally crop the video
    videoclip = crop(videoclip, width=550, x_center=1920/2)

    #Export the final video
    videoclip.write_videofile('./output/finished.mp4')