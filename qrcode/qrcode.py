#!/usr/bin/python
from bs4 import BeautifulSoup
import requests
import json

session = requests.Session()
url = 'http://url.cn/4B7NaqH'
getcode = 'http://cz.uclbrt.com/Wap/Room/getQrcode'
try:
    html = session.post(url).content
    soup = BeautifulSoup(html, 'html.parser')
    roomList = soup.find('a', attrs = {'class': 'roomList'})
    info = roomList.attrs['data-value']
except Exception as e:
    print(e)
try:
    data = {'info':info}
    html = session.post(getcode,data)
    print(json.loads(html.text)['data']['cardStr'])
except Exception as e:
    print(e)