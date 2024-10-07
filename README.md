# skrapa_bostadsformedlingen

https://www.zyte.com/learn/web-scraping-best-practices/: 

The first rule of scraping the web is: do not harm the website. 
The second rule of web crawling is: do NOT harm the website.


Purpose is to search for apartments that has Bostadstyp = **'Bostad Snabbt'**

bostadsförmedlingen_skrapa.py consist of 2 parts:
1. Scraper to get data and check for Bostadssnabben or BostadSnabbt.
2. Send email if there exist Bostadssnabben or BostadSnabbt

.py file is simple and works to run on a **raspberry pi 1b**.

