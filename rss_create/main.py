# coding=utf-8
from xlrd import open_workbook


def get_excle_data(name):
    values = []
    wb = open_workbook(name)
    for s in wb.sheets():
        for row in range(1, s.nrows):
            col_names = s.row(0)
            col_value = []
            for name, col in zip(col_names, range(s.ncols)):
                value  = (s.cell(row,col).value)
                try : value = str(int(value))
                except : pass
                col_value.append(value)
            values.append(col_value)
    return values


def create_py(data):
    rss_name = data[2]
    rss_title = (data[1]).replace('\n','')
    rss_address = (data[4]).replace('\n','')
    f = open('rss/' + rss_name + '.py', 'w', encoding='utf-8')
    f.write('#!/usr/bin/env python\n')
    f.write('# -*- coding:utf-8 -*-\n')
    f.write('from base import BaseFeedBook\n\n')
    f.write('def getBook():\n')
    f.write('    return ' + rss_name + '\n\n')
    f.write('class ' + rss_name +'(BaseFeedBook):\n')
    f.write("    title                 = u'" + rss_title +"'\n")
    f.write("    description           = u'   '\n")
    f.write("    language              = 'zh-cn'\n")
    f.write("    feed_encoding         = 'utf-8'\n    page_encoding         = 'utf-8'\n    oldest_article        = 1\n")
    f.write("    feeds = [")
    f.write("            (u'" + rss_title + "', '"+ rss_address +"', True)\n")
    f.write("           ]")
    f.close()


excle_data = get_excle_data('rsscn.xlsx')


for data in excle_data:
    create_py(data)




