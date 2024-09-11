import html
import json
import os
import urllib.request


def jsonScraper(url):
    
    #opens the page I need in its json format and retrieves the data to be parsed
    page = urllib.request.urlopen( url + ".json")
    pjson = page.read()
    pjdata = json.loads(pjson)

    #writes the data to a file and the file to read from
    with open("./json/rawPost.json", "w") as outfile:
        json.dump(pjdata, outfile)
    with open("./json/rawPost.json", 'r') as f:
        data = json.load(f)

    #saves the title and body text
    title = data[0]['data']['children'][0]['data']['title']
    selftext = data[0]['data']['children'][0]['data']['selftext']

    #saves the text body
    with open('./text/story_itself.txt', "w") as outfile:
        outfile.write(selftext)
        #outfile.write(selftext_paragraph)

    #saves the title text
    with open('./text/title_itself.txt', "w") as outfile:
        outfile.write(title)

    #filter out any text that is not part of the main body text
    filter_lines('./text/story_itself.txt')

def filter_lines(filename):
    #open text file we need
    with open(filename, 'r') as file:
        lines = file.readlines()

    #Remove any text that includes the word "edit"
    with open(filename, 'w') as file:
        for line in lines:
            # Split the line into words and check the first 3
            words = line.strip().lower().split()
            if not any("edit" in words[i] for i in range(min(3, len(words)))):
                file.write(line)


