# -*- coding: utf-8 -*-
'''
Created on 2016年1月27日

@author: Water
'''

class TradingRecord(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    def add_trading_record(self, order_timestamp, future_id, deal_timestamp, amount, price, is_buy, is_open):
        print 'add trading record'
        
    def get_trading_record(self):
        print 'get trading record'
    
    def write_to_csv(self):
        print 'write trading record to csv'
