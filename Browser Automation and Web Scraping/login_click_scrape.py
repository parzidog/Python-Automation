from selenium import webdriver;
from selenium.webdriver.common.keys import Keys
import time;

def get_driver():
  # Set options to make browsing easier
  path = "/Users/parzidog/Downloads/chromedriver_mac_arm64/chromedriver"
  url = "http://automated.pythonanywhere.com/login"

  options = webdriver.ChromeOptions();
  args = options.add_argument;
  args("disable-infobars");
  args("start-maximized");
  args("disable-dev-shm-usage");
  args("no-sandbox");
  args("disable-blink-features=AutomationControlled");
  options.add_experimental_option("excludeSwitches", ["enable-automation"])

  driver=webdriver.Chrome(options=options);
  driver.get(url)

  return driver;

def main() :
  driver = get_driver();

  username = driver.find_element(by = "id", value = "id_username");
  username.send_keys("automated");

  time.sleep(1)

  password = driver.find_element(by = "id", value = "id_password");
  password.send_keys("automatedautomated" + Keys.RETURN);

  time.sleep(1)


  home = driver.find_element(by = "xpath", value = "/html/body/nav/div/a");
  home.click();

  time.sleep(3)

  value = driver.find_element(by = "xpath", value = "//*[@id='displaytimer']")
  scraped = value.text.split(": ")
  return float(scraped[1])

print(main())