# -*- coding: utf-8 -*-
'''
Created on 2016年1月24日

@author: Water
'''
from capital import Capital
from win_rate import WinRate


class TradingAnalysis(object):
    '''
    classdocs
    '''

    def __init__(self, initial_capital):
        '''
        Constructor
        '''
        self.initial_capital = initial_capital
    def add_trading_record(self, trading_record):
        self.trading_record = trading_record
        
    def add_valuation_record(self, valuation_record):
        self.valuation_record = valuation_record
        
    def get_analysis_result(self):
        print "get analysis result" 
        win_rate_class = WinRate(self.trading_record)
        win_rate_class.get_win_rate()
        capital_class = Capital(self.trading_record, self.initial_capital)
        capital_class.get_capital()
            