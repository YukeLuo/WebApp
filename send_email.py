from email.mime.text import MIMEText
import smtplib
def send_email(email, height, average_height, count):
    from_email = "luoyukeway@gmail.com"
    from_password = "Way13472837784!"
    to_email = email

    subject = "Height Data"
    message = "Hi there, Thank you for using Yuke's Web App! Your height is <strong>%s</strong>. Average height of is <strong>%s</strong> out of <strong>%s</strong> total users." % (height, average_height, count)

    msg = MIMEText(message, "html")
    msg["Subject"] = subject
    msg["To"] = to_email
    msg["From"] = from_email

    gmail = smtplib.SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)