from flask import Flask
import pandas as pd
import googlemaps
import time
from datetime import datetime
from pandas import json_normalize

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/hello')
class distance_matrix:
 def __init__(self,key,origins,destinations,mode,traffic_model):
   self.key = key
   self.origins = origins
   self.destinations = destinations
   self.mode = mode
   self.traffic_model = traffic_model
   self.client = googlemaps.Client(self.key)
 def distance_count(self):
  now = datetime.now()
  m = self.client.distance_matrix(self.origins, self.destinations, self.mode, self.traffic_model, departure_time=now)
  matrixdf = json_normalize(m,['rows','elements']) 
  next_time = time.time()
  h = 1
  for i in range(5):
   now = datetime.now()
   matrix = self.client.distance_matrix(self.origins, self.destinations,self.mode, self.traffic_model,  departure_time=now)
   matrix
   matrixdf2 = json_normalize(matrix,['rows','elements'])
   matrixdf.append(matrixdf2, ignore_index = True)
   print(matrixdf)
   h = h + 5
   next_time += h
   time.sleep(max(0, next_time - time.time()))
   i = i+1
  matrixdf.to_csv('dataset.csv')
  
if __name__ == '__main__':
    
    key = 'AIzaSyDJgJXzuyULRp-t_IYvGoXyjdqi4ohmCEw'
    origin = {"lat": 23.794938, "lng": 90.414314}
    desti =  {"lat": 23.797754, "lng": 90.423387}
    mode = "driving"
    traffic_model = "best_guess"
    d = distance_matrix(key, origin, desti, mode, traffic_model)
    d.distance_count()

    app.run(host='0.0.0.0', debug=False)