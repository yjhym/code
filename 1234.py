import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys

cd_path='../../chromedriver'
driver=webdriver.Chrome(cd_path)
url="https://www.youtube.com/results?search_query=Wall+Su"
driver.get(url)
driver.implicitly_wait(3)
time.sleep(3)

driver.find_element_by_xpath("//div[@id='info']/ytd-channel-name[@id='channel-title']").click()
driver.find_element_by_xpath("//div[@id='info']/ytd-channel-name").send_keys(Keys.RETURN)
driver.find_element_by_xpath("//div[@id='tabsContent']/paper-tab[2]/div").click()
body=driver.find_element_by_tag_name("body")
num_of_pagedown=30
while num_of_pagedown:
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.1)
    num_of_pagedown-=1
    try:
        driver.find_element_by_xpath("//*[@id='view-all']/a").click()
        break
    except:
        pass

num_of_pagedown=30
while num_of_pagedown:
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.1)
    num_of_pagedown-=1

html=driver.page_source
soup=BeautifulSoup(html, 'html.parser')
titles=soup.select("ytd-grid-renderer > div > ytd-grid-video-renderer > div > div > div > h3")
views=soup.select("ytd-grid-renderer > div > ytd-grid-video-renderer > div > div > div > div > div > div > span")
for i, title in enumerate(titles):
    print(title.text, views[i*2].text)