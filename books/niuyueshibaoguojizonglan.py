#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return niuyueshibaoguojizonglan

class niuyueshibaoguojizonglan(BaseFeedBook):
    title                 = u'纽约时报: 国际纵览'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'纽约时报: 国际纵览', 'http://feedmaker.kindle4rss.com/feeds/main.cn-nytimes.xml', True)
           ]