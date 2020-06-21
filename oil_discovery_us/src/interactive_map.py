import configparser
import pandas as pd
import numpy as np
import plotly.express as px


config = configparser.ConfigParser()
config.read('./config.ini')

processed_oilspills_csvpath = config['interactive_map']['processed_oilspills_csvpath']
max_description_charlength = config.getint('interactive_map', 'max_description_charlength')

def main():
    
    # load oilspills
    oilspills = pd.read_csv(
        processed_oilspills_csvpath, 
        parse_dates=['open_date'])

    # fill in NaN values
    nan_value_mapping = {
        'location': 'unknown',
        'threat': 'unknown',
        'commodity': 'N/A',
        'description': 'N/A',
        'max_ptl_release_gallons': oilspills['max_ptl_release_gallons'].mean(),
        'commodity_key_tokens': '[]',
        'description_key_tokens': '[]'
        }
    oilspills = oilspills.fillna(value=nan_value_mapping)

    # TODO: Configure scale to ideal relative matching sizes
    # convert max_ptl_release_gallons to logscale (sizes look better)
    # add 2 so we do not take the log of 0
    oilspills['log_max_ptl_release_gallon'] = np.log2(
        np.add(oilspills['max_ptl_release_gallons'].values, 2)
        )

    # TODO: Separation by number of brackets would be more ideal
    # hotfix for now; limit description key tokens to 500 chars
    oilspills['description_key_tokens'] = [
        string[:max_description_charlength] for string in oilspills['description_key_tokens'].values
        ]

    # TODO: Figure out string formatting for hover box
    # TODO: Look into 'Custom Data' Field
    # plot interactive map
    fig = px.scatter_geo(oilspills, 
                     lat='lat',
                     lon='lon',
                     color="threat",
                     hover_name="name", 
                     animation_frame="year",
                     size='log_max_ptl_release_gallon',
                     hover_data = {
                         'id': True,
                         'location': True, 
                         'commodity': True, 
                         #'description', 
                         'max_ptl_release_gallons': True,
                         'log_max_ptl_release_gallon': False,
                         'commodity_key_tokens':True,
                         'description_key_tokens': True,
                        },
                     center={
                         'lat':51.704921,
                         'lon':-107.618987
                     },
                     projection="natural earth",
                     title='Global Manmade Environmental Disasters over Time'
                     )
    fig.show()


if __name__=="__main__":

    main()
