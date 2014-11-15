from flask import Flask, render_template
import pandas as pd 
from flask import request
import pdb

app = Flask(__name__)

# Flask code to visulaize the models labeling results.
# Each data set has two functions to plot the segments using the google api. 
# One ploting all segments and color coordinate the labeled clusters,
# the other ploting the slected cluster of segments and info windows of their summary.

# Data Sets: physical data, rider data, and the combination of the two.

# Physical Data Analysis
@app.route('/physical_data')
def p_index():
    df = pd.read_csv('data/p_polylines_data.csv')
    poly = df['polyline'].values
    labels = df['labels'].values
    x = zip(labels,poly)
    return render_template('p_index.html', data = x)

@app.route('/physical_clusters', methods=['POST'])
def p_cluster_map():
    clusters = [int(c) for c in request.form.values()]
    df = pd.read_csv('data/p_polylines_data.csv')
    seg = df[df['labels'].isin(clusters)]
    poly = seg['polyline'].values
    labels = seg['labels'].values
    segments = seg['index'].values
    grade = seg['average_grade'].values
    distance = seg['distance'].values
    elevation = seg['total_elevation_gain'].values
    x = zip(labels,poly,segments,grade,distance,elevation)
    return render_template('p_clusters_index.html', data = x)

# Rider Data Analysis
@app.route('/rider_data')
def r_index():
    df = pd.read_csv('data/r_polylines_data.csv')
    poly = df['polyline'].values
    labels = df['labels'].values
    x = zip(labels,poly)
    return render_template('r_index.html', data = x)

@app.route('/rider_clusters', methods=['POST'])
def r_cluster_map():
    clusters = [int(c) for c in request.form.values()]
    df = pd.read_csv('data/r_polylines_data.csv')
    seg = df[df['labels'].isin(clusters)]
    poly = seg['polyline'].values
    labels = seg['labels'].values
    segments = seg['id'].values
    hr = seg['average_hr'].values
    watts = seg['average_watts'].values
    time = seg['moving_time'].values
    speed = seg['average_speed'].values
    x = zip(labels,poly,segments,hr,watts,time,speed)
    return render_template('r_clusters_index.html', data = x)

# Combination of Rider and Physical 
@app.route('/rider_physical_data')
def rp_index():
    df = pd.read_csv('data/rp_polylines_data.csv')
    poly = df['polyline'].values
    labels = df['labels'].values
    x = zip(labels,poly)
    return render_template('rp_index.html', data = x)

@app.route('/rider_physical_clusters', methods=['POST'])
def rp_cluster_map():
    clusters = [int(c) for c in request.form.values()]
    df = pd.read_csv('data/rp_polylines_data.csv')
    seg = df[df['labels'].isin(clusters)]
    poly = seg['polyline'].values
    labels = seg['labels'].values
    segments = seg['id'].values
    grade = seg['average_grade'].values
    distance = seg['distance'].values
    elevation = seg['total_elevation_gain'].values
    hr = seg['average_hr'].values
    watts = seg['average_watts'].values
    time = seg['moving_time'].values
    speed = seg['average_speed'].values
    x = zip(labels,poly,segments,grade,distance,elevation,hr,watts,time,speed)
    return render_template('rp_clusters_index.html', data = x)

if  __name__ == '__main__':
    app.run(host='0.0.0.0', port=2112, debug=True)