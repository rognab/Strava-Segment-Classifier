# Strava api scraping... physical data

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

# scrape a physical description data set. 
# these are specific stared segments from around the bay area.
# this data is the "what" componnent for the model to make clusters on.


# stuff for the Strava api
STRAVA = 'https://www.strava.com/api/v3/segments/'
URL = 'https://www.strava.com/api/v3/segments/starred'
HEADERS = {'Authorization': 'Bearer a99afa53e8db5aba589b1f3bf9d8f06e00a2184a'}

def get_data():
    '''
    Make a request for the started data. This request returns a list.
    Input: Nothing
    Output: Dumps the file.
    '''
    physical_data = []

    for i in range(1,4,1):
        payload = {'page': i, 'per_page': 200}
        r = requests.get(URL, data=payload, headers=HEADERS)
        physical_data += r.json()

    with open('data/physical_data.json', 'wb') as f:
        json.dump(physical_data, f)

    return df


# Now clean up the features
def clean(df):
    '''
    Selects the features I want to consider and sets the index as the segment id.
    Note I took out 'maximum_grade','elevation_high','elevation_low', but they may 
    be useful later on. 
    Input: dataframe
    Output: dataframe
    '''
    clean_df = df[['average_grade','distance','id']]

    return clean_df.set_index(['id'])

# get the segment details...this takes a little while
# dump that json...
def get_seg_data(id_list):
    '''
    Makes a request for one segment at a time. Appends the data to an empy list 
    and then dump it into a json file.
    Rememeber to change the name of the json file if neccesary.
    Input: List of segment ids
    Output: Dumps the file.
    '''
    data = []
    for i in id_list:
        actual_url = STRAVA + str(i)
        r = requests.get(actual_url, headers=HEADERS)
        data.append(r.json())

    with open('data/seg_data.json', 'wb') as f:
        json.dump(data, f)

    return None

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


# if __name__ == '__main__':

#     data = get_data()
#     physical_data = clean(data)

#     seg_ids = physical_data.index

#     scale_model = scale_data()
#     scaled_data = scale_model.fit_transform(physical_data)

#     km = Km_model(6, scaled_data)

#     physical_data['labels'] = km.labels_

#     return data, scaled_model, km, physical_data






