# -*- coding: utf-8 -*-
'''
Created on 2016年1月19日

@author: Water
'''

import time

import emulator.emulator as emulator
import strategy.strategy as strategy


class TrendStrategy(strategy.Strategy):
    '''
    classdocs
    '''
    
    def initialize(self):
        from_time = time.strptime("2014-01-06 09:15:00", "%Y-%m-%d %H:%M:%S")
        to_time = time.strptime("2014-01-08 15:15:00", "%Y-%m-%d %H:%M:%S")
        self.add_data('Tick', 'test_data', ['time', 'price','amount', 'bid1', 'ask1'], time.mktime(from_time), time.mktime(to_time))
        self.add_transform('MovingAverage',['test_data'], ['price', 'bid1', 'ask1'], 400)
        self.ordered = False
        self.compare = 0
        self.trade_time = True
        self.trade_is_buy = 0
    def handle_data(self, data):
        now_time = time.strptime(data['test_data.time'][:-4], '%H:%M:%S')
        price = data['test_data.price']
        ma = data['test_data.price.moving_average400']
        if (now_time > time.strptime('15:10:00', '%H:%M:%S')):
            self.trade_time = False
            if (self.ordered == True):
                if(self.trade_is_buy == 1):
                    self.order('IF', False, False, 'LimitOrder', price - 0.6, 2)
                    self.trade_is_buy = 0
                    self.ordered = False
                else:
                    self.order('IF', True, False, 'LimitOrder', price + 0.6, 2)
                    self.trade_is_buy = 0
                    self.ordered = False
        else :
            self.trade_time = True
       
        if (self.compare == -1 and price > ma and self.trade_time == True): #上穿均线
            if (self.ordered == False):
                self.order('IF', True, True, 'LimitOrder', price + 0.6, 2)
                self.trade_is_buy = 1
                self.ordered = True
            else:
                self.order('IF', True, False, 'LimitOrder', price - 0.6, 2)
                self.trade_is_buy = 0
                self.ordered = False
        elif (self.compare == 1 and price < ma and self.trade_time == True):
            if (self.ordered == False):
                self.order('IF', False, True, 'LimitOrder', price - 0.6, 2)
                self.trade_is_buy = -1
                self.ordered = True
            else:
                self.order('IF', False, False, 'LimitOrder', price + 0.6, 2)
                self.trade_is_buy = 0
                self.ordered = False
        if (price > ma):
            self.compare = 1
        elif (price < ma):
            self.compare = -1
     
t = TrendStrategy('')
e = emulator.Emulator(t)
result = e.run()