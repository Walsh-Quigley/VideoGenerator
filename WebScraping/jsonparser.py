import html
import json
import urllib.request


def jsonScraper(url):
    
    #opens the page I need in its json format and retrieves the data to be parsed
    page = urllib.request.urlopen( url + ".json")
    pjson = page.read()
    pjdata = json.loads(pjson)
    #print(pjdata)


    #writes the data to a file and the file to read from
    with open("./json/rawPost.json", "w") as outfile:
        json.dump(pjdata, outfile)


    with open("./json/rawPost.json", 'r') as f:
        data = json.load(f)

    #sames the title and body text
    title = data[0]['data']['children'][0]['data']['title']
    selftext = data[0]['data']['children'][0]['data']['selftext']

    #saves the text body
    with open('./text/story_itself.txt', "w") as outfile:
        outfile.write(selftext)
        #outfile.write(selftext_paragraph)

    #saves the title text
    with open('./text/title_itself.txt', "w") as outfile:
        outfile.write("Am i the asshole" + title[4:])

