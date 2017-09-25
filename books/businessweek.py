#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return businessweek

class businessweek(BaseFeedBook):
    title                 = u'Businessweek'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'Businessweek', 'http://www.businessweek.com/feeds/homepage.rss', True)
           ]