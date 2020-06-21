// Greenland Temperatures
// https://developers.google.com/earth-engine/datasets/catalog/MODIS_006_MOD11A2
var dataset = ee.ImageCollection('IDAHO_EPSCOR/TERRACLIMATE')
                  .filter(ee.Filter.date('2010-01-01', '2020-01-01'))
                  // .filter(ee.Filter.calendarRange(1972,2020,'year'))
                  // .filter(ee.Filter.calendarRange(1,1,'month'))
                  .select('tmmx');

//Map.addLayer(maximumTemperature, maximumTemperatureVis, 'Maximum Temperature');

// Define a rectangular area of interest.
var aoi = ee.Geometry.Polygon(
  [[
    [-9.150796497441053,57.793817875664836],
    [-9.150796497441053,84.14214845046604], 
    [-82.97892149744105,84.14214845046604], 
    [-82.97892149744105,57.793817875664836]
  ]],
  null, false);

var videoArgs = {
  dimensions: 768,
  region: aoi,
  framesPerSecond: 7,
  min: -300.0,
  max: 300.0,  
  palette: [
    '1a3678', '2955bc', '5699ff', '8dbae9', 'acd1ff', 'caebff', 'e5f9ff',
    'fdffb4', 'ffe6a2', 'ffc969', 'ffa12d', 'ff7c1f', 'ca531a', 'ff0000',
    'ab0000'
  ],
};

print(dataset.getVideoThumbURL(videoArgs));