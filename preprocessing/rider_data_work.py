# Strava api scraping...rider data

import requests
import json
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

# stuff for the Strava api
STRAVA = 'https://www.strava.com/api/v3/segments/'
HEADERS = {'Authorization': 'Bearer a99afa53e8db5aba589b1f3bf9d8f06e00a2184a'}

def get_leaderboard(id_list):
    '''
    '''
    data = []
    for i in id_list:
        payload = {'page': 1, 'per_page': 200}
        actual_url = STRAVA + str(i) + '/leaderboard'
        r = requests.get(actual_url, data=payload, headers=HEADERS)
        data.append(r.json())

    with open('../data/leaderboard_data.json', 'wb') as f:
        json.dump(data, f)

    return

# get some averages across the leaderboads for each segments

def get_averages(df):
    '''
    Input: Dataframe of the rider leaderboard for each segment
    Output: Dataframe of the averages across the leaderboards for each segment
    '''
    averages = pd.DataFrame(columns = df.columns)

    for i in range(len(df)):
        seg_lb = pd.DataFrame(df['entries'][i])
        seg_lb = seg_lb[5:]
        # lb = seg_lb[seg_lb['elapsed_time']==seg_lb['moving_time']]
        ave = pd.DataFrame(seg_lb.mean()).T
        averages = pd.concat((averages,ave),axis=0)
    return averages

# scale the data before fitting it to kmeans. This is neccesary because the data 
# values are in a wide range.
# this function returns the StandardScaler model so I can use inverse_scale later
def scale_data():
    '''
    Returns the StandardScaler model.
    '''

    return StandardScaler()

# runs the K-means clustering model
def Km_model(i, data):
    '''
    Input: The number of clusters and data 
    Output: Kmeans model
    Fits the data and returns the model to be callable later.
    '''
    model = KMeans(n_clusters=i, init='k-means++')
    model.fit(data)

    return model



