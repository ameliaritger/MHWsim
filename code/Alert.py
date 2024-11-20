import smtplib

smtp_username = "youremail@email.com" # This is the username used to login to your SMTP provider
smtp_password = "password" # This is the password used to login to your SMTP provider
smtp_host = "smtp.gmail.com" # This is the host of the SMTP provider - change if your RPi is not using a gmail account
smtp_port = 587 # This is the port that your SMTP provider uses

sender = "youremail@email.com"
receiver = ["THE PHONE NUMBER WHERE YOU WANT TO RECEIVE TEXT ALERTS"] # must be a list

subject = "YOUR SUBJECT HEADER"

text = "WHAT DO YOU WANT YOUR RPi TO SAY?"

# Prepare actual message

message = """\
From: %s
To: %s
Subject: %s

%s
""" % (sender, ", ".join(receiver), subject, text)

def send_email():
    try:
        server = smtplib.SMTP(smtp_host, smtp_port)
        # identify ourselves to smtp gmail client
        server.ehlo()
        # secure our email with tls encryption
        server.starttls()
        # re-identify ourselves as an encrypted connection
        server.ehlo()
        server.login(smtp_username, smtp_password) # If you don't need to login to your smtp provider, simply remove this line
        server.sendmail(sender, receiver, message)         
        print("Successfully sent email")
    except smtplib.SMTPException:
        print("Error: unable to send email")
