#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return thenewyorker

class thenewyorker(BaseFeedBook):
    title                 = u'The New Yorker'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'The New Yorker', 'http://www.newyorker.com/services/rss/feeds/everything.xml', True)
           ]