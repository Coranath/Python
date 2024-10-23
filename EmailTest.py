import smtplib, ssl

port = 465 #This is for the SSL

password = input("Please enter your password: ")

context = ssl.create_default_context()

message = input("Please enter the email which you would like to send: ")
reciever = input("Please enter the recipient's email including the @somemail.com part: ")


with smtplib.SMTP_SSL("smtp.gmail.com", port, context = context) as server:
    
    server.login("PythonEmailsAlerts@gmail.com", password)
    server.sendmail("PythonEmailsAlerts@gmail.com", reciever, message)