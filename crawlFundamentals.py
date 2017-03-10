# -*- coding: utf-8 -*-

import os
import re
import sys
import csv
import time
import string
import logging
import requests
import argparse
import progressbar
from lxml import html
from datetime import datetime, timedelta

from os import mkdir
from os.path import isdir
from grs import TWSENo

stock_list = TWSENo().all_stock_no
#bar = progressbar.ProgressBar(max_value=len(stock_list))
prefix = './data'
reload(sys)
sys.setdefaultencoding('utf-8')

def check_contain_chinese(check_str):
    for ch in check_str.decode('utf-8'):
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False

def clean_row(row):
    ''' Clean comma and spaces'''
    for index, content in enumerate(row):
        row[index] = re.sub(",", "", content.strip())
        row[index] = filter(lambda x: x in string.printable, row[index])
    return row

def save_data(_type, stkno, row):
    '''Save row to csv file'''
    if not isdir(prefix+'/'+_type):
        mkdir(prefix+'/'+_type)
    f = open('{}/{}.csv'.format(prefix+'/'+_type, stkno), 'ab')
    cw = csv.writer(f, lineterminator='\n')
    cw.writerow(row)
    f.close

def Crawl_mr():
    count = 0
    for stkno in stock_list:
        url = 'http://www.wantgoo.com/stock/report/basic_mr?StockNo=' + stkno

        time.sleep(0.01)
        page = requests.get(url, timeout=20)

        count += 1
        bar.update(count)

        tree = html.fromstring(page.text)
        for tr in tree.xpath('//*[@id=\"container\"]/div[7]/div[4]/table/tbody/tr'):
            tds = tr.xpath('td/text()')
            if len(tds) < 8:
                continue
            row = clean_row([
                tds[0], #年度/月份
                tds[1], #當月營收
                tds[2], #上月比較%
                tds[3], #去年同月營收
                tds[4], #去年同月增減%
                tds[5], #當月累計營收
                tds[6], #去年累計營收
                tds[7]  #前期比較%
            ])
            save_data('mr', stkno, row)

def Crawl_eps():
    count = 0
    for stkno in stock_list:
        url = 'http://www.wantgoo.com/stock/report/basic_eps?StockNo=' + stkno

        time.sleep(0.01)
        page = requests.get(url, timeout=20)

        count += 1
        bar.update(count)

        tree = html.fromstring(page.text)
        for tr in tree.xpath('//*[@id=\"mainCol\"]/div[3]/table/tbody/tr'):
            tds = tr.xpath('td/text()')
            if len(tds) < 5:
                continue
            row = clean_row([
                tds[0], #年度/季別
                tds[1], #每股盈餘
                tds[2], #季增率%
                tds[3], #年增率%
                tds[4]  #季收盤價
            ])
            save_data('eps', stkno, row)

def Crawl_bvps():
    count = 0
    for stkno in stock_list:
        url = 'http://www.wantgoo.com/stock/report/basic_bvps?StockNo=' + stkno
    
        time.sleep(0.01)
        page = requests.get(url, timeout=20)

        count += 1
        bar.update(count)

        tree = html.fromstring(page.text)
        for tr in tree.xpath('//*[@id=\"mainCol\"]/div[3]/table/tbody/tr'):
            tds = tr.xpath('td/text()')
            if len(tds) < 3:
                continue
            row = clean_row([
                tds[0], #年度/季別
                tds[1], #每股淨值
                tds[2]  #季收盤價
            ])
            save_data('bvps', stkno, row)

def Crawl_is():
    count = 0
    for stkno in stock_list:
        url = 'http://www.wantgoo.com/stock/report/basic_is?StockNo=' + stkno
    
        time.sleep(0.01)
        page = requests.get(url, timeout=20)

        count += 1
        bar.update(count)

        tree = html.fromstring(page.text)
        for tr in tree.xpath('//*[@id=\"mainCol\"]/div[3]/table/tbody/tr'):
            tds = tr.xpath('td/text()')
            if len(tds) < 6:
                continue
            row = clean_row([
                tds[0], #年度/季別
                tds[1], #營收
                tds[2], #毛利
                tds[3], #營業利益
                tds[4], #稅前淨利
                tds[5]  #稅後淨利
            ])
            save_data('is', stkno, row)

