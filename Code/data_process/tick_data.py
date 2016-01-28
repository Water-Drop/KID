# -*- coding: utf-8 -*-
'''
Created on 2016年1月19日

@author: Water
'''
import datetime
import os
import pandas as pd
import sys


class TickData(object):
    '''
    classdocs
    '''

    def __init__(self, attribute_name_array, from_timestamp, to_timestamp):
        '''
        Constructor
        '''
        self.attribute_name_array = attribute_name_array
        self.from_timestamp = from_timestamp
        self.to_timestamp = to_timestamp
        self.data = pd.DataFrame()
        
    def get_data(self):
        from_time = datetime.datetime.fromtimestamp(self.from_timestamp)
        to_time = datetime.datetime.fromtimestamp(self.to_timestamp)
        current_date = from_time
        while (current_date <= to_time):
            data_file_name = current_date.strftime("%Y%m%d")
            self.data = self.data.append(self.read_csv_file(data_file_name))
            #print(self.data.count())
            current_date = current_date + datetime.timedelta(days=1)
        return self.data
    
    def read_csv_file(self, filename):
        upper_dir_path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(sys.argv[0])), '..'))
        filepath = upper_dir_path + os.sep + 'data_files' + os.sep + filename + '.csv'
        file_data = pd.read_csv(filepath)
        file_data.drop(len(file_data.index) - 1)
        file_data = file_data.drop(0)
        file_data = file_data.drop(1)
        return file_data