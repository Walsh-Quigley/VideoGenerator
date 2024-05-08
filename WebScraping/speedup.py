from pydub import AudioSegment
from pydub.effects import speedup
import os



def speedUp():

    file_path1 = r"c:/Users/Walsh Quigley/Desktop/PersonalProjects/VideoGenerator/WebScraping/narration/rawTitle.mp3"
    # Load the audio file
    audio = AudioSegment.from_file(file_path1, "mp3")
    new_title = speedup(audio, 1.1 , 110)
    

    file_path2 = r"c:/Users/Walsh Quigley/Desktop/PersonalProjects/VideoGenerator/WebScraping/narration/rawBody.mp3"
    audio = AudioSegment.from_file(file_path2, "mp3")
    new_body = speedup(audio, 1.1 , 110)
    
    combined = new_title + new_body

    combined.export('./narration/final.mp3', format="mp3")

def combine():
    file_path1 = r"c:/Users/Walsh Quigley/Desktop/PersonalProjects/VideoGenerator/WebScraping/narration/rawTitle.mp3"
    title = AudioSegment.from_file(file_path1, "mp3")

    file_path2 = r"c:/Users/Walsh Quigley/Desktop/PersonalProjects/VideoGenerator/WebScraping/narration/rawBody.mp3"
    body = AudioSegment.from_file(file_path2, "mp3")

    combined = title + body

    combined.export('./narration/final.mp3', format="mp3")


