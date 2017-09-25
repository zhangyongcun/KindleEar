#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return guokewangyixue

class guokewangyixue(BaseFeedBook):
    title                 = u'果壳网:医学'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'果壳网:医学', 'http://feedmaker.kindle4rss.com/feeds/subject-medicine.guokr.com.xml', True)
           ]