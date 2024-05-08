
from moviepy.video.fx.all import crop
from moviepy.editor import *


video = VideoFileClip('./video/Vid.mp4')

(w, h) = video.size

print(w, h)