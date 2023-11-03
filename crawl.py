import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import time

chrome_options = Options()
#chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
service = Service(executable_path=r'/usr/bin/chromedriver')

def getHtml(url):
    # Mozilla/5.0 (Windows NT 10.0; WOW64; rv:57.0) Gecko/20100101 Firefox/57.0
    try:
        response = requests.get(url,timeout=40,headers=headers)
        response.raise_for_status()

        response.encoding = response.apparent_encoding

        return response.text
    except:
        import traceback
        traceback.print_exc()

with open('data.txt','r') as f:
    data=f.read().splitlines()

browser = webdriver.Chrome(service=service, options=chrome_options)

urlBase='https://ieeexplore.ieee.org/xpl/tocresult.jsp?isnumber=4359912'

for i in range(len(data)):
    doi=data[i]
    url=urlBase
    browser.get(url)
    time.sleep(5)
    for i in range(1,26):
        Paper_id[i] = browser.find_element(By.XPATH, '//*[@id="publicationIssueMainContent global-margin-px"]/div[2]/div/div[2]/div/xpl-issue-results-list/div[2]/div[' + i + ']/div/xpl-issue-results-items/div[1]/div[1]/div[2]/h2/a')
        print(Paper_id)
    
    


    
    with open(fname,'ab+') as f:
        print('start download file ',fname)
        f.write(response.content)
