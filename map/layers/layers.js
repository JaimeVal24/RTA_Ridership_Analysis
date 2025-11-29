var wms_layers = [];


        var lyr_OSMStandard_0 = new ol.layer.Tile({
            'title': 'OSM Standard',
            'opacity': 1.000000,
            
            
            source: new ol.source.XYZ({
            attributions: '&nbsp;&middot; <a href="https://www.openstreetmap.org/copyright">© OpenStreetMap contributors, CC-BY-SA</a>',
                url: 'https://tile.openstreetmap.org/{z}/{x}/{y}.png'
            })
        });
var format_vnetdistance_resultoutpute57d8757f0914caca174c3137d4ea293_1 = new ol.format.GeoJSON();
var features_vnetdistance_resultoutpute57d8757f0914caca174c3137d4ea293_1 = format_vnetdistance_resultoutpute57d8757f0914caca174c3137d4ea293_1.readFeatures(json_vnetdistance_resultoutpute57d8757f0914caca174c3137d4ea293_1, 
            {dataProjection: 'EPSG:4326', featureProjection: 'EPSG:3857'});
var jsonSource_vnetdistance_resultoutpute57d8757f0914caca174c3137d4ea293_1 = new ol.source.Vector({
    attributions: ' ',
});
jsonSource_vnetdistance_resultoutpute57d8757f0914caca174c3137d4ea293_1.addFeatures(features_vnetdistance_resultoutpute57d8757f0914caca174c3137d4ea293_1);
var lyr_vnetdistance_resultoutpute57d8757f0914caca174c3137d4ea293_1 = new ol.layer.Vector({
                declutter: false,
                source:jsonSource_vnetdistance_resultoutpute57d8757f0914caca174c3137d4ea293_1, 
                style: style_vnetdistance_resultoutpute57d8757f0914caca174c3137d4ea293_1,
                popuplayertitle: 'v.net.distance_result — outpute57d8757f0914caca174c3137d4ea293',
                interactive: true,
    title: 'v.net.distance_result — outpute57d8757f0914caca174c3137d4ea293<br />\
    <img src="styles/legend/vnetdistance_resultoutpute57d8757f0914caca174c3137d4ea293_1_0.png" /> 0 - 826<br />\
    <img src="styles/legend/vnetdistance_resultoutpute57d8757f0914caca174c3137d4ea293_1_1.png" /> 826 - 2328<br />\
    <img src="styles/legend/vnetdistance_resultoutpute57d8757f0914caca174c3137d4ea293_1_2.png" /> 2328 - 4453<br />\
    <img src="styles/legend/vnetdistance_resultoutpute57d8757f0914caca174c3137d4ea293_1_3.png" /> 4453 - 7438<br />\
    <img src="styles/legend/vnetdistance_resultoutpute57d8757f0914caca174c3137d4ea293_1_4.png" /> 7438 - 12989<br />' });
var format_Hub_Distance_in_Cities_2 = new ol.format.GeoJSON();
var features_Hub_Distance_in_Cities_2 = format_Hub_Distance_in_Cities_2.readFeatures(json_Hub_Distance_in_Cities_2, 
            {dataProjection: 'EPSG:4326', featureProjection: 'EPSG:3857'});
var jsonSource_Hub_Distance_in_Cities_2 = new ol.source.Vector({
    attributions: ' ',
});
jsonSource_Hub_Distance_in_Cities_2.addFeatures(features_Hub_Distance_in_Cities_2);
var lyr_Hub_Distance_in_Cities_2 = new ol.layer.Vector({
                declutter: false,
                source:jsonSource_Hub_Distance_in_Cities_2, 
                style: style_Hub_Distance_in_Cities_2,
                popuplayertitle: 'Hub_Distance_in_Cities',
                interactive: true,
                title: '<img src="styles/legend/Hub_Distance_in_Cities_2.png" /> Hub_Distance_in_Cities'
            });
var format_Projected_Bus_Stops_in_Citiesbus_stops_projected__stops_3 = new ol.format.GeoJSON();
var features_Projected_Bus_Stops_in_Citiesbus_stops_projected__stops_3 = format_Projected_Bus_Stops_in_Citiesbus_stops_projected__stops_3.readFeatures(json_Projected_Bus_Stops_in_Citiesbus_stops_projected__stops_3, 
            {dataProjection: 'EPSG:4326', featureProjection: 'EPSG:3857'});
