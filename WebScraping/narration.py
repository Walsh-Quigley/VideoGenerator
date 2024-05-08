import json
import os
import shutil
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.chrome.options import Options



def narationGenerator(flag):
    #opens the file i need to read
    if flag == "body":
        with open('./text/story_itself.txt', 'r') as file:
            text = file.read()
    elif flag == "title":
        with open('./text/title_itself.txt', 'r') as file:
            text = file.read()
    else:
        print("for starters, what the hell are u doing")
        quit()
    #driver stast

    driver = webdriver.Firefox()

    driver.maximize_window()


    with open('./json/cookies.json', 'r') as file:
        cookies = json.load(file)


    #go to webpage
    driver.get("https://gesserit.co/#speech")

    for cookie in cookies:
        driver.add_cookie(cookie)

    driver.refresh()


    #wait for the correct area and access it
    element = WebDriverWait(driver, 1000).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="speech"]/textarea'))
    )

    #send the text i want narrated
    element.send_keys(text)

    #scroll down to hit the generate button
    driver.execute_script("window.scrollTo(0, 500)")

    sleep(2)

    voice_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="headlessui-listbox-button-:R1idcipb6:"]'))
    )


    voice_button.click()

    driver.execute_script("window.scrollTo(0, 700)")

    sleep(2)

    male_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="headlessui-listbox-option-:r1:"]'))
    )


    male_button.click()

    sleep(2)

    #find the generate button
    generate_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="speech"]/div/button'))
    )


    #generate the text
    generate_button.click()

    sleep(4)

    download_button = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div[2]/div[4]/div/div/div/div/div/div/a')

    print("here1")

    ####
    #code for saving new cookies if needed

    #sleep(20)
    #cookies = driver.get_cookies()
    #with open('cookies.json', 'w') as file:
        #json.dump(cookies, file) 
    #print("here2")
    ###


    sleep(2)

    download_button.click()

    driver.close()

    if flag == "title":
        os.rename(r"C:\Users\Walsh Quigley\Downloads\text-to-speech.mp3", r".\narration\rawTitle.mp3")
    elif flag == "body":
        sleep(2) 
        os.rename(r"C:\Users\Walsh Quigley\Downloads\text-to-speech.mp3", r".\narration\rawBody.mp3")
    else:
        print("for enders, what the hell are u doing")
        quit()
    


def titleAndBody():
    narationGenerator("title")
    narationGenerator("body")

