from datetime import date
import email
from dotenv import load_dotenv
import os
import smtplib
import ssl
load_dotenv()
email = os.getenv('email')
password = os.getenv('password')
host = os.getenv('host')
port = os.getenv('port')
# to = os.getenv('receiver')
sent_from = email
to = ['pyaephyohein.info.3326@gmail.com', 'pyae.phyohein@outlook.com']
subject = 'Test Email from python'
cmd = os.system('date')
body = str(cmd)
print(body)

print (to)
email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, str(body))
context = ssl.create_default_context()
try:
    smtp_server = smtplib.SMTP(host, port)
    smtp_server.ehlo()
    smtp_server.starttls()
    smtp_server.login(email, password)
    smtp_server.sendmail(sent_from, to, email_text)
    smtp_server.close()
    print ("Email sent successfully!")
except Exception as ex:
    print ("Something went wrong….",ex)