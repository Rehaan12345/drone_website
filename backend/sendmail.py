import smtplib
from email.message import EmailMessage
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# port = 587
# smtp_server = "live.smtp.mailtrap.io"
# login = "crlsclubfinder@gmail.com"
# password = "wmzhhaxtzqnvyuze"

# It will send a copy of the whole email (including subject & body) to BOTH droneworks@bosdroneworks.com AND the person who sent the the email, from the name droneworks@bosdroneworks.com.

# Practice with crlsclubfinder@gmail.com:

# Normal email sending:
def send_mail(email_sender, subject, body):
    email_receiver = "crlsclubfinder@gmail.com"
    email_password = "wmzhhaxtzqnvyuze"
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    # Add SSL (layer of security)
    context = ssl.create_default_context()

    # Log in and send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_receiver, email_password)
        smtp.sendmail(email_receiver, email_sender, em.as_string())

# Email sending with embedded HTML:
def send_alt_mail(email_sender, email_password, email_receiver, subject, text, html):
    port = 587
    smtp_server = "live.smtp.mailtrap.io"
    login = email_sender
    password = email_password
    sender_email = email_sender
    receiver_email = email_receiver
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = receiver_email
    text = text
    html = html
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")
    message.attach(part1)
    message.attach(part2)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(sender_email, password)
        smtp.sendmail(sender_email, receiver_email, message.as_string())