import yagmail, os, time
from datetime import datetime as dt

sender = "kenneth.schaefer0@gmail.com"
receiver = "parzidog@icloud.com"
password = os.getenv("PASSWORD")

subject = "Testing Email in Python"

content = """Here is the content of the email!!"""

# Send email based on time of day

while True:
    now = dt.now()  # Grab date and time
    if now.hour == 13:  # Execute code if datetime hour is 13
        yag = yagmail.SMTP(user=sender, password=password)
        yag.send(to=receiver, subject=subject, contents=content)
        print("Email Sent!")
        time.sleep(3600)
