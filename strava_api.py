# Strava stuff - Day3/4/5

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

# scrape a better physical description data set 
# this is specifically stared segments

strava = 'https://www.strava.com/api/v3/segments/'
url = 'https://www.strava.com/api/v3/segments/starred'
headers = {'Authorization': 'Bearer a99afa53e8db5aba589b1f3bf9d8f06e00a2184a'}

def get_data():
    '''
    Make a request for the data... note this request returns a list...
    dumps the file and sefs it to a data frame.
    '''
    physical_data = []

    for i in range(1,4,1):
        payload = {'page': i, 'per_page': 200}
        r = requests.get(url, data=payload, headers=headers)
        physical_data += r.json()

    with open('physical_data.json', 'wb') as f:
        json.dump(physical_data, f)

    df = pd.read_json('physical_data.json')

    return df

# Now clean up the features

def clean(df):
    '''
    Selects the features I want to consider and sets the index as the segment id.
    Took out 'maximum_grade','elevation_high','elevation_low'.
    '''
    clean_df = df[['average_grade','distance','id']]

    return clean_df.set_index(['id'])

# get the segment details...this takes a little while
# dump that json...

def get_seg_data(id_list):
    '''
    Input: list of segment ids, output: None
    Gets one segment at a time. Appends the data to an empy list 
    and then dump it into a json file.
    Rememeber to change the name of the json file if neccesary.
    '''
    data = []
    for i in id_list:
        actual_url = strava + str(i)
        r = requests.get(actual_url, headers=headers)
        data.append(r.json())

    with open('seg_data.json', 'wb') as f:
        json.dump(data, f)

    return None

# scale the data before fitting it to kmeans... gives better clustering.
# this function also returns the StandardScaler model so I can use inverse_scale later

def scale_data():
    '''
    Returns the StandardScaler model and the fit_transformed data.
    '''
    model = StandardScaler()

    return model

# runs the K-means clustering model

def Km_model(i, data):
    '''
    Input data and the number of clusters desiered
    Fits the data and returns the model to do other things...
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






