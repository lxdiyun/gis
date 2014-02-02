var initialOpacity = 40;
var OPACITY_MAX_PIXELS = 57; // Width of opacity control image

var mapMinZoom_1949 = 13;
var mapMaxZoom_1949 = 18;
var map_1949 = new google.maps.ImageMapType({ 
		getTileUrl: get_1949_tile,
		tileSize: new google.maps.Size(256, 256),
		name: "1949",
		minZoom: mapMinZoom_1949,
		maxZoom: mapMaxZoom_1949,
	});

var mapBounds_1949 = new google.maps.LatLngBounds(
	new google.maps.LatLng(23.348972, 116.664980),
	new google.maps.LatLng(23.364400, 116.692866)); 

function old_map_init() {
	load_map();
	map.fitBounds(mapBounds_1949);
	map.map.overlayMapTypes.insertAt('1949', map_1949);
	$('#map').fadeOut('fast');
	$('#map').fadeIn('slow');


	// Add opacity control and set initial value
	createOpacityControl(map.map, initialOpacity);
}


function get_1949_tile (coord, zoom) {
	var proj = map.getProjection();
	var tileSize = 256 / Math.pow(2,zoom);
	var tileBounds = new google.maps.LatLngBounds(
		proj.fromPointToLatLng(new google.maps.Point(coord.x*tileSize, (coord.y+1)*tileSize)),
		proj.fromPointToLatLng(new google.maps.Point((coord.x+1)*tileSize, coord.y*tileSize))
		); 
	var inter = mapBounds_1949.intersects(tileBounds);
	if (mapBounds_1949.intersects(tileBounds) && (zoom >= mapMinZoom_1949) && (zoom <= mapMaxZoom_1949))
		return "/website/static/old_map/1949/" +
			+ zoom + "/" + coord.x + "/" + (Math.pow(2, zoom)-coord.y-1) + ".png";
	else
		return "http://www.maptiler.org/img/none.png"; 
}

function createOpacityControl(map, opacity) {
	var sliderImageUrl = "/website/static/OpacityControl/opacity-slider3d14.png";

	// Create main div to hold the control.
	var opacityDiv = document.createElement('DIV');
	opacityDiv.setAttribute("style", "margin:5px;overflow-x:hidden;overflow-y:hidden;background:url(" + sliderImageUrl + ") no-repeat;width:71px;height:21px;cursor:pointer;");

	// Create knob
	var opacityKnobDiv = document.createElement('DIV');
	opacityKnobDiv.setAttribute("style", "padding:0;margin:0;overflow-x:hidden;overflow-y:hidden;background:url(" + sliderImageUrl + ") no-repeat -71px 0;width:14px;height:21px;");
	opacityDiv.appendChild(opacityKnobDiv);

	var opacityCtrlKnob = new ExtDraggableObject(opacityKnobDiv, {
		restrictY: true,
	    container: opacityDiv
	});

	var dragEndEvent = google.maps.event.addListener(opacityCtrlKnob, "dragend", function () {
		setOpacity(opacityCtrlKnob.valueX());
	});

	var clickEvent = google.maps.event.addDomListener(opacityDiv, "click", function (e) {
		var left = findPosLeft(this);
		var x = e.pageX - left - 5; // - 5 as we're using a margin of 5px on the div
		opacityCtrlKnob.setValueX(x);
		setOpacity(x);
	});

	map.controls[google.maps.ControlPosition.TOP_RIGHT].push(opacityDiv);

	// Set initial value
	var initialValue = OPACITY_MAX_PIXELS / (100 / opacity);
	opacityCtrlKnob.setValueX(initialValue);
	setOpacity(initialValue);
}

function setOpacity(pixelX) {
	// Range = 0 to OPACITY_MAX_PIXELS
	var value = (1 / OPACITY_MAX_PIXELS) * pixelX;
	if (value < 0) value = 0;
	map_1949.setOpacity(value);
}

function findPosLeft(obj) {
	var curleft = 0;
	if (obj.offsetParent) {
		do {
			curleft += obj.offsetLeft;
		} while (obj = obj.offsetParent);
		return curleft;
	}
	return undefined;
}
