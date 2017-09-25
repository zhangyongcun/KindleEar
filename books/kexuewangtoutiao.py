#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return kexuewangtoutiao

class kexuewangtoutiao(BaseFeedBook):
    title                 = u'科学网头条'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'科学网头条', 'http://www.sciencenet.cn/xml/news-0.aspx?news=0', True)
           ]