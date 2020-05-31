import pandas as pd

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
