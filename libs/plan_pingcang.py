#encoding=utf-8

import logging
import json

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='./trade.log',
                    filemode='w')

def trade(okcoin, _type, amount, current_price):
    orders_info = okcoin.future_trade('btc_usd','quarter','',amount, _type,'1','10')
    if _type == '3':
        category = '平多'
    elif _type == '4':
        category = '平空'

    logging.info('以%s价格平%s：数量%s' % (current_price, category, amount))

    return json.loads(orders_info)

# 对手价
def plan(trend, current_price, plan_price, amount, okcoin, _type):

    if trend == '>=':
        if current_price >= plan_price:
            return True, trade(okcoin, _type, amount, current_price)
    elif trend == '<=':
        if current_price <= plan_price:
            return True, trade(okcoin, _type, amount, current_price)

    return False, None

# 查询当前止损单的执行状态，如果当前止损单没有执行或者滑点太大，则取消挂单继续执行
def check_orders(trigger_order, trend, current_price, okcoin):
    order_id = trigger_order['order_id']
    orders = okcoin.future_order_info('btc_usd','quarter', order_id)
    orders = json.loads(orders)
    order = orders[0]
    status = int(order['status'])

    if status == 2:
        return False

    order_price = float(order['price'])

    # 价格差距6, 取消之前的挂单
    if trend == '>=' and current_price - price >= 6:
        okcoin.future_cancel('btc_usd','quarter', order_id)
        return False
    elif trend == '<=' and price - current_price >= 6:
        okcoin.future_cancel('btc_usd','quarter', order_id)
        return False

    return True
