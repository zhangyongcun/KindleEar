#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return zhonguorbaocaijing

class zhonguorbaocaijing(BaseFeedBook):
    title                 = u'中国日报: 财经'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'中国日报: 财经', 'http://feedmaker.kindle4rss.com/feeds/caijing.chinadaily.xml', True)
           ]