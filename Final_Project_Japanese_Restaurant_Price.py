import requests, json
import pandas as pd

# Unchanged value
API_KEY ='q1OyfS62EE5N4Hv_7Oo6AxWvm71cDH1yHoNVDFFvk2cv30QDHRtTqMyKxXAb7xhUeiV3Il4x8pyVmn6quKCIq0EaT2GCcnXo72ax7KkCnCID_MaLjNvrNPTpLAXXYx'
HEADERS = {'Authorization': 'Bearer %s'% API_KEY}
API_URL = 'https://api.yelp.com/v3/businesses/search'

# Define a function which can search with different input value
def restaurants_df(term, location, max_result=1000):
    restaurants = []
    limit = 50
    
    for x in range(0, max_result, limit):
        params = {
            'term': term,
            'location': location,
            'offset': x,
            'limit': limit
        }
        response = requests.get(API_URL,params = params, headers = HEADERS)
        if response.status_code != 200:
            err_msg = "Request error. Status code not 200"
            print(err_msg)
            return err_msg
        response_dict = json.loads(response.text)
        current_businesses = response_dict['businesses']
        restaurants = restaurants + current_businesses
    
    restaurants_df = pd.DataFrame(restaurants)
    columns = ['name', 'location', 'coordinates', 'price', 'rating', 'review_count']
    restinfo = restaurants_df[columns]
    return restinfo

# Find out the asian restaurants in New York City (Korean, Chinese, Japanese)

# chinese_df = restaurants_df(term='chinese food', location='new york city', max_result=1000)
# korean_df = restaurants_df(term='korean food', location='new york city', max_result=1000)
japanese_df = restaurants_df(term='japanese food', location='new york city', max_result=1000)



# get chinese restaurants' coordinates
#chinese_cor = chinese_df['coordinates']
#ch_lat = [coord["latitude"] for coord in chinese_cor]
#ch_long = [coord["longitude"] for coord in chinese_cor]

# get korean restaurants' coordinates
# korean_cor = korean_df['coordinates']
# kr_lat = [coord['latitude']for coord in korean_cor]
# kr_long = [coord['longitude'] for coord in korean_cor]

# get japanese restaurants' coordinates
japanese_cor = japanese_df['coordinates']
jp_lat = [coord['latitude'] for coord in japanese_cor]
jp_long = [coord['longitude'] for coord in japanese_cor]


# Add longitude and Latitude to chinese_df as two seperate coloumns
# chinese_df['Longitude'] = ch_long
# chinese_df['Latitude'] = ch_lat

# Add longitude and Latitude to korean_df as two seperate coloumns
# korean_df['Longitude'] = kr_long
# korean_df['Latitude'] = kr_lat

japanese_df['Longitude'] = jp_long
japanese_df['Latitude'] = jp_lat


# Extract the value from location and seperate to different columns
# chinese_add = chinese_df['location']
# for key, value in chinese_add[0].items():
#    chinese_df[key] = [add[key] for add in chinese_add] #add the new columns to the dataframe

# korean_add = korean_df['location']
# for key, value in korean_add[0].items():
#    korean_df[key] = [add[key] for add in korean_add]

japanese_add = japanese_df['location']
for key, value in japanese_add[0].items():
    japanese_df[key] = [add[key] for add in japanese_add]


# Restructure the dataframe to a new one chinese_df2
# chinese_df2 = chinese_df[['name','Longitude','Latitude','address1','city','zip_code','state','display_address','price','rating','review_count']]
# korean_df2 = korean_df[['name','Longitude','Latitude','address1','city','zip_code','state','display_address','price','rating','review_count']]
japanese_df2 = japanese_df[['name','Longitude','Latitude','address1','city','zip_code','state','display_address','price','rating','review_count']]



# Export dataframe to csv file
# chinese_df2.to_csv('chinese_df2.csv', sep='\t', encoding='utf-8')
# korean_df2.to_csv('korean_df2.csv', sep='\t', encoding='utf-8')
japanese_df2.to_csv('japanese_df2.csv', sep='\t', encoding='utf-8')