def Crawl_bs():
    count = 0
    for stkno in stock_list:
        url = 'http://www.wantgoo.com/stock/report/basic_bs?StockNo=' + stkno
    
        time.sleep(0.01)
        page = requests.get(url, timeout=20)

        count += 1
        bar.update(count)

        tree = html.fromstring(page.text)
        for tr in tree.xpath('//*[@id=\"mainCol\"]/div[3]/table/tbody/tr'):
            tds = tr.xpath('td/text()')
            if len(tds) < 6:
                continue
            row = clean_row([
                tds[0], #年度/季別
                tds[1], #流動資產
                tds[2], #長期投資
                tds[3], #固定資產
                tds[4], #其餘資產
                tds[5]  #總資產
            ])
            save_data('bs', stkno, row)

def Crawl_dse():
    count = 0
    for stkno in stock_list:
        url = 'http://www.wantgoo.com/stock/report/basic_dse?StockNo=' + stkno
    
        time.sleep(0.01)
        page = requests.get(url, timeout=20)

        count += 1
        bar.update(count)

        tree = html.fromstring(page.text)
        for tr in tree.xpath('//*[@id=\"mainCol\"]/div[3]/table/tbody/tr'):
            tds = tr.xpath('td/text()')
            if len(tds) < 7:
                continue
            row = clean_row([
                tds[0], #年度/季別
                tds[1], #流動負債
                tds[2], #長期負債
                tds[3], #其餘負債
                tds[4], #總負債
                tds[5], #淨值
                tds[6]  #總資產
            ])
            save_data('dse', stkno, row)

def Crawl_ese():
    count = 0
    for stkno in stock_list:
        url = 'http://www.wantgoo.com/stock/report/basic_ese?StockNo=' + stkno
    
        time.sleep(0.01)
        page = requests.get(url, timeout=20)

        count += 1
        bar.update(count)

        tree = html.fromstring(page.text)
        for tr in tree.xpath('//*[@id=\"mainCol\"]/div[3]/table/tbody/tr'):
            tds = tr.xpath('td/text()')
            if len(tds) < 4:
                continue
            row = clean_row([
                tds[0], #年度/季別
                tds[1], #股本
                tds[2], #淨值
                tds[3] #季收盤價
            ])
            save_data('ese', stkno, row)

def Crawl_cfs():
    count = 0
    for stkno in stock_list:
        url = 'http://www.wantgoo.com/stock/report/basic_cfs?StockNo=' + stkno
    
        time.sleep(0.01)
        page = requests.get(url, timeout=20)

        count += 1
        bar.update(count)

        tree = html.fromstring(page.text)
        for tr in tree.xpath('//*[@id=\"mainCol\"]/div[3]/table/tbody/tr'):
            tds = tr.xpath('td/text()')
            if len(tds) < 6:
                continue
            row = clean_row([
                tds[0], #年度/季別
                tds[1], #營業現金流
                tds[2], #投資現金流
                tds[3], #融資現金流
                tds[4], #自由現金流
                tds[5]  #淨現金流
            ])
            save_data('cfs', stkno, row)

def Crawl_dp():
    count = 0
    for stkno in stock_list:
        url = 'http://www.wantgoo.com/stock/report/basic_dp?StockNo=' + stkno
    
        time.sleep(0.01)
        page = requests.get(url, timeout=20)

        count += 1
        bar.update(count)

        tree = html.fromstring(page.text)
        for tr in tree.xpath('//*[@id=\"mainCol\"]/div[3]/table/tbody/tr'):
            tds = tr.xpath('td/text()')
            if check_contain_chinese(tds[0]):
                continue
            if len(tds) == 5:    
                row = clean_row([
                    tds[0], #年度
                    '', #除權息日
                    tds[1], #股票股利
                    tds[2], #現金股利
                    tds[3], #除權息前股價
                    tds[4], #現金殖利率%
                    ''  #扣抵稅率%
                ])
            elif len(tds) < 7:
                continue
            else:
                row = clean_row([
                    tds[0], #年度
                    tds[1], #除權息日
                    tds[2], #股票股利
                    tds[3], #現金股利
                    tds[4], #除權息前股價
                    tds[5], #現金殖利率%
                    tds[6]  #扣抵稅率%
                ])
            save_data('dp', stkno, row)

