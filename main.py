import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendEmail(to, subject, body):
    fromaddr = "email"
    pswrd = "pwd"
    toaddr = to
    msg = MIMEText(body)
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = subject
    #body = body
    #msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, pswrd)
    text = msg.as_string()
    #server.sendmail(fromaddr, toaddr, text)
    server.send_message(msg)
    server.quit()

sendEmail('6315593179@vtext.com','','pwd:spoonassassin7')

import poplib
from email import parser

pop_conn = poplib.POP3_SSL('pop.gmail.com')
pop_conn.user('email')
pop_conn.pass_('pwd')
#Get messages from server:
messages = [pop_conn.retr(i) for i in range(1, len(pop_conn.list()[1]) + 1)]
#print(messages)
for i in range(len(pop_conn.list()[1])):
    for j in pop_conn.retr(i+1)[1]:
        print(j.decode('UTF-8'))
# Concat message pieces:
#messages = ["\n".join(mssg[1]) for mssg in messages]
#Parse message intom an email object:
#messages = [parser.Parser().parsestr(mssg) for mssg in messages]
#for message in messages:
#    print(message['subject'])
pop_conn.quit()
