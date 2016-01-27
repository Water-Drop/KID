# -*- coding: utf-8 -*-
'''
Created on 2016年1月24日

@author: Water
'''

from data_process.daily_data import DailyData
from data_process.minute_data import MinuteData
from data_process.tick_data import TickData

class MarketData(object):
    '''
    classdocs
    '''


    def __init__(self, data_type):
        '''
        Constructor
        '''
        if (data_type == 'Daily'):
            self.data_class = DailyData('')
        elif (data_type == 'Minute'):
            self.data_class = MinuteData('')
        elif (data_type == 'Tick'):
            self.data_class = TickData('')
        else:
            print 'unhandled data type'
            
    def get_data(self):
        self.data_class.get_data()