def Crawl_pr():
    count = 0
    for stkno in stock_list:
        url = 'http://www.wantgoo.com/stock/report/profit_pr?StockNo=' + stkno

        time.sleep(0.01)
        page = requests.get(url, timeout=20)

        count += 1
        bar.update(count)

        tree = html.fromstring(page.text)
        for tr in tree.xpath('//*[@id=\"mainCol\"]/div[3]/table/tbody/tr'):
            tds = tr.xpath('td/text()')
            if len(tds) < 6:
                continue
            row = clean_row([
                tds[0], #年度/季別
                tds[1], #毛利率%
                tds[2], #營業利益率%
                tds[3], #稅前淨利率%
                tds[4], #稅後淨利率%
                tds[5]  #季收盤價
            ])
            save_data('pr', stkno, row)

def Crawl_roe():
    count = 0
    for stkno in stock_list:
        url = 'http://www.wantgoo.com/stock/report/profit_roe?StockNo=' + stkno

        time.sleep(0.01)
        page = requests.get(url, timeout=20)

        count += 1
        bar.update(count)

        tree = html.fromstring(page.text)
        for tr in tree.xpath('//*[@id=\"mainCol\"]/div[3]/table/tbody/tr'):
            tds = tr.xpath('td/text()')
            if len(tds) < 4:
                continue
            row = clean_row([
                tds[0], #年度/季別
                tds[1], #ROE%
                tds[2], #ROA%
                tds[3]  #季收盤價
            ])
            save_data('roe', stkno, row)

def Crawl_da():
    count = 0
    for stkno in stock_list:
        url = 'http://www.wantgoo.com/stock/report/profit_da?StockNo=' + stkno

        time.sleep(0.01)
        page = requests.get(url, timeout=20)

        count += 1
        bar.update(count)

        tree = html.fromstring(page.text)
        for tr in tree.xpath('//*[@id=\"mainCol\"]/div[3]/table/tbody/tr'):
            tds = tr.xpath('td/text()')
            if len(tds) < 5:
                continue
            row = clean_row([
                tds[0], #年度/季別
                tds[1], #ROE%
                tds[2], #稅後淨利率%
                tds[3], #總資產週轉%
                tds[4]  #權益乘數
            ])
            save_data('da', stkno, row)

def Crawl_wct():
    count = 0
    for stkno in stock_list:
        url = 'http://www.wantgoo.com/stock/report/profit_wct?StockNo=' + stkno

        time.sleep(0.01)
        page = requests.get(url, timeout=20)

        count += 1
        bar.update(count)

        tree = html.fromstring(page.text)
        for tr in tree.xpath('//*[@id=\"mainCol\"]/div[3]/table/tbody/tr'):
            tds = tr.xpath('td/text()')
            if len(tds) < 4:
                continue
            row = clean_row([
                tds[0], #年度/季別
                tds[1], #應收帳款周轉(次)
                tds[2], #存貨週轉(次)
                tds[3]  #季收盤價 
            ])
            save_data('wct', stkno, row)

def Crawl_fat():
    count = 0
    for stkno in stock_list:
        url = 'http://www.wantgoo.com/stock/report/profit_fat?StockNo=' + stkno

        time.sleep(0.01)
        page = requests.get(url, timeout=20)

        count += 1
        bar.update(count)

        tree = html.fromstring(page.text)
        for tr in tree.xpath('//*[@id=\"mainCol\"]/div[3]/table/tbody/tr'):
            tds = tr.xpath('td/text()')
            if len(tds) < 4:
                continue
            row = clean_row([
                tds[0], #年度/季別
                tds[1], #固定資產週轉率(次)
                tds[2], #固定資產(仟元)
                tds[3]  #季收盤價 
            ])
            save_data('fat', stkno, row)

def Crawl_tat():
    count = 0
    for stkno in stock_list:
        url = 'http://www.wantgoo.com/stock/report/profit_tat?StockNo=' + stkno

        time.sleep(0.01)
        page = requests.get(url, timeout=20)

        count += 1
        bar.update(count)

        tree = html.fromstring(page.text)
        for tr in tree.xpath('//*[@id=\"mainCol\"]/div[3]/table/tbody/tr'):
            tds = tr.xpath('td/text()')
            if len(tds) < 4:
                continue
            row = clean_row([
                tds[0], #年度/季別
                tds[1], #總資產週轉率(次)
                tds[2], #總資產(仟元)
                tds[3]  #季收盤價 
            ])
            save_data('tat', stkno, row)

