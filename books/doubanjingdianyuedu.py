#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return doubanjingdianyuedu

class doubanjingdianyuedu(BaseFeedBook):
    title                 = u'豆瓣: 经典短篇阅读'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'豆瓣: 经典短篇阅读', 'http://www.douban.com/feed/group/classicreading/discussion', True)
           ]