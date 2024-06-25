import smtplib
import os
from dotenv import load_dotenv

load_dotenv("/Users/ayan/Downloads/cafe-and-wifi-website-main/environ.env")




ADMIN_EMAIL = os.getenv('MyEmail')
ADMIN_EMAIL_PASSWORD = os.getenv('MyPassword')
SMTP_SERVER = os.getenv('SMTP_SERVER')


def send_email(email, subject, message):
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(ADMIN_EMAIL, ADMIN_EMAIL_PASSWORD)
        connection.sendmail(from_addr=ADMIN_EMAIL,
                            to_addrs=email,
                            msg=f"Subject:{subject}\n\n{message}")
