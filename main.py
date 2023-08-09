from selenium import webdriver
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
    # Set driver variable to call the chrome driver to utilize options
    # options on the left side is the arugment wd.chrome constructor expects which tells it to use the options we created
    # options on the right represents all the custom "options" we provided
    driver = webdriver.Chrome(options=options)
    # give driver a page to return
    driver.get("http://automated.pythonanywhere.com")
    return driver

def clean_text(text):
    """Extract only the temperature from text"""
    #This will give us a list ([pt1, pt2]), and assign the numerical temp to output as a float
    output = float(text.split(": ")[1])
    return output

def main():
    driver = get_driver()
    #Pause the script for 2 seconds to give webpage time to load
    time.sleep(2)
    # providing the x-path (via html inspect) of the text we want to scrape
    element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
    return clean_text(element.text)

print(main())