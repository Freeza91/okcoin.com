#!/usr/bin/python
# -*- coding: utf-8 -*-
# encoding: utf-8

import sys
import json
import time
import logging
from OkcoinFutureAPI import OKCoinFuture
from plan_pingcang import plan
from helpers import get_btc_price

from conf import okcoin

apikey = okcoin.apikey
secretkey = okcoin.secretkey
okcoinRESTURL = okcoin.okcoinRESTURL

okcoinFuture = OKCoinFuture(okcoinRESTURL,apikey,secretkey)

category = ''
price = 0
trend = ''
is_continue = True

input_trend = sys.argv[1]
input_price = sys.argv[2]
input_category = sys.argv[3]

if 'duo' in input_category:
    category = 'duo'
elif 'kong' in input_category:
    category = 'kong'
else:
    print('input_category 输入格式不正确， 重新输入')
    is_continue = False

if input_trend == 'gt':
    trend = '>='
elif input_trend == 'lt':
    trend = '<='
else:
    print('input_trend 输入格式不正确， 重新输入')
    is_continue = False

price = float(input_price)
if not 1000 <= price <= 100000:
    print('价格输入格式不正确， 重新输入')
    is_continue = False

if is_continue:
    print('-' * 30)
    print('你将开始一个计划委托：当价格 %s %s 时，平%s单' %(trend, price, category))
    print('-' * 30)
else:
    print('输入不合法，自动退出')
    sys.exit()

print('start>>>>>>>>>>>>>>>>>>>>>>>')

while True:

    try:
        # 获取订单信息
        # 有挂单就继续向下，等待持仓成交， 没挂单，则自动退出
        orders = okcoinFuture.future_orderinfo('btc_usd', 'quarter', '-1', '1', '1', '50')
        orders = json.loads(orders)['orders']

        # 全仓持仓信息
        holding = json.loads(okcoinFuture.future_position('btc_usd','quarter'))['holding'][0]
        buy_available = holding['buy_available']
        sell_available = holding['sell_available']

        # 在没有挂单同时也没有持仓的情况下就要退出
        if not len(orders) and buy_available == 0 and sell_available == 0:
            sys.exit()

        # 平多仓
        if category == 'duo' and buy_available > 0:
            amount = buy_available

            # 获取当前价格参数
            current_price = get_btc_price('bitstampbtcusd')
            if current_price:
                current_price = float(current_price)
                logging.info(current_price)

                plan(trend, current_price, price, amount, okcoinFuture, '3', orders)

        # 平空仓
        elif category == 'kong' and sell_available > 0:
            amount = sell_available

            # 获取当前价格参数
            current_price = get_btc_price('bitstampbtcusd')
            if current_price:
                current_price = float(current_price)
                logging.info(current_price)

                plan(trend, current_price, price, amount, okcoinFuture, '4', orders)

    except Exception as e:
        logging.info(e)
        time.sleep(3)
