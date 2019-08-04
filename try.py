import requests
from bs4 import BeautifulSoup
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# browser = webdriver.PhantomJS('phantomjs')
chrome_options = Options()
chrome_options.add_argument("--headless")
browser = webdriver.Chrome(chrome_options=chrome_options)

import html2text
h = html2text.HTML2Text()
h.ignore_links = True
f= open("output.txt","w+")

with open("input.txt") as q:
    for line in q:
        url = line;
        r=requests.get(url)
        soup=BeautifulSoup(r.content,"html5lib")

        temp = soup.findAll("h1",attrs={"class":"AHFaub"})     # Extracting the name of the App
        temp1 = temp[0].findAll("span")
        title = temp1[0].text
        f.write("Name of App :-%s\n" % title)

        description = soup.findAll("meta",attrs={"itemprop":"description"})     # Extracting App description   
        temp = description[0]["content"]
        f.write("Description of App :-\n%s\n" % temp)

        browser.get(url)
        browser.find_element_by_link_text('View details').click()
        time.sleep(2)
        html = browser.page_source
        soup = BeautifulSoup(html,"html5lib")
        permissions = soup.findAll("div",attrs={"class":"fnLizd"})  # Extracting App permissions
        f.write("Permissions of App :-\n%s\n\n" % h.handle(str(permissions)))
f.close()
