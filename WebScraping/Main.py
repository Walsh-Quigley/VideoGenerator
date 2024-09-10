from jsonparser import *
from narration import *
from storyImages import *
from speedup import *
from videoBackground import *
from cleanup import *

def main(url, pcode):
    jsonScraper(url)
    titleAndBody()
    combine()
    ImageGenerator(url, pcode)
    vidGenerator()
    cleanAll()

main("https://www.reddit.com/r/AmItheAsshole/comments/1f0rugc/aita_for_not_telling_my_gf_about_my_scars/", "1f0rugc" )



