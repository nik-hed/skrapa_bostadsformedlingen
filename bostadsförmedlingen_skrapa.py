import urllib.request, json 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib



"""
To configure and get password for email:
Prior to May 30, 2022, it was possible to connect to Gmail’s SMTP server using your regular Gmail password if “2-step verification” was activated. For a higher security standard, Google now requires you to use an “App Password”.
This is a 16-digit passcode that is generated in your Google account and allows less secure apps or devices that don’t support 2-step verification to sign in to your Gmail Account.
Alternatively, there is OAuth 2.0 Gmail authentication mode, but in this case, you’ll need to use the Gmail API sending method in your Python script. 
source: https://mailtrap.io/blog/python-send-email-gmail/
"""

def send_email():  


    msg = MIMEMultipart()
    password = "password-from_email"
    msg['From'] = "from_email"
    to_emails = ['email_1','email_2']   
    msg['To'] =', '.join(to_emails) 
    msg['Subject'] = "Det finns lägenheter i Bostadssnabben hos Bostadsförmedlingen"
    #Email message:
    message='Klicka här:\r\r\nhttps://bostad.stockholm.se/bostad/?s=59.46450&n=59.47182&w=18.11195&e=18.13296&sort=annonserad-fran-desc&bostadSnabbt=1\r\r\n'  
    msg.attach(MIMEText(message, 'plain'))
            
    server = smtplib.SMTP('smtp.gmail.com: 587')
    server.starttls()
    server.login(msg['From'], password)
    msg.as_string()
    server.sendmail(msg['From'], to_emails,msg.as_string() )
    server.quit()


url = "https://bostad.stockholm.se/AllaAnnonser/"
    
    
with urllib.request.urlopen(url) as url:
    all_listed_apartments = json.load(url)


for i in all_listed_apartments:
            
        if i.get('Bostadssnabben')==True or i.get('BostadSnabbt')==True :
            found_apartments=1

        
        
if found_apartments==1: #"Det finns BostadSnabbt/Bostadssnabben - lägenheter hos Bostadsförmedlingen"
     send_email()                
       

# %%
