# Manmade Environmental Disaster Discovery and Visualisation
Visualising and uncovering the hidden data behind manmade environmental
disasters.

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

-  US State boundaries from: http://www.arcgis.com/home/item.html?id=f7f805eb65eb4ab787a0a3e1116ca7e5

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
    -  `EDA.ipynb` (Exploratory Data Analysis): Creates static visualisations of the
    raw data and engineers additional features. Examples can be seen in the
    `./screenshots/EDA` directory. In the notebook we have also listed out 
    findings from the data and our approach in processing the raw data within
    markdown cells.
    -  Answers for the required exercises/tasks can be found in `Exercises.ipynb`.


3)  Run the interactive dashboard locally:
    ```
    cd ./src && python interactive_map.py
    ```
    Supplementary Video: https://youtu.be/vnOs3hBXjDY (recommend watch on high 
    quality)

### Future Works:
An idea I had going forward with this data is to create a metric which assesses 
the environmental health of a certain region which decreases following a big
incident and we are able to quantify the degree of damage (example: an oilspill
might be more catastrophic than a whale carcass on a beach) and will slowly degrade
over time.

With this, not only can one provide analytics of how a region has been impacted,
but the ecosystems around it and then use this past data to inform current ongoings
in terms of the broader impact of a regio, taking into account more factors to 
help decision makers understand better the outcomes of some of their potential 
options.

Another small technical detail could be to include some clustering techniques
(unsupervised learning) to see if there are any hidden patterns within the data.
This is as well as some NLP (natural language processing) techniques that
could be done on the description or commodity sections to gain more insight. And 
of course, as always, more data is always welcome.


## Final Words:
This was actually a really fun task and I can highly appreciate the value of 
simple yet informative and fun visuals to convey a particular message. So thank
you to the team at Earth.og for giving me the opportunity to play with this data
and I hope to hear from you guys soon.

One book I would recommeend which talks about similar topics is 'Factfulness', by
Hans Rosling who uses simple and effective visualisation to show the world why
things in the world are better than they are depicted to be.
