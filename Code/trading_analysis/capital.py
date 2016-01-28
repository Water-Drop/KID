# -*- coding: utf-8 -*-
'''
Created on 2016年1月27日

@author: Water
'''

import pandas as pd

class Capital(object):
    '''
    classdocs
    '''

    def __init__(self, trading_record, initial_capital):
        '''
        Constructor
        '''
        self.trading_record = trading_record
        self.initial_capital = initial_capital
        self.capital = pd.DataFrame()
    def get_capital(self):
        tmp_capital = self.initial_capital
        for i in range(0, len(self.trading_record.index) / 2):
            if (self.trading_record.iloc[2 * i]['is_buy'] == True):
                tmp_capital = tmp_capital - self.trading_record.iloc[2 * i]['price'] * 300
                tmp_capital = tmp_capital + self.trading_record.iloc[2 * i + 1]['price'] * 300
            else:
                tmp_capital = tmp_capital + self.trading_record.iloc[2 * i]['price'] * 300
                tmp_capital = tmp_capital - self.trading_record.iloc[2 * i + 1]['price'] * 300
            new_capital = pd.DataFrame({'capital': tmp_capital}, index = [len(self.capital.index)])
            self.capital = self.capital.append(new_capital)        
        print self.capital
        return self.capital