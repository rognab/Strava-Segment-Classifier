# Combinding the Strava data...rider and physical data

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

def combind_datasets():
    '''
    Input: None
    Output: dataframe
    Combinds the physical data and rider data into one dataset 
    '''
    P = pd.read_csv('data/p_polylines_data.csv')
    R = pd.read_csv('data/r_polylines_data.csv')
    RP = R[['average_hr','average_watts','moving_time', 'average_speed']]
    RP['average_grade'] = P['average_grade']
    RP['distance'] = P['distance']
    RP['total_elevation_gain'] = P['total_elevation_gain']

    return RP

# scale the data before fitting it to kmeans. This is neccesary because the data 
# values are in a wide range.
# this function returns the StandardScaler model so I can use inverse_scale later
def scale_data():
    '''
    Returns the StandardScaler model.
    '''
    model = StandardScaler()

    return model

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

