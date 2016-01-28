# -*- coding: utf-8 -*-
'''
Created on 2016年1月24日

@author: Water
'''

class WinRate(object):
    '''
    classdocs
    '''

    def __init__(self, trading_record):
        '''
        Constructor
        '''
        self.trading_record = trading_record
        self.win_times = 0
        self.loss_times = 0
        
    def get_win_rate(self):
        for i in range(0, len(self.trading_record.index) / 2):
            if (self.trading_record.iloc[2 * i]['is_buy'] == True):
                if (self.trading_record.iloc[2 * i]['price'] < self.trading_record.iloc[2 * i + 1]['price']):
                    self.win_times  = self.win_times + 1
                else:
                    self.loss_times  = self.loss_times + 1    
            else:
                if (self.trading_record.iloc[2 * i]['price'] > self.trading_record.iloc[2 * i + 1]['price']):
                    self.win_times  = self.win_times + 1
                else:
                    self.loss_times  = self.loss_times + 1
        print ('win_times:' + str(self.win_times))
        print ('loss_times:' + str(self.loss_times))
        win_rate = float(self.win_times) / (float(self.win_times) + float(self.loss_times))
        print ('win_rate:' + str(win_rate))
        return win_rate