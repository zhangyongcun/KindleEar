#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return jikegongyuan

class jikegongyuan(BaseFeedBook):
    title                 = u'极客公园-GeekPark'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'极客公园-GeekPark', 'http://www.geekpark.net/rss', True)
           ]