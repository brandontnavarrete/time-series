import pandas as pd 
import requests
import math
pd.options.display.max_columns = None
pd.options.display.max_rows = None


def get_people_data(url):
    
    # creating an empty list of people
    people_data = []
    
    # while url is not none this code will keep repeating
    while url:
        
        # make API requests
        response = requests.get(url)
        
        # creates a .json object from our response
        people = response.json()
        
        ## Add the current page's planet information to the `planet_data` list
        people_data.extend(people['results'])
        
        # # Get the next URL from the response
        url = people['next']
        
        #return dataframe
    return people_data

# ---------------------------------------------
def get_planets_data(url):
    planet_data = []
    while url:
        response = requests.get(url)
        planets = response.json()
        planet_data.extend(planets['results'])
        url = planets['next']
    return planet_data