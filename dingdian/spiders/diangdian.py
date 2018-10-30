#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Author:Leslie-x 
import re, time
import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request
from dingdian.items import DingdianItem


class Myspider(scrapy.Spider):
    name = 'dingdian'
    allowed_domains = ['x23us.com']
    bash_url = 'http://www.x23us.com/class/'
    bashurl = '.html'

    def start_requests(self):
        for i in range(1, 11):
            url = self.bash_url + str(i) + '_1' + self.bashurl
            # url = http://www.x23us.com/class/5_1.html
            yield Request(url, self.parse)

    def parse(self, response):
        # 请求分类页面：http://www.x23us.com/class/5_1.html，得到分类中的所有小说的目录
        # print(response.text)
        max_num = BeautifulSoup(response.text, 'lxml').find('div', class_='pagelink').find_all('a')[-1].get_text()
        bookurl = str(response.url[:-7])
        for number in range(1, int(max_num) + 1):
            url = bookurl + '_' + str(number) + self.bashurl
            yield Request(url, callback=self.get_name)

    def get_name(self, response):
        tds = BeautifulSoup(response.text, 'lxml').find_all('tr', bgcolor='#FFFFFF')
        for td in tds:
            novelname = td.find_all('a')[1].text
            novleurl = td.find_all('a')[1]['href']
            yield Request(novleurl, callback=self.get_chapturl, meta={'name': novelname, 'url': novleurl})

    def get_chapturl(self, response):
        item = DingdianItem()
        item['name'] = str(response.meta['name']).replace('\xa0', '')
        item['novelurl'] = response.meta['url']
        category = BeautifulSoup(response.text, 'lxml').find('dt').find_all('a')[5].get_text()
        author_info = BeautifulSoup(response.text, 'lxml').find('h3').get_text()
        name_id = ''.join(response.meta['url'].split('/')[-3:-1])
        item['category'] = category
        item['author'] = re.split(r'[：\xa0;]', author_info)[1]
        item['name_id'] = name_id
        return item
