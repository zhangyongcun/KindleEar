#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return ftmeiryingwen

class ftmeiryingwen(BaseFeedBook):
    title                 = u'FT中文网:每日英语'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'FT中文网:每日英语', 'http://feedmaker.kindle4rss.com/feeds/diglossia.ftchinese.com.xml', True)
           ]