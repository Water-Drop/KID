# -*- coding: utf-8 -*-
'''
Created on 2016年1月19日

@author: Water
'''

import strategy.strategy as strategy
import emulator.emulator as emulator

class TrendStrategy(strategy.Strategy):
    '''
    classdocs
    '''

    def initialize(self):
        self.add_data('Daily', '', '', '', '')
    def handle_data(self, data):
        print ''   

t = TrendStrategy('')
e = emulator.Emulator(t)
result = e.run()