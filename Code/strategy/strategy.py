# -*- coding: utf-8 -*-
'''
Created on 2016年1月19日

@author: Water
'''

from data_process.market_data import MarketData
from order_process.order_process import OrderProcess


class Strategy(object):
    '''
    classdocs
    '''

    def __init__(self, params):
        '''
        Constructor
        '''
        self.initial_capital = 1000000
        self.order_process_class = OrderProcess()
        print 'strategy init'
        
    def handle_data(self, data):
        print data   
        
    def initialize(self):
        print ''
    
    def set_initial_capital(self, capital):
        self.initial_capital = capital
         
    def add_transform(self, transform_type, data_name_array, attribute_name_array, window_length): 
        print ''
    
    def add_data(self, data_type, data_name, attribute_name_array, from_timestamp, to_timestamp):
        market_data_class = MarketData('Daily')
        self.market_datas = market_data_class.get_data()
        print 'add strategy data'
    
    def order(self, future_id, is_buy, is_open, order_type, price, amount):
        self.order_process_class.process_order(future_id, is_buy, is_open, order_type, price, amount)
        print 'order'