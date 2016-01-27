# -*- coding: utf-8 -*-
'''
Created on 2016年1月19日

@author: Water
'''
from trading_analysis.trading_analysis import TradingAnalysis


class Emulator(object):
    '''
    classdocs
    '''


    def __init__(self, strategy):
        '''
        Constructor
        '''
        self.strategy = strategy
        self.analysis_class = TradingAnalysis()
    def run(self):
        self.strategy.initialize()
        for market_data in self.strategy.market_datas:
            self.strategy.handle_data(market_data)
        self.analysis_class.get_analysis_result()