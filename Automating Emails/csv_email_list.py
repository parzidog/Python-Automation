import yagmail, os, time, pandas
from datetime import datetime as dt

sender = "kenneth.schaefer0@gmail.com"
receiver = "parzidog@icloud.com"
password = os.getenv("PASSWORD")

subject = "Testing Email in Python"

df = pandas.read_csv("users.csv")  # Read data from CSV

yag = yagmail.SMTP(user=sender, password=password)

# Send email based on time of day

for index, row in df.iterrows():
    content = [
        f"""Hello, {row['name']}! Here is your email: {row['email']}""",
        "users.csv",
    ]  # Add contents as a list with the attachment as the second list item
    # yag.send(to=receiver, subject=subject, contents=content)
    print(content)
