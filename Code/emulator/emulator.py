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
        print ('in emulator run ')
        #for i in range(len(self.strategy.market_datas.index)):
        for i in range(100):
            self.strategy.handle_data(self.strategy.market_datas.iloc[i])
        self.analysis_class.get_analysis_result()