# Strava api scraping...rider data

import requests
import json
import requests
import pandas as pd
import numpy as np
import seaborn
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn import metrics
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pdb

# scrape a rider description data set. That is the averages over 200 activies 
# for each of the 600 segments.

def get_leaderboard(id_list):
    '''
    '''
    data = []
    for i in id_list:
        payload = {'page': 2, 'per_page': 200}
        actual_url = strava + str(i) + '/leaderboard'
        r = requests.get(actual_url, data=payload, headers=headers)
        data.append(r.json())

    with open('data/leaderboard_data.json', 'wb') as f:
        json.dump(data, f)

    return None

# get some averages across the leaderboads for each segments

def get_averages(df):
    '''
    Input: Dataframe of the rider leaderboard for each segment
    Output: Dataframe of the averages across the leaderboards for each segment
    '''
    averages = pd.DataFrame(columns = df.columns)
    for i in range(len(df)):
        seg_lb = pd.DataFrame(df['entries'][i])
        # lb = seg_lb[seg_lb['elapsed_time']==seg_lb['moving_time']]
        ave = pd.DataFrame(seg_lb.mean()).T
        averages = pd.concat((averages,ave),axis=0)
    return averages







