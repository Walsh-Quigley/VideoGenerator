from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys 
import csv
from time import sleep

def ImageGenerator(url, pCode):
    #sentence lenghts and reading times
    lengths = []
    times = []

    driver = webdriver.Chrome()

    driver.set_window_size(430,800)

    driver.get(url)

    #this is dependant on the story
    numberOfParagraphs = 5

    body_element = driver.find_element(By.XPATH, "//body")
    body_element.send_keys(Keys.CONTROL + Keys.SHIFT + 'i')


    print("here")
    sleep(15)


    #get title and length and time
    title = driver.find_element(By.XPATH, '//*[@id="post-title-t3_' + pCode + '"]')
    lengths.append(len(title.text.split()))
    times.append(lengths[0]//3)

    title.screenshot("./images/body0.png")

    #get body and lengths and times
    for i in range(1, numberOfParagraphs+1):
        paragraph = driver.find_element(By.XPATH, '//*[@id="t3_' + pCode + '-post-rtjson-content"]/p[' + str(i) +']')

        lengths.append(len(paragraph.text.split()))
        times.append(lengths[i]//3)
        print(times)



        paragraph.screenshot("./images/body" + str(i) + ".png")


    #save the lengths BUT NOT TIMES YET
    #with open('./images/lengths.csv', 'w') as csvfile:
        #write = csv.writer(csvfile)
        
        #write.writerow(lengths)
        #write.writerow(times)
