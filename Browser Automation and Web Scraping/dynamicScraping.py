from selenium import webdriver;
import time;

def get_driver():
  # Set options to make browsing easier
  path = "/Users/parzidog/Downloads/chromedriver_mac_arm64/chromedriver"
  options = webdriver.ChromeOptions();
  args = options.add_argument;
  args("disable-infobars");
  args("start-maximized");
  args("disable-dev-shm-usage");
  args("no-sandbox");
  args("disable-blink-features=AutomationControlled");
  options.add_experimental_option("excludeSwitches", ["enable-automation"])

  driver=webdriver.Chrome(options=options);
  driver.get("http://automated.pythonanywhere.com")

  return driver;

def clean_text(text) :
  output = text.split(": ")

  return output[1];

def main():
  driver = get_driver();
  time.sleep(2);
  element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")

  return clean_text(element.text)

print(main())