# -*- coding: utf-8 -*-
'''
Created on 2016年1月27日

@author: Water
'''

import pandas as pd

class TradingRecord(object):
    '''
    classdocs
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
        self.trading_record = pd.DataFrame()
        
    def add_trading_record(self, order_timestamp, future_id, deal_timestamp, amount, price, is_buy, is_open):
        new_trading_record = pd.DataFrame({'order_timestamp': order_timestamp,
                      'future_id': future_id,
                      'deal_timestamp': deal_timestamp,
                      'amount': amount,
                      'price': price,
                      'is_buy': is_buy,
                      'is_open': is_open}, index = [len(self.trading_record.index)])
        self.trading_record = self.trading_record.append(new_trading_record)
        
    def get_trading_record(self):
        print'get trading record'
        print self.trading_record
        return self.trading_record
    
    def write_to_csv(self):
        print 'write trading record to csv'
