#encoding=utf-8

import requests

def get_btc_price(platform='bitfinexbtcusd'):
    url = 'https://s2.bitcoinwisdom.com/ticker'
    try:
        data = requests.get(url, timeout=5).json()
        return data[platform]['last']
    except:
        return None

def get_eos_price():
    url = 'https://api.bitfinex.com/v1/pubticker/eosusd'
    try:
        data = requests.get(url, timeout=3).json()
        return data['last_price']
    except:
        return None
