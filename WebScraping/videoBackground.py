from moviepy.editor import *
import csv
from moviepy.video.fx.all import crop

def vidGenerator():
    #access the base video
    video = VideoFileClip('./video/Vid.mp4')

    #creates a subclip of seconds (x, y)
    video = video.subclip(40, 97)

    audioclip = AudioFileClip("./narration/final.mp3")

    videoclip = video.set_audio(audioclip)

    #videoclip.write_videofile('./output/NarratedVid.mp4')

    with open('./images/lengths.csv') as csvfile:
        reader = csv.reader(csvfile)
        rawLengths = list(reader)

    lengths = rawLengths[0]

    start = 0
    #replace 2 with len(lengths)
    for i in range(6):
        cat = (ImageClip('./images/body' + str(i) + '.png')
                .set_start(start)
                .set_duration(int(lengths[i])) 
                .set_position(("center", "center"))
        )
        start += int(lengths[i])
        videoclip = CompositeVideoClip([videoclip, cat])

    #cancatonates clips
    clip = CompositeVideoClip([videoclip, cat])

    videoclip = crop(videoclip, width = 550, x_center= 1920/2)

    #export 
    videoclip.write_videofile('./output/finished.mp4')