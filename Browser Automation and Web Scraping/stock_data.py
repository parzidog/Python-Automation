import requests
import time
from datetime import datetime as dt

company = input("Enter the company stick: \n")

from_date = input("Enter start date in yyyy/mm/dd format: \n")
start_date = dt.strptime(from_date, "%Y/%m/%d")
from_epoch = int(time.mktime(start_date.timetuple()))
print(from_epoch)

to_date = input("Enter end date in yyyy/mm/dd format: \n")
end_date = dt.strptime(to_date, "%Y/%m/%d")
to_epoch = int(time.mktime(end_date.timetuple()))

url = f"https://query1.finance.yahoo.com/v7/finance/download/{company}?period1={from_epoch}&period2={to_epoch}&interval=1d&events=history&includeAdjustedClose=true"

headers = {
    "user-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"
}

content = requests.get(url, headers=headers).content

with open("data.csv", "wb") as file:
    file.write(content)
