#!/usr/bin/python
# -*- encoding=utf-8 -*- 

from bs4 import BeautifulSoup
import requests
import json
import string
class DouBanSpider(object):
    """docstring for DouBanSpider"""
    def __init__(self):
        self.page = 1
        self.curl = "http://movie.douban.com/top250?start={page}&filter=&type="
        self.datas = []
        self._top_num = 1
    def get_page(self,cur_page):
        url = self.curl
        try:
            my_page = requests.get(url.format(page = (cur_page - 1) * 25)).text
        except Exception as e:
            print(e)
        return my_page
    def find_title(self, my_page):
        temp_data = []
        soup = BeautifulSoup(my_page, 'html.parser')
        divs = soup.find_all('div', attrs={'class': 'hd'})
        for div in divs:
            spans = div.find_all('span', attrs = {'class': 'title'})
            temp_text = ''
            for span in spans:
                temp_text += span.text 
            temp_data.append("Top" + str(self._top_num) + " " + temp_text)
            self._top_num += 1
            self.datas.extend(temp_data)    
    def start_spider(self) :
        while self.page <= 4 :
            my_page = self.get_page(self.page)
            self.find_title(my_page)
            self.page += 1
def main() :
    my_spider = DouBanSpider()
    my_spider.start_spider()
    for item in my_spider.datas :
        print(item)
    print("豆瓣爬虫爬取结束...")
if __name__ == '__main__':
    main()