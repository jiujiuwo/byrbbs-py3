# -*- coding: utf-8 -*-

import os

# os.system('scrapy crawl byr_section')
# os.system('scrapy crawl byr_article -o article_list.xml')
# os.system('scrapy crawl byrbbs_section')


from scrapy import cmdline


# cmdline.execute("scrapy crawl byrbbs_section".split(' '))


cmdline.execute("scrapy crawl byrbbs_article".split(' '))

