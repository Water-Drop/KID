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
        
    def run(self):
        self.strategy.initialize()
        print ('in emulator run ')
        print self.strategy.market_datas.count()
        print self.strategy.market_datas.head()
        #for i in range(len(self.strategy.market_datas.index)):
        for i in range(0,100000):
            self.strategy.handle_data(self.strategy.market_datas.iloc[i])
        analysis_class = TradingAnalysis(self.strategy.initial_capital)
        analysis_class.add_trading_record(self.strategy.order_process_class.trading_record_class.get_trading_record())
        analysis_class.get_analysis_result()