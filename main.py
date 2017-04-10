#!/usr/bin/python
# -*- coding: utf-8 -*-
# encoding: utf-8

from OkcoinSpotAPI import OKCoinSpot
from OkcoinFutureAPI import OKCoinFuture

from conf import okcoin

apikey = okcoin.apikey
secretkey = okcoin.secretkey
okcoinRESTURL = okcoin.okcoinRESTURL

#期货API
okcoinFuture = OKCoinFuture(okcoinRESTURL,apikey,secretkey)

print (u' 期货行情信息')
print (okcoinFuture.future_ticker('btc_usd','quarter'))

print (u' 期货市场深度信息')
print (okcoinFuture.future_depth('btc_usd','quarter','6'))

print (u'美元人民币汇率')
print (okcoinFuture.exchange_rate())

print (u'获取预估交割价')
print (okcoinFuture.future_estimated_price('btc_usd'))

print (u'获取全仓账户信息')
print (okcoinFuture.future_userinfo())

#print (u'获取全仓持仓信息')
#print (okcoinFuture.future_position('btc_usd','quarter'))

#print (u'期货下单')
#print (okcoinFuture.future_trade('btc_usd','quarter','0.1','1','1','0','20'))

#print (u'期货批量下单')
#print (okcoinFuture.future_batchTrade('btc_usd','quarter','[{price:0.1,amount:1,type:1,match_price:0},{price:0.1,amount:3,type:1,match_price:0}]','20'))

#print (u'期货取消订单')
#print (okcoinFuture.future_cancel('btc_usd','quarter','47231499'))

#print (u'期货获取订单信息')
#print (okcoinFuture.future_orderinfo('btc_usd','quarter','47231812','0','1','2'))

#print (u'期货逐仓账户信息')
#print (okcoinFuture.future_userinfo_4fix())

#print (u'期货逐仓持仓信息')
#print (okcoinFuture.future_position_4fix('btc_usd','quarter',1))
