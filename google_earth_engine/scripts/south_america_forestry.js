// Ex: https://earthenginepartners.appspot.com/science-2013-global-forestv
// https://developers.google.com/earth-engine/datasets/catalog/JAXA_ALOS_PALSAR_YEARLY_FNF
ar dataset = ee.ImageCollection('JAXA/ALOS/PALSAR/YEARLY/FNF')
                  .filterDate('2007-01-01', '2017-12-31')
                  .select('fnf');

// Define a rectangular area of interest.
var aoi = ee.Geometry.Polygon(
    [[
      [-55.243243117753764,-11.406265338343747],
      [-55.243243117753764,4.158513431653985],
      [-74.75496186775376,4.158513431653985],
      [-74.75496186775376,-11.406265338343747]
    ]],
    null, false);

var videoArgs = {
  dimensions: 768,
  region: aoi,
  framesPerSecond: 7,
  min: 1,
  max: 3,  
  palette: ['006400', 'FEFF99', '0000FF'],
};

print(dataset.getVideoThumbURL(videoArgs));