def Crawl_wctd():
    count = 0
    for stkno in stock_list:
        url = 'http://www.wantgoo.com/stock/report/profit_wctd?StockNo=' + stkno

        time.sleep(0.01)
        page = requests.get(url, timeout=20)

        count += 1
        bar.update(count)

        tree = html.fromstring(page.text)
        for tr in tree.xpath('//*[@id=\"mainCol\"]/div[3]/table/tbody/tr'):
            tds = tr.xpath('td/text()')
            if len(tds) < 5:
                continue
            row = clean_row([
                tds[0], #年度/季別
                tds[1], #應收帳款收現(天)
                tds[2], #存貨週轉(天)
                tds[3], #營運週轉(天)
                tds[4]  #季收盤價 
            ])
            save_data('wctd', stkno, row)

def Crawl_cfoin():
    count = 0
    for stkno in stock_list:
        url = 'http://www.wantgoo.com/stock/report/profit_cfoin?StockNo=' + stkno

        time.sleep(0.01)
        page = requests.get(url, timeout=20)

        count += 1
        bar.update(count)

        tree = html.fromstring(page.text)
        for tr in tree.xpath('//*[@id=\"mainCol\"]/div[3]/table/tbody/tr'):
            tds = tr.xpath('td/text()')
            if len(tds) < 3:
                continue
            row = clean_row([
                tds[0], #年度/季別
                tds[1], #營業現金流對淨值比%
                tds[2]  #季收盤價
            ])
            save_data('cfoin', stkno, row)

def Crawl_dpr():
    count = 0
    for stkno in stock_list:
        url = 'http://www.wantgoo.com/stock/report/profit_dpr?StockNo=' + stkno

        time.sleep(0.01)
        page = requests.get(url, timeout=20)

        count += 1
        bar.update(count)

        tree = html.fromstring(page.text)
        for tr in tree.xpath('//*[@id=\"mainCol\"]/div[3]/table/tbody/tr'):
            tds = tr.xpath('td/text()')
            if len(tds) < 3:
                continue
            row = clean_row([
                tds[0], #年度/季別
                tds[1], #現金股利發放率%
                tds[2]  #年收盤價
            ])
            save_data('dpr', stkno, row)

def Crawl_safe_1():
    count = 0
    for stkno in stock_list:
        url = 'http://www.wantgoo.com/stock/report/safe?types=1&StockNo=' + stkno

        time.sleep(0.01)
        page = requests.get(url, timeout=20)

        count += 1
        bar.update(count)

        tree = html.fromstring(page.text)
        for tr in tree.xpath('//*[@id=\"mainCol\"]/div[6]/table/tbody/tr'):
            tds = tr.xpath('td/text()')
            if len(tds) < 3:
                continue
            row = clean_row([
                tds[0], #年度/季別
                tds[1], #負債佔資產比%
                tds[2]  #季收盤價
            ])
            save_data('safe_1', stkno, row)

def Crawl_safe_2():
    count = 0
    for stkno in stock_list:
        url = 'http://www.wantgoo.com/stock/report/safe?types=2&StockNo=' + stkno

        time.sleep(0.01)
        page = requests.get(url, timeout=20)

        count += 1
        bar.update(count)

        tree = html.fromstring(page.text)
        for tr in tree.xpath('//*[@id=\"mainCol\"]/div[6]/table/tbody/tr'):
            tds = tr.xpath('td/text()')
            if len(tds) < 3:
                continue
            row = clean_row([
                tds[0], #年度/季別
                tds[1], #長期資金佔固定資產比%
                tds[2]  #季收盤價
            ])
            save_data('safe_2', stkno, row)

def Crawl_safe_3():
    count = 0
    for stkno in stock_list:
        url = 'http://www.wantgoo.com/stock/report/safe?types=3&StockNo=' + stkno

        time.sleep(0.01)
        page = requests.get(url, timeout=20)

        count += 1
        bar.update(count)

        tree = html.fromstring(page.text)
        for tr in tree.xpath('//*[@id=\"mainCol\"]/div[4]/table/tbody/tr'):
            tds = tr.xpath('td/text()')
            if len(tds) < 4:
                continue
            row = clean_row([
                tds[0], #年度/季別
                tds[1], #流動比%
                tds[2], #速動比%
                tds[3]  #季收盤價
            ])
            save_data('safe_3', stkno, row)

