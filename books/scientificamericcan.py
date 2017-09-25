#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return scientificamericcan

class scientificamericcan(BaseFeedBook):
    title                 = u'Scientific American Podcast: 60-Second Science'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'Scientific American Podcast: 60-Second Science', 'http://feedmaker.kindle4rss.com/feeds/60secsciencepodcast.sciam.xml', True)
           ]