from flask import Flask, render_template
import pandas as pd 
from flask import request
import pdb

app = Flask(__name__)

@app.route('/home')
def index():
    df = pd.read_csv('data/polylines_data.csv')
    poly = df['polyline'].values
    labels = df['labels'].values
    x = zip(labels,poly)
    return render_template('p_index.html', data = x)

@app.route('/clusters', methods=['POST'])
def cluster_map():
    clusters = [int(c) for c in request.form.values()]
    df = pd.read_csv('data/polylines_data.csv')
    seg = df[df['labels'].isin(clusters)]
    poly = seg['polyline'].values
    labels = seg['labels'].values
    segments = seg['index'].values
    x = zip(labels,poly,segments)
    return render_template('p_clusters_index.html', data = x)

if  __name__ == '__main__':
    app.run(host='0.0.0.0', port=2121, debug=True)