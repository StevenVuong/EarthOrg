import configparser
import pandas as pd
import plotly.express as px
import os

config = configparser.ConfigParser()
config.read('./config.ini')

processed_oilspills_csvpath = config['interactive_map']['processed_oilspills_csvpath']

def main():
    
    oilspills = pd.read_csv(processed_oilspills_csvpath)
    print(oilspills.head)


if __name__=="__main__":

    main()
