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
options.add_argument("--start-maximized")
service = Service(cd_path)
driver = webdriver.Chrome(service=service, options=options)

# 유튜브 검색 페이지로 이동
base_url = "https://www.youtube.com/results?search_query="
name=input("검색하고 싶은 채널 이름(띄어 쓰기 제외)").strip()
query_params={"query": f"{name}"}
query_string=parse.urlencode(query_params)
url=f"{base_url}{name}"
driver.get(url)
driver.implicitly_wait(5)
time.sleep(3)

# 채널 클릭
try:
    channel_element = driver.find_element(By.CSS_SELECTOR, "ytd-channel-renderer a#main-link")
    channel_element.click()
except:
    print("채널을 찾을 수 없습니다.")
    driver.quit()

# 동영상 탭 클릭
try:
    videos_tab = driver.find_element(By.XPATH, '//*[@id="tabsContent"]/yt-tab-group-shape/div[1]/yt-tab-shape[2]')
    videos_tab.click()
except:
    print("동영상 탭을 찾을 수 없습니다.")
    driver.quit()

# 스크롤 다운
body = driver.find_element(By.TAG_NAME, "body")
for _ in range(30):
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.1)

# '모두 보기' 버튼 클릭 (존재할 경우)
try:
    view_all_button = driver.find_element(By.XPATH, "//*[@id='view-all']/a")
    view_all_button.click()
except:
    pass  # 버튼이 없으면 그냥 계속 진행



# HTML 가져와서 BeautifulSoup으로 파싱
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
#print(soup)
# 제목과 조회수 가져오기
titles = soup.select("a#video-title-link")
views=soup.select("span.inline-metadata-item")
for i, title in enumerate(titles):
    print(title.text, views[i*2].text if i*2 < len(views) else "조회수 없음")
# 드라이버 종료
#driver.quit()
