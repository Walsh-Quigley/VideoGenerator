from jsonparser import *
from narration import *
from storyImages import *
from videoBackground import *
from speedup import *


def main(url, pcode):
    jsonScraper(url)
    titleAndBody()
    combine()
    ImageGenerator(url, pcode)
    vidGenerator()

main("https://www.reddit.com/r/AmItheAsshole/comments/1by3w5s/aita_for_wearing_fake_freckles/", "1by3w5s" )



