import schedule
import time

from bs4 import BeautifulSoup
from selenium import webdriver


# 네이버 실시간 검색어를 확인 가능한 signal.bz 홈페이지 url 및 chromedriver 파일경로 
url = 'https://www.signal.bz/'
path = "/home/song/talpiot/chromedriver"

# (unknown error: DevToolsActivePort file doesn't exist) 오류 발생으로 인한 해결방안 코드 
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--single-process")
chrome_options.add_argument("--disable-dev-shm-usage", )

# 반복문을 통하여 하나하나 출력 
def RankListPrint():
    driver = webdriver.Chrome(path, chrome_options=chrome_options)
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    rank_list = soup.select('span.rank-text')

    index = 0
    for rank in rank_list:
        index += 1
        print(str(index) + ". " + rank.text)
        if index >= 10:
            break

# 매일 아침 9시마다 RankListPrint를 실행하여 결과룰 출력한다.
schedule.every().day.at("09:00").do(RankListPrint)

while 1:
    schedule.run_pending()
    time.sleep(1)
