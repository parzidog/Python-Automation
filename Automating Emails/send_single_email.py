import yagmail
import os

sender = "kenneth.schaefer0@gmail.com"
receiver = "parzidog@icloud.com"
password = os.getenv("PASSWORD")

subject = "Testing Email in Python"

content = """Here is the content of the email!!"""

yag = yagmail.SMTP(user=sender, password=password)
yag.send(to=receiver, subject=subject, contents=content)
print("Email Sent!")
