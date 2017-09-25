#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return ftmeirgengxin

class ftmeirgengxin(BaseFeedBook):
    title                 = u'FT中文网:每日更新'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'FT中文网:每日更新', 'http://feedmaker.kindle4rss.com/feeds/feed.ftchinese.com.xml', True)
           ]