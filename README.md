# GeolocationMongoDB_Project
# Aim of the project
`Database - Crunchbase` is given with more than 18k of company documents, with the business information of most of the USA companies around the world. 

With the aim of finding the perfect spot where an imaginary startup should be created, the following instructions should be delivered:

# Instructions
Using MongoDB and the Python extension PyMongo, we have to generate some geoquerys to the collection to find the perfect place.

You recently created a new company in the `GAMING industry`. The company will have the following scheme:

- 20 Designers
- 5 UI/UX Engineers
- 10 Frontend Developers
- 15 Data Engineers
- 5 Backend Developers
- 20 Account Managers
- 1 Maintenance guy that loves basketball
- 10 Executives
- 1 CEO/President

As a data engineer you have asked all the employees to show their preferences on where to place the new office.
Your goal is to place the **new company offices** in the best place for the company to grow.
You have to found a place that more or less covers all the following requirements.
Note that **it's impossible to cover all requirements**, so you have to prioritize at your glance.

- Designers like to go to design talks and share knowledge. There must be some nearby companies that also do design.
- 30% of the company have at least 1 child.
- Developers like to be near successful tech startups that have raised at least 1 Million dollars.
- Executives like Starbucks A LOT. Ensure there's a starbucks not to far.
- Account managers need to travel a lot
- All people in the company have between 25 and 40 years, give them some place to go to party.
- Nobody in the company likes to have companies with more than 10 years in a radius of 2 KM.
- The CEO is Vegan

# Resources
- MongoDB
- API Google Places 
- API Foursquare
- GeoPandas
- GeoPy
- Cartoframe / Folium to create maps

# Inputs
- Crunchbase JSON
- Airports JSON
- Starbucks CSV

#OUTPUTS
- Best location
- Cleaned JSON and CSV

# Methodology
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

# Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

# Project Status
Learning and enjoying everyday.
Next steps:
- Use folium and generate html maps
- Refactor and generate better functions