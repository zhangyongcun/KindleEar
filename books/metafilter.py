#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return metafilter

class metafilter(BaseFeedBook):
    title                 = u'MetaFilter'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'MetaFilter', 'http://feeds.feedburner.com/Metafilter', True)
           ]