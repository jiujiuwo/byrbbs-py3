# -*- coding: utf-8 -*-
import scrapy
from byrbbs.spiders.byrbbs_config import URL_HEAD, HEADERS, LOGIN_FORMDATA, DB_CONFIG
from byrbbs.items import ByrbbsArticleItem
import re
import pymysql
from datetime import datetime


class ByrbbsArticleHourSpider(scrapy.Spider):
    pipeline = ['ByrbbsArticleHourPipeline']
    name = "byrbbs_article_hour"
    allowed_domains = ["bbs.byr.cn"]
    start_urls = ["https://bbs.byr.cn"]
    article_per_list = 30

    def start_requests(self):
        return [scrapy.FormRequest("https://bbs.byr.cn/user/ajax_login.json",
                                   formdata=LOGIN_FORMDATA,
                                   meta={'cookiejar': 1},
                                   headers=HEADERS,
                                   callback=self.logged_in)]

    # 不翻页(hour版不进行翻页，只处理第一页，因为更新速度够短，默认设为半小时)
    def logged_in(self, response):
        conn = pymysql.connect(**DB_CONFIG)
        cursor = conn.cursor()
        sql = 'select * from section'
        cursor.execute(sql)
        for row in cursor.fetchall():
            item = ByrbbsArticleItem()
            item['section_url'] = row[1]
            yield scrapy.Request(response.urljoin(row[1]), meta={'cookiejar': response.meta['cookiejar'], 'item': item}, headers=HEADERS,
                                 callback=self.parse_article_list)

    # 用于测试指定版块或文章
    #     self.start_urls = ['https://bbs.byr.cn/board/BM_Market']
    #     item = ByrbbsArticleItem()
    #     item['section_url'] = 'board/BM_Market'
    #     return scrapy.Request(self.start_urls[0], meta={'cookiejar': response.meta['cookiejar'], 'item': item},
    #                           headers=HEADERS, callback=self.parse_article_list)

    # 处理列表，获取列表上的每条文章信息与文章链接
    def parse_article_list(self, response):
        # print "parse_article_list "+response._get_url()
        section_url = response.meta['item']['section_url']
        sel_article = response.xpath('//*[@class="b-content"]/table/tbody/tr')
        article_url = sel_article.xpath('td[2]/a/@href').extract()
        article_title = sel_article.xpath('td[2]/a/text()').extract()
        article_createtime = sel_article.xpath('td[3]/text()').extract()
        article_author = sel_article.xpath('td[4]/a/text()').extract()
        article_comment = sel_article.xpath('td[5]/text()').extract()

        # 处理列表的每一行，即每一篇文章的信息，存入item
        for index, url in enumerate(article_url):
            item = ByrbbsArticleItem()
            item['section_url'] = section_url
            item['article_title'] = article_title[index]
            item['article_url'] = response.urljoin(article_url[index])
            item['article_author'] = article_author[index]
            item['article_comment'] = article_comment[index]
            item['updatetime'] = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

            temp = str(article_createtime[index]).strip()
            # 有-为年月日（时分秒被省略了）；有:为时分秒（年月日被省略了，为今天）
            if temp.find("-") == -1 and temp.find(":") != -1:
                item['article_createtime'] = datetime.now().strftime("%Y-%m-%d") + " " + temp
                # yield item
            elif temp.find("-") != -1 and temp.find(":") == -1:
                item['article_createtime'] = temp.strip() + " 00:00:00"
            elif temp.find("-") == -1 and temp.find(":") == -1:
                item['article_createtime'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            else:
                item['article_createtime'] = temp
            yield item

