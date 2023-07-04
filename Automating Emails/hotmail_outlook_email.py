import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

sender = "anything@outlook.com"
receiver = "anything@email.com"

password = os.getenv("PASSWORD")

# Enter plain text to be sent

message = """\
Subject: New Email

Enter your multi-line content email with plain text.
Thank you!
"""

# Enter HTML to be sent after importing email modules

message = MIMEMultipart()
message["From"] = sender
message["To"] = receiver
message["Subject"] = "Subject Text"

body = """
<h1>H1 Tag</h1>
<p>Paragraph</p>
"""

mimetext = MIMEText(body, "html")  # Requires message and encoding

message.attach(mimetext)

# Attach file to email

attachment_path = "users.csv"
attachment_file = open(attachment_path, "rb")
payload = MIMEBase("application", "octate-stream")
payload.set_payload(attachment_file.read())
encoders.encode_base64(payload)
payload.add_header("Content-Disposition", "attachment", filename=attachment_path)
message.attach(payload)

# Obtain SMTP server details and follow the following protocol

server = smtplib.SMTP("smtp.office365.com", 587)
server.starttls()
server.login(sender, password)
message_text = (
    message.as_string()
)  # Only needed for HTML encoded messages, otherwise change message_text to message in following line
server.sendmail(sender, receiver, message_text)
server.quit()
