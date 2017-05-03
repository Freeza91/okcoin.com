#encoding=utf-8

import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='./trade.log',
                    filemode='w')

def trade(okcoin, _type, amount, current_price):
    okcoin.future_trade('btc_usd','quarter','',amount, _type,'1','10')
    if _type == '3':
        category = '平多'
    elif _type == '4':
        category = '平空'

    logging.info('以%s价格平%s：数量%s' % (current_price, category, amount))

# 对手价
def plan(trend, current_price, plan_price, amount, okcoin, _type):
    if trend == '>=':
        if current_price >= plan_price:
            trade(okcoin, _type, amount, current_price)
    elif trend == '<=':
        if current_price <= plan_price:
            trade(okcoin, _type, amount, current_price)
