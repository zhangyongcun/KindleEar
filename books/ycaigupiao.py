#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return ycaigupiao

class ycaigupiao(BaseFeedBook):
    title                 = u'一财:股票'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'一财:股票', 'http://feedmaker.kindle4rss.com/feeds/markets.yicai.com.xml', True)
           ]