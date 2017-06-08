# -*- coding: utf-8 -*-
from scrapy import cmdline
from datetime import datetime

starttime = str(datetime.now().strftime("%Y-%m-%d-%H-%M-%S"))

log_file = '../log/scrapy-test-'+starttime+".log"

command = "scrapy list -s LOG_FILE=" + log_file

cmdline.execute(command.split(' '))