def Crawl_safe_4():
    count = 0
    for stkno in stock_list:
        url = 'http://www.wantgoo.com/stock/report/safe?types=4&StockNo=' + stkno

        time.sleep(0.01)
        page = requests.get(url, timeout=20)

        count += 1
        bar.update(count)

        tree = html.fromstring(page.text)
        for tr in tree.xpath('//*[@id=\"mainCol\"]/div[6]/table/tbody/tr'):
            tds = tr.xpath('td/text()')
            if len(tds) < 3:
                continue
            row = clean_row([
                tds[0], #年度/季別
                tds[1], #利息保障倍數%
                tds[2]  #季收盤價
            ])
            save_data('safe_4', stkno, row)

def Crawl_safe_5():
    count = 0
    for stkno in stock_list:
        url = 'http://www.wantgoo.com/stock/report/safe?types=5&StockNo=' + stkno

        time.sleep(0.01)
        page = requests.get(url, timeout=20)

        count += 1
        bar.update(count)

        tree = html.fromstring(page.text)
        for tr in tree.xpath('//*[@id=\"mainCol\"]/div[4]/table/tbody/tr'):
            tds = tr.xpath('td/text()')
            if len(tds) < 4:
                continue
            row = clean_row([
                tds[0], #年度/季別
                tds[1], #營業現金對流動負債比%
                tds[2], #營業現金對負債比%
                tds[3]  #季收盤價
            ])
            save_data('safe_5', stkno, row)

def Crawl_safe_6():
    count = 0
    for stkno in stock_list:
        url = 'http://www.wantgoo.com/stock/report/safe?types=6&StockNo=' + stkno

        time.sleep(0.01)
        page = requests.get(url, timeout=20)

        count += 1
        bar.update(count)

        tree = html.fromstring(page.text)
        for tr in tree.xpath('//*[@id=\"mainCol\"]/div[6]/table/tbody/tr'):
            tds = tr.xpath('td/text()')
            if len(tds) < 3:
                continue
            row = clean_row([
                tds[0], #年度/季別
                tds[1], #盈餘再投資比率%
                tds[2]  #季收盤價
            ])
            save_data('safe_6', stkno, row)

def Crawl_gp_season():
    count = 0
    for stkno in stock_list:
        url = 'http://www.wantgoo.com/stock/report/growth_gp?StockNo=' + stkno

        time.sleep(0.01)
        page = requests.get(url, timeout=20)

        count += 1
        bar.update(count)

        tree = html.fromstring(page.text)
        for tr in tree.xpath('//*[@id=\"mainCol\"]/div[3]/table/tbody/tr'):
            tds = tr.xpath('td/text()')
            if len(tds) < 4:
                continue
            row = clean_row([
                tds[0], #年度/季別
                tds[1], #毛利季增率%
                tds[2], #近4季毛利季增率%
                tds[3]  #季收盤價
            ])
            save_data('gp_season', stkno, row)

def Crawl_gp_year():
    count = 0
    for stkno in stock_list:
        url = 'http://www.wantgoo.com/stock/report/growth_gp?StockNo=' + stkno +'&isY=y'

        time.sleep(0.01)
        page = requests.get(url, timeout=20)

        count += 1
        bar.update(count)

        tree = html.fromstring(page.text)
        for tr in tree.xpath('//*[@id=\"mainCol\"]/div[3]/table/tbody/tr'):
            tds = tr.xpath('td/text()')
            if len(tds) < 4:
                continue
            row = clean_row([
                tds[0], #年度/季別
                tds[1], #毛利年增率%
                tds[2], #近4季毛利年增率%
                tds[3]  #季收盤價
            ])
            save_data('gp_year', stkno, row)

def Crawl_oigr_season():
    count = 0
    for stkno in stock_list:
        url = 'http://www.wantgoo.com/stock/report/growth_oigr?StockNo=' + stkno

        time.sleep(0.01)
        page = requests.get(url, timeout=20)

        count += 1
        bar.update(count)

        tree = html.fromstring(page.text)
        for tr in tree.xpath('//*[@id=\"mainCol\"]/div[3]/table/tbody/tr'):
            tds = tr.xpath('td/text()')
            if len(tds) < 4:
                continue
            row = clean_row([
                tds[0], #年度/季別
                tds[1], #營業利益季增率%
                tds[2], #近4季營業利益季增率%
                tds[3]  #季收盤價
            ])
            save_data('oigr_season', stkno, row)

