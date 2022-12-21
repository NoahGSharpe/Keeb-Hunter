from smtplib import SMTP_SSL
import dotenv


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

    def send_email(self, message):
        with SMTP_SSL(self.server, self.port) as smtp:
            # Login
            smtp.login(self.username, self.password)

            # Send email
            smtp.sendmail(self.username, self.target_email, message)
