# -*- coding: utf-8 -*-
from scrapy import cmdline
from datetime import datetime

starttime = str(datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))

log_file = '../log/scrapy-articlehour-'+starttime+".log"

command = "scrapy crawl byrbbs_article_hour -s LOG_FILE=" + log_file

cmdline.execute(command.split(' '))