def Crawl_oigr_year():
    count = 0
    for stkno in stock_list:
        url = 'http://www.wantgoo.com/stock/report/growth_oigr?StockNo=' + stkno +'&isY=y'

        time.sleep(0.01)
        page = requests.get(url, timeout=20)

        count += 1
        bar.update(count)

        tree = html.fromstring(page.text)
        for tr in tree.xpath('//*[@id=\"mainCol\"]/div[3]/table/tbody/tr'):
            tds = tr.xpath('td/text()')
            if len(tds) < 4:
                continue
            row = clean_row([
                tds[0], #年度/季別
                tds[1], #營業利益年增率%
                tds[2], #近4季營業利益年增率%
                tds[3]  #季收盤價
            ])
            save_data('oigr_year', stkno, row)

def Crawl_nigr_season():
    count = 0
    for stkno in stock_list:
        url = 'http://www.wantgoo.com/stock/report/growth_nigr?StockNo=' + stkno

        time.sleep(0.01)
        page = requests.get(url, timeout=20)

        count += 1
        bar.update(count)

        tree = html.fromstring(page.text)
        for tr in tree.xpath('//*[@id=\"mainCol\"]/div[3]/table/tbody/tr'):
            tds = tr.xpath('td/text()')
            if len(tds) < 4:
                continue
            row = clean_row([
                tds[0], #年度/季別
                tds[1], #稅後淨利季增率%
                tds[2], #近4季稅後淨利季增率%
                tds[3]  #季收盤價
            ])
            save_data('nigr_season', stkno, row)

def Crawl_nigr_year():
    count = 0
    for stkno in stock_list:
        url = 'http://www.wantgoo.com/stock/report/growth_nigr?StockNo=' + stkno +'&isY=y'

        time.sleep(0.01)
        page = requests.get(url, timeout=20)

        count += 1
        bar.update(count)

        tree = html.fromstring(page.text)
        for tr in tree.xpath('//*[@id=\"mainCol\"]/div[3]/table/tbody/tr'):
            tds = tr.xpath('td/text()')
            if len(tds) < 4:
                continue
            row = clean_row([
                tds[0], #年度/季別
                tds[1], #稅後淨利年增率%
                tds[2], #近4季稅後淨利年增率%
                tds[3]  #季收盤價
            ])
            save_data('nigr_year', stkno, row)

def Crawl_value_1():
    count = 0
    for stkno in stock_list:
        url = 'http://www.wantgoo.com/stock/report/value?types=1&StockNo=' + stkno

        time.sleep(0.01)
        page = requests.get(url, timeout=20)

        count += 1
        bar.update(count)

        tree = html.fromstring(page.text)
        for tr in tree.xpath('//*[@id=\"mainCol\"]/div[5]/table/tbody/tr'):
            tds = tr.xpath('td/text()')
            if len(tds) < 3:
                continue
            row = clean_row([
                tds[0], #年度/月份
                tds[1], #本益比(倍)
                tds[2]  #月收盤價
            ])
            save_data('value_1', stkno, row)

def Crawl_value_2():
    count = 0
    for stkno in stock_list:
        url = 'http://www.wantgoo.com/stock/report/value?types=2&StockNo=' + stkno

        time.sleep(0.01)
        page = requests.get(url, timeout=20)

        count += 1
        bar.update(count)

        tree = html.fromstring(page.text)
        for tr in tree.xpath('//*[@id=\"mainCol\"]/div[5]/table/tbody/tr'):
            tds = tr.xpath('td/text()')
            if len(tds) < 3:
                continue
            row = clean_row([
                tds[0], #年度/月份
                tds[1], #股價淨值比(倍)
                tds[2]  #月收盤價
            ])
            save_data('value_2', stkno, row)

