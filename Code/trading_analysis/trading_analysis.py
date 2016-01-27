# -*- coding: utf-8 -*-
'''
Created on 2016年1月24日

@author: Water
'''

class TradingAnalysis(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
    def add_trading_record(self, trading_record):
        self.trading_record = trading_record
        
    def add_valuation_record(self, valuation_record):
        self.valuation_record = valuation_record
        
    def get_analysis_result(self):
        print "get analysis result"     