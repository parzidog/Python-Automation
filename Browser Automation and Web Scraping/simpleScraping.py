from selenium import webdriver;

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

def main():
  driver = get_driver();
  element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[1]")

  return element.text

print(main())