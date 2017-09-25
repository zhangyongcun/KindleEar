#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return zhihumeirjingxuan

class zhihumeirjingxuan(BaseFeedBook):
    title                 = u'知乎每日精选'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'知乎每日精选', 'http://www.zhihu.com/rss', True)
           ]