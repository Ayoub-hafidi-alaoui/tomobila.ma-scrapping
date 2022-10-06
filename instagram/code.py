from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


browser = webdriver.Firefox()



def login(phoneOrEmail, password):
    print("login....")
    browser.get("https://www.instagram.com")
    time.sleep(3)
    browser.find_element("name", "username").send_keys(phoneOrEmail)
    browser.find_element("name", "password").send_keys(password)
    browser.find_element("name", "password").send_keys(Keys.RETURN)
    

def user_navigate(username):
    browser.get(f"https://www.instagram.com/{username}")
    time.sleep(5)
    
    #follow
    print("following the rock")
    follow_btn = browser.find_element("xpath", "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/div[1]/div[2]/div/div[2]/button")
    follow_btn.click()
    time.sleep(3)

    

login("", "")
user_navigate("therock")
#browser.get("https://www.instagram.com/therock")




