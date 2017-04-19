#encoding=utf-8

# 对手价
def plan(trend, current_price, plan_price, amount, okcoin, _type):
    if trend == '>=':
        if current_price >= plan_price:
            okcoin.future_trade('btc_usd','quarter','',amount,_type,'1','10'))
    elif trend == '<=':
        if current_price <= plan_price:
            okcoin.future_trade('btc_usd','quarter','',amount,_type,'1','10'))

# print (u'期货逐仓账户信息')
# print (okcoinFuture.future_userinfo_4fix())

# print (u'期货逐仓持仓信息')
# print (okcoinFuture.future_position_4fix('btc_usd','quarter',1))
