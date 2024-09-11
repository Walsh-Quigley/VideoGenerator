from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys 
import csv
from time import sleep

def ImageGenerator(url, pCode):
    #create arrays for sentence lenghts and reading times
    lengths = []
    times = []

    #launches webdriver
    driver = webdriver.Chrome()
    #manipulate driver to correct size so images saved are correct size 
    driver.set_window_size(430,800)
    #pull URL from passed through flag
    driver.get(url)
    #this is dependant on the story, currently hardcoded temporarily
    numberOfParagraphs = 3
    #open page inspecter
    body_element = driver.find_element(By.XPATH, "//body")
    body_element.send_keys(Keys.CONTROL + Keys.SHIFT + 'i')
    #also dependant on the story, opens entire story if neccessary
    read_more_button = driver.find_element(By.XPATH, '//*[@id="t3_1f0rugc-read-more-button"]')
    read_more_button.click()
    print("expand story to full size")
    sleep(5)
    #get title image as well as length of text and calculated time to read length of text
    title = driver.find_element(By.XPATH, '//*[@id="post-title-t3_' + pCode + '"]')
    lengths.append(len(title.text.split()))
    times.append(lengths[0]//3)
    #saves title image
    title.screenshot("./images/body0.png")
    #get body images as well as lengths of texts and times to read them
    #iterate through all paragraphs
    for i in range(1, numberOfParagraphs+1):
        #finds paragraph
        paragraph = driver.find_element(By.XPATH, '//*[@id="t3_' + pCode + '-post-rtjson-content"]/p[' + str(i) +']')
        #saves the length of their text
        lengths.append(len(paragraph.text.split()))
        #calculates time to read the texts
        times.append(lengths[i]//3)
        #saves each screenshot individually
        paragraph.screenshot("./images/body" + str(i) + ".png")


    #save the times taken to read each text section for later calculations
    with open('./images/lengths.csv', 'w') as csvfile:
        write = csv.writer(csvfile)

        #currently uneeded lenghts not saved, left in for future use
        #write.writerow(lengths)
        
        #writes times to be used later
        write.writerow(times)
