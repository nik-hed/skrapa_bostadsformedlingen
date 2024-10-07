# skrapa_bostadsformedlingen


The first rule of scraping the web is: do not harm the website. 
The second rule of web crawling is: do NOT harm the website.
https://www.zyte.com/learn/web-scraping-best-practices/

To configure and get password for email:
Prior to May 30, 2022, it was possible to connect to Gmail’s SMTP server using your regular Gmail password if “2-step verification” was activated. For a higher security standard, Google now requires you to use an “App Password”.
This is a 16-digit passcode that is generated in your Google account and allows less secure apps or devices that don’t support 2-step verification to sign in to your Gmail Account.
Alternatively, there is OAuth 2.0 Gmail authentication mode, but in this case, you’ll need to use the Gmail API sending method in your Python script. 
source: https://mailtrap.io/blog/python-send-email-gmail/


Script consist of 2 parts:
1. Scraper to get data and check for Bostadssnabben or BostadSnabbt.
2. Send email if there exist Bostadssnabben or BostadSnabbt

# Purpose was to have something simple that works to run on a rasbperry pi 1b.
