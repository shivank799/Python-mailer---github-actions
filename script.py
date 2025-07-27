import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

def send_mail(WORKFLOW_NAME, repo_name):
    # email detail
    Sender_email= os.getenv('SENDER_EMAIL')
    Sender_password= os.getenv('Sender_password')
    Receiver_email= os.getenv('Receiver_email')

    # email message
    Subject= f"workflow { WORKFLOW_NAME} failed for repo {repo_name}"
    Body=f"hi, the workflow{WORKFLOW_NAME}failed for the repo{repo_name}. Please check the logs for more detail.\n more details: \n Run_ID: {WORKFLOW_NAME}"

    msg= MIMEMultipart()
    msg['from']= Sender_email 
    msg['To']= Receiver_email
    msg['subject']= Subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        Server= smtplib.SMTP("smtp.gnail.com" , 587)
        Server.starttls
        Server.login(Sender_email, Receiver_email, text)
        text = msg.as_string
        Server.sendmail(Sender_email, Receiver_email, text)
        Server.quit()
        print("emial sent succesfully")
    except Exception as e:
        print(f"error: {e}")

        send_mail(os.getenv ('WORKFLOW_NAME'), os.getenv('repor_name'), os.getenv('WORKFLOW_RUN_ID'))

print("hello from github action!")
