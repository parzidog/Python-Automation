from bs4 import BeautifulSoup
import requests


def get_currency():
    in_curr = input("Enter the input currency as XXX: \n")
    out_curr = input("Enter the output currency as XXX: \n")
    amount = input("Enter the amount of currency that you want converted: \n")
    url = f"https://www.x-rates.com/calculator/?from={in_curr}&to={out_curr}&amount={amount}"
    content = requests.get(url).text
    soup = BeautifulSoup(content, "html.parser")
    currency = soup.find("span", class_="ccOutputRslt").get_text()
    currency = float(currency[0:-4])

    return currency


print(get_currency())
