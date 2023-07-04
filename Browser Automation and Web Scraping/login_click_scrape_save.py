from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime as dt


def get_driver():
    # Set options to make browsing easier
    path = "/Users/parzidog/Downloads/chromedriver_mac_arm64/chromedriver"
    url = "http://automated.pythonanywhere.com/login"

    options = webdriver.ChromeOptions()
    args = options.add_argument
    args("disable-infobars")
    args("start-maximized")
    args("disable-dev-shm-usage")
    args("no-sandbox")
    args("disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])

    driver = webdriver.Chrome(options=options)
    driver.get(url)

    return driver


def login(driver):
    username = driver.find_element(by="id", value="id_username")
    username.send_keys("automated")

    time.sleep(1)

    password = driver.find_element(by="id", value="id_password")
    password.send_keys("automatedautomated" + Keys.RETURN)

    time.sleep(1)


def getValue(driver):
    value = driver.find_element(by="xpath", value="//*[@id='displaytimer']")
    scraped = value.text.split(": ")
    return scraped[1]


def main():
    driver = get_driver()

    login(driver)

    home = driver.find_element(by="xpath", value="/html/body/nav/div/a")
    home.click()

    time.sleep(3)

    reruns = 0

    while reruns < 4:
        num = getValue(driver)
        with open(
            "/Users/parzidog/Development/Python Automation/Browser Automation and Web Scraping/"
            + str(dt.now())
            + ".txt",
            "w",
        ) as f:
            f.write(num)
        reruns += 1
        time.sleep(2)


main()
