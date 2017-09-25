#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return dailyintelligencer

class dailyintelligencer(BaseFeedBook):
    title                 = u'Daily Intelligencer'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'Daily Intelligencer', 'http://feeds.feedburner.com/nymag/intelligencer', True)
           ]