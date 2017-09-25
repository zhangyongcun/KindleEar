#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return ftshenghuoshishang

class ftshenghuoshishang(BaseFeedBook):
    title                 = u'FT中文网:生活时尚'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'FT中文网:生活时尚', 'http://feedmaker.kindle4rss.com/feeds/lifestyle.ftchinese.com.xml', True)
           ]