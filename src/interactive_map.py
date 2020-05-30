import configparser
import pandas as pd
import numpy as np
import plotly.express as px


config = configparser.ConfigParser()
config.read('./config.ini')

processed_oilspills_csvpath = config['interactive_map']['processed_oilspills_csvpath']

def main():
    
    # load oilspills
    oilspills = pd.read_csv(
        processed_oilspills_csvpath, 
        index_col='id', 
        parse_dates=['open_date'])

    # fill in NaN values
    nan_value_mapping = {
        'location': 'unknown',
        'threat': 'unknown',
        'commodity': '',
        'description': '',
        'max_ptl_release_gallons': oilspills['max_ptl_release_gallons'].mean(),
        'commodity_key_tokens': '',
        'description_key_tokens': '',
        'commodity_key_tokens': '[]',
        'description_key_tokens': '[]'
        }
    oilspills = oilspills.fillna(value=nan_value_mapping)

    # convert max_ptl_release_gallons to logscale (sizes look better)
    # add 2 so we do not take the log of 0
    oilspills['log_max_ptl_release_gallon'] = np.log2(
        np.add(oilspills['max_ptl_release_gallons'].values, 2)
        )

    # plot interactive map
    fig = px.scatter_geo(oilspills, 
                     lat='lat',
                     lon='lon',
                     color="threat",
                     hover_name="name", 
                     animation_frame="year",
                     size='log_max_ptl_release_gallon',
                     hover_data = [
                         'location', 
                         'commodity', 
                         'description', 
                         'max_ptl_release_gallons', 
                         'commodity_key_tokens'],
                     center={
                         'lat':51.704921,
                         'lon':-107.618987
                     }
                     projection="natural earth")
    fig.show()


if __name__=="__main__":

    main()
