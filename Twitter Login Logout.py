from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os
import time

driver = webdriver.Chrome()
driver.get('https://twitter.com/login')
time.sleep(5)

email_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input'
password_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input'
login_button_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div/div'

email_element = driver.find_element_by_xpath(email_xpath)
password_element = driver.find_element_by_xpath(password_xpath)
login_button_element = driver.find_element_by_xpath(login_button_xpath)

# login form
email_element.send_keys ('username')
password_element.send_keys ('password')
login_button_element.click()
time.sleep(5)

# tweet text
text_box_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div'
text_box_element = driver.find_element_by_xpath(text_box_xpath)
text_box_element.send_keys ('TWEET HERE')

# image
image_xpath = driver.find_element_by_xpath("//input[@accept = 'image/jpeg,image/png,image/webp,image/gif,video/mp4,video/quicktime,video/webm']")
image_xpath.send_keys(os.getcwd() + "//image.png")
    
# tweet button
tweet_button_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]/div'
tweet_button_element = driver.find_element_by_xpath(tweet_button_xpath)
tweet_button_element.click()
time.sleep(10)

# logout 
profile_button_xpath = '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[2]/div/div/div/div/div[2]'
profile_button_element = driver.find_element_by_xpath(profile_button_xpath)
profile_button_element.click()
time.sleep(5)

logout_button_element = driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div[2]/div/div[2]/div/div/div/div/div/a[2]/div/div')
logout_button_element.click()
time.sleep(5)

last_button_element = driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div[3]/div[2]/div').click()
time.sleep(5)

os.system("killall -9 'Google Chrome'")








