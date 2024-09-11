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
    #opens the text body file as well as the text title
    if flag == "body":
        with open('./text/story_itself.txt', 'r') as file:
            text = file.read()
    elif flag == "title":
        with open('./text/title_itself.txt', 'r') as file:
            text = file.read()
    #error handling for incorrect flags being passed to function
    else:
        print("for starters, what the hell are u doing")
        quit()

    #driver starting and window maximized
    driver = webdriver.Firefox()
    driver.maximize_window()
    print("diver started")
    #retrieve saved cookies for website login
    with open('./json/cookies.json', 'r') as file:
        cookies = json.load(file)
    print("cookies accessed")
    #use driver to open the TTS webpage
    driver.get("https://gesserit.co/#speech")
    print("TTS website accessed")
    #upload cookies for login 
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.refresh()
    print("Cookies uploaded and page refreshed")

    #wait for the correct area and access it
    element = WebDriverWait(driver, 1000).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="speech"]/textarea'))
    )
    print("text uploaded to text area")
    #sending text to be narrated
    element.send_keys(text)
    #scroll down to hit the generate button
    driver.execute_script("window.scrollTo(0, 500)")
    sleep(2)
    print("sleep executed momentarily for text uploaded")
    #find and open narrator selector
    voice_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div[4]/div/div/div/div/form/div/div[2]'))
    )
    voice_button.click()
    print("Voice Selected")
    #window scrolled to needed section
    driver.execute_script("window.scrollTo(0, 700)")
    sleep(2)
    #finds and selects the correct narrator
    male_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="headlessui-listbox-option-:r1:"]'))
    )
    male_button.click()
    sleep(2)

    #find and select the generate button
    generate_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="speech"]/div/button'))
    )
    generate_button.click()
    sleep(4)
    #downloads the generated audio
    download_button = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div[2]/div[4]/div/div/div/div/div/div/a')
    print("narration generated")
    sleep(2)
    download_button.click()
    print("narration generated")
    #driver quites
    driver.close()

    #flag evaluator to determine where to save unique narration
    if flag == "title":
        os.rename(r"C:\Users\Walsh Quigley\Downloads\text-to-speech.mp3", r".\narration\rawTitle.mp3")
    elif flag == "body":
        sleep(2) 
        os.rename(r"C:\Users\Walsh Quigley\Downloads\text-to-speech.mp3", r".\narration\rawBody.mp3")
    else:
        print("for enders, what the hell are u doing")
        quit()
    
    ####
    #code for saving new cookies if needed
    #
    ####
    #sleep(20)
    #cookies = driver.get_cookies()
    #with open('cookies.json', 'w') as file:
    #    json.dump(cookies, file) 
    #print("here2")
    ###
    

#helper function to run both title and body in a single function
def titleAndBody():
    narationGenerator("title")
    narationGenerator("body")

