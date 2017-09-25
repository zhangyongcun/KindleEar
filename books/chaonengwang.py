#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return chaonengwang

class chaonengwang(BaseFeedBook):
    title                 = u'超能网'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'超能网', 'http://www.expreview.com/rss.php', True)
           ]