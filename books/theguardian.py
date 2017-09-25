#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return theguardian

class theguardian(BaseFeedBook):
    title                 = u'The Guardian'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'The Guardian', 'http://feeds.guardian.co.uk/theguardian/us-home/rss', True)
           ]