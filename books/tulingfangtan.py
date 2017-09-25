#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return tulingfangtan

class tulingfangtan(BaseFeedBook):
    title                 = u'图灵访谈'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'图灵访谈', 'http://feedmaker.kindle4rss.com/feeds/ituring_interview.weixin.xml', True)
           ]