def Crawl_value_3():
    count = 0
    for stkno in stock_list:
        url = 'http://www.wantgoo.com/stock/report/value?types=3&StockNo=' + stkno

        time.sleep(0.01)
        page = requests.get(url, timeout=20)

        count += 1
        bar.update(count)

        tree = html.fromstring(page.text)
        for tr in tree.xpath('//*[@id=\"mainCol\"]/div[5]/table/tbody/tr'):
            tds = tr.xpath('td/text()')
            if len(tds) < 3:
                continue
            row = clean_row([
                tds[0], #年度/月份
                tds[1], #現金殖利率%
                tds[2]  #月收盤價
            ])
            save_data('value_3', stkno, row)



def main():
    print 'Crawl mr'    #基本財報->每月營收
    Crawl_mr()
    print 'Crawl eps'   #基本財報->每股盈餘
    Crawl_eps()
    print 'Crawl bvps'  #基本財報->每股淨值
    Crawl_bvps()
    print 'Crawl is'    #基本財報->損益表
    Crawl_is()
    print 'Crawl bs'    #基本財報->資產表
    Crawl_bs()
    print 'Crawl dse'   #基本財報->股東權益(負債)
    Crawl_dse()
    print 'Crawl ese'   #基本財報->股東權益(股本)
    Crawl_ese()
    print 'Crawl cfs'   #基本財報->現金流量表
    Crawl_cfs()

    print 'Crawl dp'    #股利政策
    Crawl_dp()

    print 'Crawl pr'    #獲利能力->利潤比率
    Crawl_pr()
    print 'Crawl roe'   #獲利能力->報酬率
    Crawl_roe()
    print 'Crawl da'    #獲利能力->杜邦分析
    Crawl_da()
    print 'Crawl wct'   #獲利能力->營運週轉能力
    Crawl_wct()
    print 'Crawl fat'   #獲利能力->固定資產週轉
    Crawl_fat()
    print 'Crawl tat'   #獲利能力->總資產週轉
    Crawl_tat()
    print 'Crawl wctd'  #獲利能力->營運週轉天數
    Crawl_wctd()
    print 'Crawl cfoin' #獲利能力->營業現金流對淨值比
    Crawl_cfoin()
    print 'Crawl dpr'   #獲利能力->現金股利發放率
    Crawl_dpr()
   
    print 'Crawl safe_1' #財務安全->負債占資產比
    Crawl_safe_1()
    print 'Crawl safe_2' #財務安全->長期資金佔固定資產比
    Crawl_safe_2()
    print 'Crawl safe_3' #財務安全->流速動比率
    Crawl_safe_3()
    print 'Crawl safe_4' #財務安全->利息保障倍數
    Crawl_safe_4()
    print 'Crawl safe_5' #財務安全->現金流量分析
    Crawl_safe_5()
    print 'Crawl safe_6' #財務安全->盈餘再投資比率
    Crawl_safe_6()

    print 'Crawl gp (season)'   #公司成長->毛利成長率(季)
    Crawl_gp_season()
    print 'Crawl gp (year)'     #公司成長->毛利成長率(年)
    Crawl_gp_year()
    print 'Crawl oigr (season)' #公司成長->營業利益成長率(季)
    Crawl_oigr_season()
    print 'Crawl oigr (year)'   #公司成長->營業利益成長率(年)
    Crawl_oigr_year()
    print 'Crawl nigr (season)' #公司成長->稅後淨利成長率(季)
    Crawl_nigr_season()
    print 'Crawl nigr (year)'   #公司成長->稅後淨利成長率(年)
    Crawl_nigr_year()
    
    print 'Crawl value_1' #企業價值->本益比
    Crawl_value_1()
    print 'Crawl value_2' #企業價值->股價淨值比
    Crawl_value_2()
    print 'Crawl value_3' #企業價值->現金殖利率
    Crawl_value_3()

def testOneEPS(stkno):
    url = 'http://www.wantgoo.com/stock/report/basic_eps?StockNo=' + stkno
    time.sleep(0.01)
    page = requests.get(url, timeout=20)
    tree = html.fromstring(page.text)
    for tr in tree.xpath('//*[@id=\"mainCol\"]/div[3]/table/tbody/tr'):
        tds = tr.xpath('td/text()')
        if len(tds) < 5:
          continue
        row = clean_row([
            tds[0], #年度/季別
            tds[1], #每股盈餘
            tds[2], #季增率%
            tds[3], #年增率%
            tds[4]  #季收盤價
        ])
        save_data('eps', stkno, row)

if __name__ == '__main__':
    #main()
    testOneEPS('1215')

