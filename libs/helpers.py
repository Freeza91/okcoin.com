#encoding=utf-8

import requests

def get_btc_price(platform='bitstampbtcusd'):
    url = 'https://s2.bitcoinwisdom.com/ticker'
    try:
        data = requests.get(url, timeout=5).json()
        return data[platform]['last']
    except:
        return None

