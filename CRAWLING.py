from bs4 import BeautifulSoup
import time
from urllib import parse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# ChromeDriver 설정
cd_path = 'chromedriver-win64/chromedriver.exe'
options = Options()
name=input("지역 이름 (예시:강남구 대치4동)").strip()
options.add_argument("--start-maximized")
service = Service(cd_path)
driver = webdriver.Chrome(service=service, options=options)
url="https://weather.naver.com"
driver.get(url)
driver.implicitly_wait(10)
time.sleep(3)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
try:
    channel_element = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div/div[3]/button")
    channel_element.click()
except:
    print("error")
try:
    element = driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div/div[3]/div/div/div/form/fieldset/input")
    element.click()
    element.send_keys(name)
    element.send_keys(Keys.RETURN)
    
except:
    print("error")
try:
    enter=driver.find_elements(By.XPATH, "/html/body/div[2]/div[1]/div/div/div[3]/div/div/div/div[5]/ul/li/div/a/span[1]/em")
    enter.click()
    time.sleep(2)
except:
    print("error")
body = driver.find_element(By.TAG_NAME, "body")
temp=soup.find("strong", attrs={'class':"current"})
summ=soup.find("p", attrs={'class':"summary"})
temperature=temp.text
summary=summ.text
driver.quit()
#10r
