#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return pengpai

class pengpai(BaseFeedBook):
    title                 = u'澎湃'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'澎湃', 'http://feedmaker.kindle4rss.com/feeds/choice.thepaper.xml', True)
           ]