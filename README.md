# Oilspill_Dashboard
Building a dashboard to monitor oil spills across the US

Data:
-  US_oilspills.csv: csv with information about US oilspills with columns:
    -  id 
    -  open_date 
    -  name 
    -  location 
    -  lat 
    -  lon 
    -  threat
    -  commodity 
    -  max_ptl_release_gallons 
    -  field_10 to field_25

## Quickstart:

1)  Create Virtual Environment and Install Libraries (not necessary but recommended)
    ```
    python3 -m venv earth
    ```
    And access with
    ```
    source activate ./earth/bin/activate
    ```
    Note: You can exit the virtual environment at any time with `deactivate`.
    Install libraries with
    ```
    python3 -m pip install -r ./requirements.txt
    ```

2)  Run the Jupyter Notebooks:
    ```
    jupyter lab .
    ```
    Then go into `./notebooks` and have a look at the notebooks available.
    -  EDA (Exploratory Data Analysis): Creates static visualisations of the
    raw data and engineers additional features. Examples can be seen in the
    `./screenshots/EDA` directory. In the notebook we have also listed out 
    findings from the data and our approach in processing the raw data within
    markdown cells.


3)  Run the interactive dashboard locally:
    ```
    cd ./src && python interactive_map.py
    ```
    Supplementary Video: https://youtu.be/vnOs3hBXjDY (recommend watch on high 
    quality)


## Final Words:
This was actually a really fun task and I can highly appreciate the value of 
simple yet informative and fun visuals to convey a particular message. So thank
you to the team at Earth.og for giving me the opportunity to play with this data
and I hope to hear from you guys soon.

One book I would recommeend which talks about similar topics is 'Factfulness', by
Hans Rosling who uses simple and effective visualisation to show the world why
things in the world are better than they are depicted to be.
