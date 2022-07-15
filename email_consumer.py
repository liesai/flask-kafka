from kafka import KafkaConsumer, KafkaProducer
import os
import json
import uuid
from concurrent.futures import ThreadPoolExecutor
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

TOPIC_NAME = "EMAIL"
consumer = KafkaConsumer(
    TOPIC_NAME,
    # value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    value_deserializer=lambda m: json.loads(m),
)
def sendEmail(data):
    print(data)


    msg = MIMEMultipart()
    msg['From'] = 'email@adresse'
    msg['To'] = 'email@adresse'
    msg['Subject'] = 'some changes' 
    message = str(data)
    msg.attach(MIMEText(message))
    mailserver = smtplib.SMTP('smtp.gmail.com', 587)
    mailserver.ehlo()
    mailserver.starttls()
    mailserver.ehlo()
    mailserver.login('email@adresse', 'password')
    mailserver.sendmail(msg['From'], msg['To'], msg.as_string())
    mailserver.quit()


for email in consumer:
	
	email_data = email.value
	
	sendEmail(email_data)