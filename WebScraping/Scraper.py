from bs4 import BeautifulSoup
import requests
import json

#page_to_scrape = requests.get("https://quotes.toscrape.com/")
#soup = BeautifulSoup(page_to_scrape.text, "html.parser")

#quotes = soup.findAll("span", attrs= {"class" : "text"})

#authors = soup.findAll("small", attrs = {"class": "author"})

#for qoute in quotes:
    #print(qoute.text)
#for author in authors:
    #print(author.text)





page_to_scrape = requests.get("https://www.reddit.com/r/AmItheAsshole/comments/1bpviga/aita_for_telling_my_sister_i_am_not_the_golden/.json")
#print(page_to_scrape.content)

jsonPretty = json.loads(page_to_scrape.content)

with open("sample.json", "w") as outfile:
    json.dump(jsonPretty, outfile)


#print(jsonPretty)

#CSSselector = '#t3_1boerq9 > div > div._2FCtq-QzlfuN-SwVMUZMM3._2v9pwVh0VUYrmhoMv1tHPm.t3_1boerq9 > div.y8HYJ-y_lTUHkQIc1mdCq._2INHSNB8V5eaWp4P0rY_mE > div > h1'

#XPathSelector = '//*[@id="t3_1boerq9"]/div/div[3]/div[1]/div/h1'

#soup = BeautifulSoup(page_to_scrape.text, "html.parser")

#print(soup.con)

#titles = soup.findAll("h1", attrs={"class":"_eYtD2XCVieq6emjKBH3m _2SdHzo12ISmrC8H86TgSCp _29WrubtjAcKqzJSPdQqQ4h"})

#stories = soup.findAll("p", attrs = {"class": "_1qeIAgB0cPwnLhDF9XSiJM"})

#for title in titles:
    #print(title.text)
#for story in stories:
    #print(story.text)