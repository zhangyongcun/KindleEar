#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return xiaozhongruanjian

class xiaozhongruanjian(BaseFeedBook):
    title                 = u'小众软件'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'小众软件', 'http://feeds.appinn.com/appinns/', True)
           ]