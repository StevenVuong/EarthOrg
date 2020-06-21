import pandas as pd
from math import sin, cos, sqrt, atan2, radians

def load_oilspills(csvpath: str) -> pd.DataFrame:
    
    oilspills = pd.read_csv(csvpath, 
                            index_col='id', 
                            parse_dates=['open_date'])

    # remove anomalous row (contains additional fields in columns)
    row_8039 = oilspills[oilspills['field_12'].notna()]
    oilspills = oilspills.drop(row_8039.index)

    # drop columns with NaN values
    oilspills = oilspills.dropna(axis=1, how='all')

    # drop column: 'field_10'
    oilspills = oilspills.drop(['field_10'], axis=1)

    oilspills = oilspills.rename(columns={'field_11':'description'})
    
    return oilspills


def calc_coordinates_distance(long1, lat1, long2, lat2) -> float:
    """Returns distance between two coordinates in metres.
    Args:
        - long1 (float)
        - lat1 (float)
        - long2(float)
        - lat2(float)
    Returns:
        - distance (float)
    """

    # approximate radius of earth in km
    R = 6373.0

    lon1 = radians(long1)
    lat1 = radians(lat1)
    lon2 = radians(long2)
    lat2 = radians(lat2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c * 1000 # convert to metres from km

    return distance
