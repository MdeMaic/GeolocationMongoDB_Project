# GeolocationMongoDB_Project
# OBJETIVE
Database - Crunchbase is given with more than 18k of company documents, with the business information of most of the USA companies around the world. 

With the aim of finding the perfect spot where an imaginary startup should be created, the following instructions should be delivered:

# INSTRUCTIONS
Using MongoDB and the Python extension PyMongo, we have to generate some geoquerys to the collection to find the perfect place. 

# RESOURCES
- MongoDB
- API Google Places 
- API Foursquare
- GeoPandas
- GeoPy
- Cartoframe / Folium to create maps

# INPUTS
- Crunchbase JSON
- Airports JSON
- Starbucks CSV

#OUTPUTS
- Best location
- Cleaned JSON and CSV

# METHODOLOGY
## 1- Filter information
Four filters are made using the crunchbase database. 

### 1 | No 10 year companies in a 2km radius
From 7600 to 1992 documents

### 2 | Airports less than 5km 
From 1992 to 417 documents

### 3 | Startups less than 40km 
From 417 to 126 documents

### 4 | Design companies less than 10km    
From 126 to 82 documents

### Conclusion
Top 20 companies matching these condition ordered by the following priority: airports, startups, design companies and old companies 

Best place: OAKLAND, CALIFORNIA [37.772323,-122.214897]

## 2 - GeoAPIs and map display
The following 4 filters are applied in the best spot to see if this place meets the conditions required.

### 1 | Party
Using Foursquare API

### 2 | Starbucks
Using Starbucks.csv and $geonear function 

### 3 | Schools 
Using Google places API

### 4 | Vegan restaurant
Using Google places API

### Conclusion
Drawing the map, we can conclude that the place selected meet the requirements to create the new business.

#CONTRIBUTING
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

#PROJECT STATUS
Learning and enjoying everyday.
Next steps:
- Use folium and generate html maps
- Refactor and generate better functions