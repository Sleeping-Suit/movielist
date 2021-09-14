import requests
from bs4 import BeautifulSoup

def getTemp():
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%ED%98%84%EC%9E%AC%EC%98%A8%EB%8F%84"
    
    response = requests.get(url)

    naver_html = response.text

    soup = BeautifulSoup(naver_html, 'html.parser')
    temp = soup.select_one('.todaytemp')

    return temp.text