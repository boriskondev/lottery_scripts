import smtplib
import ssl


port = 465
smtp_server = "smtp.gmail.com"
sender_email = "pythonemailtests@gmail.com"
password = input("Enter password: ")
receiver_email = "b.kondev@publicis-dialog.bg"
message = """\
Subject: Hi there

This message is send from Python.
"""

context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)