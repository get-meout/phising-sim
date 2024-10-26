import smtplib
from email.mime.text import MIMEText
import time
from helper import prompt


start = "> "
def send_mail():
    from_addr = prompt(start + "From (i.e John@example.com): ")
    password = prompt(start + "Password: ")
    to_addrs  = prompt(start + "To (i.e. Susan@example.com): ").split()
    fraud_from = prompt(start + "Fake name (i.e. Mark Rober): ")
    path = prompt(start + "Html file: ")
    subject = prompt(start + "Title (i.e Important): ")
    file = open(path)
    msg = MIMEText(file.read(), 'html')
    msg['From'] = fraud_from
    msg['To'] = to_addrs
    msg['Subject'] = subject

    if "@gmail" in from_addr:
        print("gmail")
        gmail(msg, from_addr, password, to_addrs)

def gmail(msg, from_addr, password, to_addr):
    print("Message length is", len(msg))
    time.sleep(5)
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(from_addr, password)
    text = msg.as_string()
    server.sendmail(from_addr, to_addr, text)
    server.quit()
    print("Email Sent")
# print("Enter message, end with ^D (Unix) or ^Z (Windows):")

# # Add the From: and To: headers at the start!
# lines = [f"From: {from_addr}", f"To: {', '.join(to_addrs)}", ""]
# while True:
#     try:
#         line = input()
#     except EOFError:
#         break
#     else:
#         lines.append(line)

# msg = "\r\n".join(lines)
