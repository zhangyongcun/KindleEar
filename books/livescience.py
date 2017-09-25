#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return livescience

class livescience(BaseFeedBook):
    title                 = u'LiveScience.com'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'LiveScience.com', 'http://www.livescience.com//home/feed/site.xml', True)
           ]