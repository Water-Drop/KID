# -*- coding: utf-8 -*-
'''
Created on 2016年1月28日

@author: Water
'''

import pandas as pd
import copy

class MovingAverage(object):
    '''
    classdocs
    '''


    def __init__(self, time_window, market_data):
        '''
        Constructor
        '''
        self.transform_data = market_data
        self.time_window = time_window
        
    def get_transform_data(self):
        column_names = copy.deepcopy(self.transform_data.columns)
        for i in range(0, len(column_names)):
            column_name = column_names[i]
            self.transform_data[column_name + '.' + 'moving_average' + str(self.time_window)] = pd.rolling_mean(self.transform_data[column_name], self.time_window)
            del self.transform_data[column_name]
        return self.transform_data