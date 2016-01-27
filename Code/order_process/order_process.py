# -*- coding: utf-8 -*-
'''
Created on 2016年1月26日

@author: Water
'''
from order_process.trading_record import TradingRecord


class OrderProcess(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.trading_record_class = TradingRecord()
    def process_order(self, future_id, is_buy, is_open, order_type, price, amount):
        self.trading_record_class.add_trading_record('', future_id, '', amount, price, is_buy, is_open)
        print ''
        
        