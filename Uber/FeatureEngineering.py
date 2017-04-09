# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 22:30:49 2017

@author: zhang_000
"""
# feature generation functions
    
class FeatureEngineering(object):
    
    def __init__(self, rawFile):
      self.rawFile = rawFile
      self.rawData = self.loadRawData()
            
    def loadRawData(self):
        import pandas as pd
        #load data from file       
        rawData = pd.read_csv(self.rawFile, header = 0, sep = ',')
        return rawData
    
    ''' generate following features:    
    City_name: categorical 
    Signup_os: categorical 
    Signup_channel: categorical
    vehicle_info_offered: boolean
    Vehicle_date: categorical
    Vehicle_made: categorical
    Vehicle_model: categorical
    Vehicle_year: categorical
    weekday_sign_on: categorical
    Days_between_sign_on_and_bgc: numerical
    '''    
    
    def generateFeatures(self):
        import pandas as pd
        import numpy as np
        import datetime
        
        selectedCols = ['city_name', 'signup_os', 'signup_date','bgc_date', \
        'signup_channel', 'vehicle_added_date', 'vehicle_make', \
        'vehicle_model', 'vehicle_year']
        
        features = self.rawData[selectedCols]
    
        # fill nan in bgc date with an arbitoary late date
        features['bgc_date'].fillna(datetime.date.today().strftime('%m/%d/%Y'), inplace=True)
        features['vehicle_added_date'].fillna(datetime.date.today().strftime('%m/%d/%Y'), inplace=True)
                
        # impute signup_os
        features['signup_os'].fillna('NA', inplace=True)
        
        features['signup_date'] = features['signup_date'].apply(lambda x: datetime.datetime.strptime(x, '%m/%d/%Y'))
        features['bgc_date'] = features['bgc_date'].apply(lambda x: datetime.datetime.strptime(x, '%m/%d/%Y'))
        features['interval_between_signup_bcg'] = features['bgc_date'] - features['signup_date']
        features['interval_between_signup_bcg'] = features['interval_between_signup_bcg'].apply(lambda x: x.days)
        features['signup_date'] = features['signup_date'].apply(lambda x: x.weekday())
        features['vehicle_info_offered'] = features['vehicle_make'].notnull()
        
         # impute missing value in vehical information
        features['vehicle_make'].fillna('NA', inplace=True)
        features['vehicle_model'].fillna('NA', inplace=True)
        features['vehicle_year'].fillna(features['vehicle_year'].median(), inplace=True)

        features = features.drop(['bgc_date'], 1)
        
        features = pd.get_dummies(features)
        return features
    
    def generateLabels(self):
        import pandas as pd
    
        labels = self.rawData['first_completed_date']
        labels = labels.notnull()
        return labels
            
     