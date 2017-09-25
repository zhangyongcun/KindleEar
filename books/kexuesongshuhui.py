#!/usr/bin/env python
# -*- coding:utf-8 -*-
from base import BaseFeedBook

def getBook():
    return kexuesongshuhui

class kexuesongshuhui(BaseFeedBook):
    title                 = u'科学松鼠会'
    description           = u'   '
    language              = 'zh-cn'
    feed_encoding         = 'utf-8'
    page_encoding         = 'utf-8'
    oldest_article        = 1
    feeds = [            (u'科学松鼠会', 'http://songshuhui.net/feed', True)
           ]