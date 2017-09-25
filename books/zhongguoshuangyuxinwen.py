#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return zhongguoshuangyuxinwen

class zhongguoshuangyuxinwen(BaseFeedBook):
    title                 = u'中国日报: 双语新闻'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'中国日报: 双语新闻', 'http://feedmaker.kindle4rss.com/feeds/language-news.chinadaily.xml', True)
           ]