from smtplib import SMTP_SSL
from dotenv import load_dotenv
import os


class Emailer:
    def __init__(self):
        # Declare server and port. Use the following for a secure SSL connection
        self.server = 'smtp.gmail.com'
        self.port = 465

        # Load environment variables
        load_dotenv()
        self.email = os.environ['BOT_EMAIL_ADDRESS']
        self.password = os.environ['BOT_EMAIL_PASSWORD']
        self.target_email = os.environ['MY_EMAIL_ADDRESS']

    def send_email(self, subject, message):
        with SMTP_SSL(self.server, self.port) as smtp:
            # Login
            smtp.login(self.email, self.password)

            # Send email
            msg = "Subject: %s\n\n%s" % (subject, message)
            smtp.sendmail(self.email, self.target_email, msg)
