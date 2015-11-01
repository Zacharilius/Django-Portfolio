google.maps.event.addDomListener(window, 'load', coffeeMapInit);  
google.maps.event.addDomListener(window, 'load', seattleNeighborhoodsMapInit); 
  
function seattleNeighborhoodsMapInit() {
  map = new google.maps.Map(document.getElementById('seattleNeighborhoodMap'), {
    zoom: 4,
    center: {lat: -28, lng: 137}
  });

  // [START snippet-load]
  // Load GeoJSON.
  map.data.loadGeoJson('geoJson/australiaTestData.json');
  // [END snippet-load]

  // [START snippet-style]
  // Set the stroke width, and fill color for each polygon
  map.data.setStyle({
    fillColor: 'green',
    strokeWeight: 1
  });
  // [END snippet-style]
} 
  
function coffeeMapInit() {
    google.maps.visualRefresh = true;
    var isMobile = (navigator.userAgent.toLowerCase().indexOf('android') > -1) ||
      (navigator.userAgent.match(/(iPod|iPhone|iPad|BlackBerry|Windows Phone|iemobile)/));
    if (isMobile) {
      var viewport = document.querySelector("meta[name=viewport]");
      viewport.setAttribute('content', 'initial-scale=1.0, user-scalable=no');
    }
    var mapDiv = document.getElementById('coffee-mapCanvas');
    mapDiv.style.width = isMobile ? '100%' : '500px';
    mapDiv.style.height = isMobile ? '100%' : '300px';
    var map = new google.maps.Map(mapDiv, {
      center: new google.maps.LatLng(2.795756106992082, -8.129880812500005),
      zoom: 2,
      mapTypeId: google.maps.MapTypeId.ROADMAP
    });
    map.controls[google.maps.ControlPosition.RIGHT_BOTTOM].push(document.getElementById('googft-legend-open'));
    map.controls[google.maps.ControlPosition.RIGHT_BOTTOM].push(document.getElementById('googft-legend'));

    layer = new google.maps.FusionTablesLayer({
      map: map,
      heatmap: { enabled: false },
      query: {
        select: "col0\x3e\x3e1",
        from: "1mOwEVBrCDZxmwDd7gc-sFl3Us2Ux4tGYRiJIXA7E",
        where: ""
      },
      options: {
        styleId: 2,
        templateId: 2
      }
    });

    if (isMobile) {
      var legend = document.getElementById('googft-legend');
      var legendOpenButton = document.getElementById('googft-legend-open');
      var legendCloseButton = document.getElementById('googft-legend-close');
      legend.style.display = 'none';
      legendOpenButton.style.display = 'block';
      legendCloseButton.style.display = 'block';
      legendOpenButton.onclick = function() {
        legend.style.display = 'block';
        legendOpenButton.style.display = 'none';
      }
      legendCloseButton.onclick = function() {
        legend.style.display = 'none';
        legendOpenButton.style.display = 'block';
      }
    }
  }

