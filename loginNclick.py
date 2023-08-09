from selenium import webdriver
#This import gives us access to "Key" functions like enter
from selenium.webdriver.common.keys import Keys
import time

def get_driver():
    # add_argument is used to add command-line arguments to the Chrome webdriver, the options below make browsing easier
    # Created option object using the webdriver Chrome options constructor (aka class)
    options = webdriver.ChromeOptions()
    # To make sure infobar pop-ups are disabled to not mess with script
    options.add_argument("disable-infobars")
    # Will start the browser in a maximized state
    options.add_argument("start-maximized")
    # Helps to avoid possible errors that come up if ran on linux OS / replit
    options.add_argument("disable-dev-shm-usage")
    # Will allow our script to bypass certain security features of Chrome
    options.add_argument("no-sandbox")
    # Helps selenium avoid detection from the browser
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    # Disables auotmationcontrolled feature that helps chrome detect that it is being controlled by selenium
    options.add_argument("disable-blink-features=AutomationControlled")
    #This will keep the page running as long as we do not call the quit function
    options.add_experimental_option("detach",True)
    # Set driver variable to call the chrome driver to utilize options
    # options on the left side is the arugment wd.chrome constructor expects which tells it to use the options we created
    # options on the right represents all the custom "options" we provided
    driver = webdriver.Chrome(options=options)
    # give driver a page to return
    driver.get("http://automated.pythonanywhere.com/login/")
    return driver

def clean_text(text):
    """Extract only the temperature from text"""
    #This will give us a list ([pt1, pt2]), and assign the numerical temp to output as a float
    output = float(text.split(": ")[1])
    return output

def main():
    driver = get_driver()
    driver.find_element(by="id", value="id_username").send_keys("automated")
    #Pause the script for 2 seconds to give time between operations
    time.sleep(2)
    #provide password and then "hit" enter
    driver.find_element(by="id", value="id_password").send_keys("automatedautomated" + Keys.RETURN)
    #After we log in this will take us to the home page
    driver.find_element(by="xpath", value="/html/body/nav/div/a").click()

print(main())