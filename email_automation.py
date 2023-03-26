import os, smtplib, datetime

def send_mail():
    # fetch environment variables from .bashrc file
    print('Fetching login data.....')
    username = os.environ.get('EMAIL_USER')
    password = os.environ.get('EMAIL_PASS')

    # make smtp object and connect to gmail
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    print('Logging into your email account....')
    smtpObj.login(username, password)

    # make email message
    subject = "Happy Birthday"
    body = "Wish you many many happy returns of the day. HAPPY BIRTHDAY :)"
    # new style string formatting
    # message = f"Subject: {subject}\n\n{body}\n\n- Kavindra"
    # old style string formatting
    message = "Subject: %s\n\n%s\n\n- Kavindra" % (subject, body)

    print('Sending email....')
    smtpObj.sendmail('dev.blearch@gmail.com', receiver, message)
    print('Email sent....')
    smtpObj.quit()

# set today's date in dd-mm format
today = datetime.date.today().strftime('%d-%m') 

birthday_dict = {
    '24-11': 'example1@abc.com',
    '04-09': 'example2@abc.com',
    '17-08': 'example3@abc.com'
    }

receiver = []

for key, value in birthday_dict.items():
    if key == today:
        receiver.append(value)

if len(receiver) > 0:
    print('Today is', today)
    print('Length of receiver is', len(receiver))
    send_mail()
else:
    print('Nobody has birthday today!!')

# send daily good morning message
# if today != '24-11':
#     wish_goodmorning()