# byrbbs-py3
爬取北邮人论坛所有帖子与板块信息（python3）

## 基本介绍：

- 与https://github.com/ryderchan/byrbbs 功能相似；
- byrbbs中使用的是python2编写，byrbbs-py3使用的是python3；
- 实现上都是基于scrapy，但Mysqldb不支持python3,更换为pymysql；

## 所需环境与工具

- anaconda3(不仅包含python编译器，还有安装scrapy所需的一些基础库)
- scrapy（爬虫框架）
- pymysql（连接mysql数据库）


## 功能：
- 模块1.byrbbs_section:爬取byr.bbs.cn的板块基本信息
- 模块2.byrbbs_article:爬取各个板块的帖子的基本信息
- 模块3.byrbbs_article_hour:快速更新模块，获取今日新帖
- 前两个的功能与byrbbs一致，只是删掉了爬取帖子正文的功能，正文太占空间了，我的小服务器吃不消，跑几次就没空间了，暂时删掉，后面可能会加上。
第三个的快速更新，每次只获取每个版块的第一页信息，一次完整的执行能在10分钟结束。可以改成只获取当天的信息，测试能在2分钟内完成爬取。通过对这个模块的半个小时或一个小时的间隔执行，可完成对帖子数据的更新。

