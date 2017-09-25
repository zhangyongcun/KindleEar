#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return kaiyuanzhongwenshequ

class kaiyuanzhongwenshequ(BaseFeedBook):
    title                 = u'Linux.中国 - 开源中文社区'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'Linux.中国 - 开源中文社区', 'https://linux.cn/rss.xml', True)
           ]