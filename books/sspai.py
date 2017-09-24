#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return sspai

class ZhihuDaily(BaseFeedBook):
    title                 = u'少数派'
    description           = u'少数派 数码'
    language              = 'zh-cn'
    feed_encoding         = "utf-8"
    page_encoding         = "utf-8"
    oldest_article        = 1
    feeds = [
            (u'少数派', 'https://sspai.com/feed', True)
           ]