var jsonSource_Projected_Bus_Stops_in_Citiesbus_stops_projected__stops_3 = new ol.source.Vector({
    attributions: ' ',
});
jsonSource_Projected_Bus_Stops_in_Citiesbus_stops_projected__stops_3.addFeatures(features_Projected_Bus_Stops_in_Citiesbus_stops_projected__stops_3);
var lyr_Projected_Bus_Stops_in_Citiesbus_stops_projected__stops_3 = new ol.layer.Vector({
                declutter: false,
                source:jsonSource_Projected_Bus_Stops_in_Citiesbus_stops_projected__stops_3, 
                style: style_Projected_Bus_Stops_in_Citiesbus_stops_projected__stops_3,
                popuplayertitle: 'Projected_Bus_Stops_in_Cities — bus_stops_projected__stops',
                interactive: true,
                title: '<img src="styles/legend/Projected_Bus_Stops_in_Citiesbus_stops_projected__stops_3.png" /> Projected_Bus_Stops_in_Cities — bus_stops_projected__stops'
            });
var group_google_transit1 = new ol.layer.Group({
                                layers: [lyr_Projected_Bus_Stops_in_Citiesbus_stops_projected__stops_3,],
                                fold: 'open',
                                title: 'google_transit (1)'});

lyr_OSMStandard_0.setVisible(true);lyr_vnetdistance_resultoutpute57d8757f0914caca174c3137d4ea293_1.setVisible(true);lyr_Hub_Distance_in_Cities_2.setVisible(true);lyr_Projected_Bus_Stops_in_Citiesbus_stops_projected__stops_3.setVisible(true);
var layersList = [lyr_OSMStandard_0,lyr_vnetdistance_resultoutpute57d8757f0914caca174c3137d4ea293_1,lyr_Hub_Distance_in_Cities_2,group_google_transit1];
lyr_vnetdistance_resultoutpute57d8757f0914caca174c3137d4ea293_1.set('fieldAliases', {'fid': 'fid', 'dist': 'dist', });
lyr_Hub_Distance_in_Cities_2.set('fieldAliases', {'fid': 'fid', 'OBJECTID': 'OBJECTID', 'X_COORDINA': 'X_COORDINA', 'Y_COORDINA': 'Y_COORDINA', 'LAT_COORDI': 'LAT_COORDI', 'LONG_COORD': 'LONG_COORD', 'HubName': 'HubName', 'HubDist': 'HubDist', });
lyr_Projected_Bus_Stops_in_Citiesbus_stops_projected__stops_3.set('fieldAliases', {'fid': 'fid', 'stop_id': 'stop_id', 'stop_name': 'stop_name', });
lyr_vnetdistance_resultoutpute57d8757f0914caca174c3137d4ea293_1.set('fieldImages', {'fid': 'TextEdit', 'dist': 'TextEdit', });
lyr_Hub_Distance_in_Cities_2.set('fieldImages', {'fid': 'TextEdit', 'OBJECTID': 'Range', 'X_COORDINA': 'TextEdit', 'Y_COORDINA': 'TextEdit', 'LAT_COORDI': 'TextEdit', 'LONG_COORD': 'TextEdit', 'HubName': 'TextEdit', 'HubDist': 'TextEdit', });
lyr_Projected_Bus_Stops_in_Citiesbus_stops_projected__stops_3.set('fieldImages', {'fid': 'TextEdit', 'stop_id': 'TextEdit', 'stop_name': 'TextEdit', });
lyr_vnetdistance_resultoutpute57d8757f0914caca174c3137d4ea293_1.set('fieldLabels', {'fid': 'no label', 'dist': 'no label', });
lyr_Hub_Distance_in_Cities_2.set('fieldLabels', {'fid': 'no label', 'OBJECTID': 'no label', 'X_COORDINA': 'no label', 'Y_COORDINA': 'no label', 'LAT_COORDI': 'no label', 'LONG_COORD': 'no label', 'HubName': 'no label', 'HubDist': 'no label', });
lyr_Projected_Bus_Stops_in_Citiesbus_stops_projected__stops_3.set('fieldLabels', {'fid': 'no label', 'stop_id': 'no label', 'stop_name': 'no label', });
lyr_Projected_Bus_Stops_in_Citiesbus_stops_projected__stops_3.on('precompose', function(evt) {
    evt.context.globalCompositeOperation = 'normal';
});