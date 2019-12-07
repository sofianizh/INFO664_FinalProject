This is a repository for Pratt INFO 664 final project

Project Description

The Project attempts to create maps of three types of restaurants in the New York City based on their price settings. All the data sources are requested through the Yelp API.

The project has two parts: a Python script that makes an API call and performs data manipulation before converting to three csv file, and three Tableau maps built on the csv file. The python file calls a Yelp API for all three requested types restaurants in New York city. Although under certain regulations, Yelp can only provide restaurants information of each type with maximum 1000. Then converts that data into a Panda Dataframe. Drops unwanted columns, and then converts to csv file. After converting all data two the csv file, then upload them to Tableau inorder to generate the map of restaurants with price details. All restaurants are colored differently by the price range. 
