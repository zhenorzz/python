#!/usr/bin/python
from bs4 import BeautifulSoup
import requests

page = 1
url = 'http://www.cilizhuzhu.org/remen/'
try:
    html = requests.get(url).content
    soup = BeautifulSoup(html, 'html.parser')
    div = soup.find_all('div', attrs = {'class': 'photo-frame'})
    num = 1
    for img in div:
        src = img.find('img').attrs['src']
        try:
            image = requests.get('http://www.cilizhuzhu.org'+src, stream=True).content
            with open('%s.jpg'%num,'wb') as fp:
                fp.write(image)
                num += 1
                print('正在下载第%s张图片'%num)
        except Exception as e:
            print(e)
except Exception as e:
    print(e)
        