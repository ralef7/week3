

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
        station_name = result['stationBeanList'][i]['stationName']
        bikes = result['stationBeanList'][i]['availableBikes']
        longitude_euclid = ((longitude + 87.600915)*(longitude + 87.600915))
        latitude_euclid = ((latitude - 41.793414)*(latitude-41.793414))
        distance= math.sqrt(longitude_euclid + latitude_euclid)
        
        
    if distance < min_distance: 
        min_distance = distance
        min_station = station_name
        min_bikes = bikes
print("The nearest station is: {0} and it currently has {1} bikes available".format(min_station, min_bikes))
            
    
        
    

    
    
 
    
    
            
    
    
