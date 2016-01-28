# -*- coding: utf-8 -*-
'''
Created on 2016年1月19日

@author: Water
'''

from data_process.market_data import MarketData
from order_process.order_process import OrderProcess
import pandas as pd
from transform.moving_average import MovingAverage
import copy


class Strategy(object):
    '''
    classdocs
    '''

    def __init__(self, params):
        '''
        Constructor
        '''
        self.initial_capital = 1000000
        self.market_datas = pd.DataFrame()
        self.order_process_class = OrderProcess()
        print 'strategy init'
        
    def handle_data(self, data):
        print data   
        
    def initialize(self):
        print ''
    
    def set_initial_capital(self, capital):
        self.initial_capital = capital
         
    def add_transform(self, transform_type, data_name_array, attribute_name_array, window_length):
        if (transform_type == 'MovingAverage'):
            for data_name in data_name_array:
                tmp_attribute_name_array = copy.deepcopy(attribute_name_array)
                for i in range(0, len(tmp_attribute_name_array)):
                    tmp_attribute_name_array[i] = data_name + '.' + tmp_attribute_name_array[i]
                print self.market_datas.count()
                moving_average_class = MovingAverage(window_length, self.market_datas[tmp_attribute_name_array])
                self.merge_transform_data(moving_average_class.get_transform_data())
        else:
            print ('unhandled transformed type')
        print ''
    
    def add_data(self, data_type, data_name, attribute_name_array, from_timestamp, to_timestamp):
        market_data_class = MarketData(data_type, attribute_name_array, from_timestamp, to_timestamp)
        market_data = market_data_class.get_data()
        #print ('in strategy add data when return market data get data:')
        #print (market_data.count())
        self.merge_market_data(data_name, attribute_name_array, market_data) 
        #print ('in strategy add data:')
        #print (self.market_datas.count())
    
    def order(self, future_id, is_buy, is_open, order_type, price, amount):
        self.order_process_class.process_order(future_id, is_buy, is_open, order_type, price, amount)
        print 'order'
    
    def merge_market_data(self, data_name, attribute_name_array, market_data):
        for attribute_name in attribute_name_array:
            market_data = market_data.rename(columns = {attribute_name: data_name + '.' + attribute_name})
        self.market_datas = pd.concat([self.market_datas, market_data], axis=1)
    
    def merge_transform_data(self, transformed_data):
        self.market_datas = pd.concat([self.market_datas, transformed_data], axis=1)
        