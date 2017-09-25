#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return niuyueshibaoguojishenghuo

class niuyueshibaoguojishenghuo(BaseFeedBook):
    title                 = u'纽约时报: 国际生活'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'纽约时报: 国际生活', 'http://feedmaker.kindle4rss.com/feeds/style.cn-nytimes.xml', True)
           ]