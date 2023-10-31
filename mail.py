import smtplib

password = ""

def sendMail(sender: str = "", receiver: str = "", subject: str = "", message: str = ""):
    smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(sender, password)
    message = f"Subject: {subject}\n{message}"
    smtpserver.sendmail(sender, receiver, message)
    print("Gönderim Başarılı!")
    smtpserver.close()