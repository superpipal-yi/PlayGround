# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 21:56:37 2017

@author: zhang_Yi
"""
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import datetime
from FeatureEngineering import FeatureEngineering
#load data from file
rawDataFile = './ds_challenge_v2_1_data (1) (1).csv'  
rawData = pd.read_csv(rawDataFile, header = 0, sep = ',')

# check for missing data
[num_instance, num_col] = rawData.shape
numMissingData = rawData.isnull().sum()
rawDataWithTrip = rawData.loc[rawData['first_completed_date'].notnull()]    
numMissingDataWithTrip = rawDataWithTrip.isnull().sum()      

# check whether absolute date carries information
numOfTrips = rawDataWithTrip[['first_completed_date','signup_date']].groupby(['signup_date']).count()
numOfTrips.sort_index(inplace = True)  
date = [datetime.datetime.strptime(d, '%m/%d/%Y') for d in numOfTrips.index]       
plt.bar(date, numOfTrips['first_completed_date'])              
plt.xlabel('Date')
plt.ylabel('Number of Drivers who Made Trips')

numOfTrips = rawDataWithTrip[['first_completed_date','bgc_date']].groupby(['bgc_date']).count()
numOfTrips.sort_index(inplace = True)  
date = [datetime.datetime.strptime(d, '%m/%d/%Y') for d in numOfTrips.index]       
plt.bar(date, numOfTrips['first_completed_date'])              
plt.xlabel('Date')
plt.ylabel('Number of Drivers who Made Trips')

#understand some correlations
rawDataFile = './ds_challenge_v2_1_data (1) (1).csv' 
FE = FeatureEngineering(rawDataFile)
rawData = FE.loadRawData()
features = FE.generateFeatures()
labels = FE.generateLabels()

features = features.join(rawData['first_completed_date'])
numOfTripsOnOs = features[['first_completed_date','signup_os']].groupby(['signup_os']).count() 
plt.bar(range(len(numOfTripsOnOs)), numOfTripsOnOs['first_completed_date'])              
plt.xticks(range(len(numOfTripsOnOs)), numOfTripsOnOs.index)
plt.xlabel('Sign On OS')
plt.ylabel('Number of Drivers who Made Trips')

numOfTripsOnInt = features[['first_completed_date','interval_between_signup_bcg']].groupby(['interval_between_signup_bcg']).count() 
numOfTripsOnInt.sort_index(inplace = True)  
plt.bar(range(len(numOfTripsOnInt)), numOfTripsOnInt['first_completed_date'])              
plt.xticks(range(len(numOfTripsOnInt)), numOfTripsOnInt.index)
plt.xlabel('Time Intervals between Sign On and Background Check')
plt.ylabel('Number of Drivers who Made Trips')

numOfTripsOnCarYear = features[['first_completed_date','vehicle_year']].groupby(['vehicle_year']).count() 
numOfTripsOnCarYear.sort_index(inplace = True)  
plt.bar(range(len(numOfTripsOnCarYear)), numOfTripsOnCarYear['first_completed_date'])              
plt.xticks(range(len(numOfTripsOnCarYear)), numOfTripsOnCarYear.index)
plt.xlabel('Car Year')
plt.ylabel('Number of Drivers who Made Trips')

numOfTripsOnChannel = features[['first_completed_date','signup_channel']].groupby(['signup_channel']).count() 
numOfTripsOnChannel.sort_index(inplace = True)  
plt.bar(range(len(numOfTripsOnChannel)), numOfTripsOnChannel['first_completed_date'])              
plt.xticks(range(len(numOfTripsOnChannel)), numOfTripsOnChannel.index)
plt.xlabel('Sign up Channel')
plt.ylabel('Number of Drivers who Made Trips')

numOfTripsOnMake = features[['first_completed_date','vehicle_make']].groupby(['vehicle_make']).count() 
numOfTripsOnMake.sort(['first_completed_date'], ascending=False, inplace = True)  
plt.bar(range(len(numOfTripsOnMake)), numOfTripsOnMake['first_completed_date'])              
plt.xticks(range(len(numOfTripsOnMake)), numOfTripsOnMake.index)
plt.xlabel('Car Make')
plt.ylabel('Number of Drivers who Made Trips')

numOfTripsOnDays = features[['first_completed_date','signup_date']].groupby(['signup_date']).count() 
numOfTripsOnDays.sort(['first_completed_date'], ascending=False, inplace = True)  
plt.bar(range(len(numOfTripsOnDays)), numOfTripsOnDays['first_completed_date'])              
plt.xticks(range(len(numOfTripsOnDays)), numOfTripsOnDays.index)
plt.xlabel('Sign on Week Days')
plt.ylabel('Number of Drivers who Made Trips')