
from selenium import webdriver
import time
import keyboard
import getpass
# import pandas as pd
import requests
def Instagram(username,pwd): # keyword is the hashtag to extract and num_iter how much data you want to extract
    ###################################### LOGIN #####################################
    # if num_iter==0:
    #     return print(f'User wants nothing to scrape')
    
    driver = webdriver.Chrome('chromedriver')
    driver.maximize_window()
    driver.get('https://www.instagram.com/')
    time.sleep(3)

    driver.find_element_by_xpath("//div[@class='EPjEi']/form/div[2]/div").click()

    keyboard.write(username)
    keyboard.press_and_release('tab') # go to pwd
    time.sleep(2)
    keyboard.write(pwd)
    keyboard.press_and_release('tab')# go to show button(not necessary)
    keyboard.press_and_release('tab')#go to login button
    keyboard.press_and_release('enter')#press enter to login
    time.sleep(5)

username = input('enter username: ')
pwd = input('enter username: ')
Instagram(username,pwd)    