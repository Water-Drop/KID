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
        self.add_data('Tick', 'test_data', ['price','amount', 'bid1', 'ask1'], time.mktime(from_time), time.mktime(to_time))
    def handle_data(self, data):
        print data['test_data.price']

t = TrendStrategy('')
e = emulator.Emulator(t)
result = e.run()