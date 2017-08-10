#!/usr/bin/python
# -*- coding: UTF-8 -*-

from bs4 import BeautifulSoup
import requests
import codecs

def get_page(url):
    date = requests.get(url).content
    return date
def get_text(html):
    soup = BeautifulSoup(html, 'html.parser')
    article = soup.find('div', attrs = {'class': 'article'})
    title = article.find('h1', attrs = {'class': 'title'}).get_text()
    text = []
    for paragraph in article.find_all('p'):
        p_content = paragraph.get_text()
        text.append(p_content)
    return title, text
def save_text(title, text):
    file_name = title + '.txt'
    with codecs.open(file_name, 'wb', encoding = 'utf-8') as fp:
        try:
            for p in text:
                fp.write('\t%s\t\r\n'%p)
        except Exception as e:
            print('error')
        print('文章读取完成')
        return

if __name__ == '__main__':
    url = 'http://www.jianshu.com/p/96fbc2afca13'
    html = get_page(url)
    title, text = get_text(html)
    save_text(title, text)