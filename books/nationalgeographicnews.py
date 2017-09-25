#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return nationalgeographicnews

class nationalgeographicnews(BaseFeedBook):
    title                 = u'National Geographic News'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'National Geographic News', 'http://feeds.nationalgeographic.com/ng/News/News_Main', True)
           ]