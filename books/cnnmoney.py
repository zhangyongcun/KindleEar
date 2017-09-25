#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return cnnmoney

class cnnmoney(BaseFeedBook):
    title                 = u'CNN Money'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'CNN Money', 'http://rss.cnn.com/rss/money_topstories.rss', True)
           ]