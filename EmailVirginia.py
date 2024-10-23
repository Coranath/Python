import smtplib
import ssl

port = 465  # This is for the SSL

password = "NunyuhBusiness"

context = ssl.create_default_context()

message = "Virginia, here is the quote for the week. Please include it in the bulletin."
receiver = "Aprivateemail$theemailplace,gom"

file = open("quotes.txt", 'r')

quotes = list(file)

file.close()
message = f'{message}\n\n{quotes[0]}'

quotes.append(quotes.pop(0))
listlen = len(quotes)
file = open("quotes.txt", 'w')
for i, val in enumerate(quotes):
    if i < listlen-1:
        val = val.strip("\n")
        file.write(f'{val}\n')
    else:
        file.write(val.strip("\n"))
        
file.close()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context = context) as server:
    
    server.login("levi.moore.email@gmail.com", password)
    server.sendmail("levi.moore.email@gmail.com", receiver, message)
    
print(f"Sent {quotes[listlen-1]} to {receiver}")
input()


