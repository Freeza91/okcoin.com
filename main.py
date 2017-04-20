#!/usr/bin/python
# -*- coding: utf-8 -*-
# encoding: utf-8

import sys
import json
import time
from OkcoinFutureAPI import OKCoinFuture
from plan_pingcang import plan

from conf import okcoin

apikey = okcoin.apikey
secretkey = okcoin.secretkey
okcoinRESTURL = okcoin.okcoinRESTURL

okcoinFuture = OKCoinFuture(okcoinRESTURL,apikey,secretkey)

category = ''
price = 0
trend = ''

while True:

    input_category = input('输入交易类型: 平多单(duo) or 平空单(kong):\n')
    if input_category == 'duo':
        category = 'duo'
        break
    elif input_category == 'kong':
        category = 'kong'
        break
    else:
        print('输入格式不正确, 重新输入')

while True:

    input_trend = input('输入交易方向: >= or <= :\n')
    if input_trend == '>=':
        trend = '>='
        break
    elif input_trend == '<=':
        trend = '<='
        break
    else:
        print('输入格式不正确， 重新输入')

while True:

    input_price = input('输入触发价: \n')
    price = float(input_price)
    if 1000 <= price <= 100000:
        break
    else:
        print('输入格式不正确， 重新输入')

while True:
    print('-' * 30)
    print('你将开始一个计划委托：当价格 %s%s 时，平%s单' %(trend, price, category))
    print('-' * 30)

    yes_or_no = input('yes 继续 no 结束: \n')

    if yes_or_no == 'yes':
        break
    elif yes_or_no == 'no':
        sys.exit()

rate = okcoinFuture.exchange_rate()['rate']

while True:

    try:
        # 获取订单信息
        # 有挂单就继续向下，等待持仓成交， 没挂单，则自动退出
        # okcoinfuture_orderinfo
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
            current_usd_price = okcoinFuture.future_ticker('btc_usd','quarter')['ticker']['last']
            current_price = round(float(rate) * float(current_usd_price), 1)
            print(current_price)

            plan(trend, current_price, price, amount, okcoinFuture, '3')

        # 平空仓
        elif category == 'kong' and sell_available > 0:
            amount = sell_available

            # 获取当前价格参数
            current_usd_price = okcoinFuture.future_ticker('btc_usd','quarter')['ticker']['last']
            current_price = round(float(rate) * float(current_usd_price), 1)
            print(current_price)

            plan(trend, current_price, price, amount, okcoinFuture, '4')
    except Exception as e:
        print(e)
        time.sleep(3)
