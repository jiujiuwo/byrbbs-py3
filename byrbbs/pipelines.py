# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from byrbbs.spiders.byrbbs_config import DB_CONFIG
import pymysql
import functools

def check_pipline(func):
    @functools.wraps(func)
    def wrapper(self, item, spider):
        if self.__class__.__name__ in spider.pipeline:
            return func(self, item, spider)
        else:
            return item
    return wrapper


class ByrbbsSectionPipeline(object):
    @check_pipline
    def process_item(self, item, spider):
        # 用spider.name区分不同的spider
        # https://segmentfault.com/q/1010000004863755
        con = pymysql.connect(**DB_CONFIG)
        cur = con.cursor()
        sql = 'insert into section(section_url,section_name,section_article_total,top_section_num,top_section_name,updatetime) ' \
              'values(%s,%s,%s,%s,%s,%s)'
        values = (item['section_url'], item['section_name'], item['section_article_total'],
                  item['top_section_num'], item['top_section_name'], item['updatetime'])
        cur.execute(sql, values)  # second parameter must be iterabale
        con.commit()
        cur.close()
        con.close()
        return item

class ByrbbsArticlePipeline(object):
    @check_pipline
    def process_item(self, item, spider):
        con = pymysql.connect(**DB_CONFIG)
        cur = con.cursor()
        sql = 'insert into articleinfo(section_url,article_title,' \
              'article_url,article_comment,article_author,article_createtime,updatetime) ' \
              'values(%s,%s,%s,%s,%s,%s,%s)'
        values = (item['section_url'], item['article_title'], item['article_url'], item['article_comment'],
                  item['article_author'], item['article_createtime'], item['updatetime'])
        cur.execute(sql, values)  # second parameter must be iterabale
        # sql2 = 'insert into articlebody(article_url,article_content) values(%s,%s)'
        # values2 = (item['article_url'], item['article_content'])
        # cur.execute(sql2, values2)
        con.commit()
        cur.close()
        con.close()
        return item

