var size = 0;
var placement = 'point';

var style_vnetdistance_resultoutpute57d8757f0914caca174c3137d4ea293_1 = function(feature, resolution){
    var context = {
        feature: feature,
        variables: {}
    };
    
    var labelText = ""; 
    var value = feature.get("dist");
    var labelFont = "10px, sans-serif";
    var labelFill = "#000000";
    var bufferColor = "";
    var bufferWidth = 0;
    var textAlign = "left";
    var offsetX = 0;
    var offsetY = 0;
    var placement = 'line';
    if ("" !== null) {
        labelText = String("");
    }
    if (value >= 0.041000 && value <= 826.301000) {
            style = [ new ol.style.Style({
        stroke: new ol.style.Stroke({color: 'rgba(26,150,65,0.6980392156862745)', lineDash: null, lineCap: 'square', lineJoin: 'bevel', width: 5.699999999999999}),
        text: createTextStyle(feature, resolution, labelText, labelFont,
                              labelFill, placement, bufferColor,
                              bufferWidth)
    })]
                    } else if (value >= 826.301000 && value <= 2328.060000) {
            style = [ new ol.style.Style({
        stroke: new ol.style.Stroke({color: 'rgba(166,217,106,0.6980392156862745)', lineDash: null, lineCap: 'square', lineJoin: 'bevel', width: 5.699999999999999}),
        text: createTextStyle(feature, resolution, labelText, labelFont,
                              labelFill, placement, bufferColor,
                              bufferWidth)
    })]
                    } else if (value >= 2328.060000 && value <= 4452.848000) {
            style = [ new ol.style.Style({
        stroke: new ol.style.Stroke({color: 'rgba(255,255,192,0.6980392156862745)', lineDash: null, lineCap: 'square', lineJoin: 'bevel', width: 5.699999999999999}),
        text: createTextStyle(feature, resolution, labelText, labelFont,
                              labelFill, placement, bufferColor,
                              bufferWidth)
    })]
                    } else if (value >= 4452.848000 && value <= 7438.434000) {
            style = [ new ol.style.Style({
        stroke: new ol.style.Stroke({color: 'rgba(253,174,97,0.6980392156862745)', lineDash: null, lineCap: 'square', lineJoin: 'bevel', width: 5.699999999999999}),
        text: createTextStyle(feature, resolution, labelText, labelFont,
                              labelFill, placement, bufferColor,
                              bufferWidth)
    })]
                    } else if (value >= 7438.434000 && value <= 12988.600000) {
            style = [ new ol.style.Style({
        stroke: new ol.style.Stroke({color: 'rgba(215,25,28,0.6980392156862745)', lineDash: null, lineCap: 'square', lineJoin: 'bevel', width: 5.699999999999999}),
        text: createTextStyle(feature, resolution, labelText, labelFont,
                              labelFill, placement, bufferColor,
                              bufferWidth)
    })]
                    };

    return style;
};
