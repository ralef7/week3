

import math
import json
from urllib.request import urlopen


webservice_url = "http://www.divvybikes.com/stations/json"
data = urlopen(webservice_url).read().decode("utf8")
result = json.loads(data)
min_distance = (float("inf"))

stations = result['stationBeanList']
x = len(stations) 

for i in range(x):  
    if len(result):
        latitude = result['stationBeanList'][i]['latitude']
        longitude = result['stationBeanList'][i]['longitude']
        stations = result['stationBeanList'][i]['stationName']
        bikes = result['stationBeanList'][i]['availableBikes']
        station_distance_euclid = ((longitude + 87.600915)*(longitude + 87.600915))
        static_distance_euclid = ((latitude - 41.793414)*(latitude-41.793414))
        distance= math.sqrt(station_distance_euclid + static_distance_euclid)
        
        
    if distance < min_distance: 
        min_distance = distance
        min_station = stations
        min_bikes = bikes
print("The nearest station is: {0} and it currently has {1} bikes available".format(min_station, min_bikes))
            
    
        
    

    
    
 
    
    
            
    
    
