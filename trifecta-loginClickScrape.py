from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.get("http://automated.pythonanywhere.com/login/")
    return driver


def clean_txt(text):
    output = float(text.split(": ")[1])
    return output


def logTemperature(temperature):
    with open("temperatures.txt","a") as file:
        file.write(str(temperature) + "\n")


def main():
    driver = get_driver()
    driver.find_element(by="id", value="id_username").send_keys("automated")
    time.sleep(1)
    driver.find_element(by="id", value="id_password").send_keys("automatedautomated" + Keys.RETURN)
    driver.find_element(by="xpath", value="/html/body/nav/div/a").click()
    time.sleep(2)
    text = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]").text
    cleanText = clean_txt(text)
    logTemperature(cleanText)
    return cleanText


print(main())
