import smtplib
import os
import imghdr
from dotenv import load_dotenv
from email.message import EmailMessage

load_dotenv()

gmail_user = os.getenv('GMAIL_USER')
gmail_password = os.getenv('PASSWORD')



def send_email(predictedPerson,image_file):
    msg = EmailMessage()
    msg['Subject'] = 'Banned Person Detected'
    msg['From'] = gmail_user
    msg['To'] = gmail_user
    print(predictedPerson)
    msg.set_content(f'{predictedPerson} has been detected at your door')

    with open(image_file,'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name

    msg.add_attachment(file_data,
                        maintype='image',
                        subtype=file_type,
                        filename=file_name)


    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        smtp.login(gmail_user,gmail_password)

        smtp.send_message(msg)