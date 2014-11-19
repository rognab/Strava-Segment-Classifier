This is a tool for classifying and visualizing Bay Area Strava road segments according to specific competitive cyclist workout types.

A full detailed description and links to the live version of the app can be found here at http://www.davidbangor.com/blog

Outline of what is in this repo:

1. The data folder contains all the data related to this project.  
2. The preprocessing folder contains all the files for scraping the data using Strava's API.  
3. Then templates folder contains all the html files that visualize the data and the models results on a google map using the google map API.  
4. The Workout Type Definitions.txt file is a discription of defined workout types for regimented training efforts.  
5. The model_app.py file is the main file that calls on the template files and runs the app.  

How to fully run the app you need:
* model_app.py to run the app
* the entire templates folder
* p_polylines_data.csv, r_polylines_data.csv, and rp_polylines_data.csv from the data file (you can use the entire data folder or select these three files and make your own data folder)

Then to actually run the app all you need to do is run the model_app.py file and go to the correct url.  
/physical_data will give the model based on the physical characteristics of the segments.  
/rider_data will give the model based on how competitive cyclists are riding the segments.  
/rider_physical_data will give the model based on both data sets and is the best tool for classifying Bay Area Strava road segments according to specific competitive cyclist workout types. 
