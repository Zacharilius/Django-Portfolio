# Leaflet JS
var layer = L.geoJson();
map.addLayer(layer);
$.getJSON("{% url 'data' %}", function (data) {
    layer.addData(data);
});