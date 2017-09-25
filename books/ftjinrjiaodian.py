#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return ftjinrjiaodian

class ftjinrjiaodian(BaseFeedBook):
    title                 = u'FT中文网:今日焦点'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'FT中文网:今日焦点', 'http://feedmaker.kindle4rss.com/feeds/news.ftchinese.com.xml', True)
           ]