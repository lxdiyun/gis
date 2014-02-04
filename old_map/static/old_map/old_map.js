var OVERLAY_INDEX = 0;
var MAP_DEFAULT_ZOOM = 13;
var MAP_DEFAULT_CENTER = [23.37, 116.71];
var LAYER_1949_ID = "map_1949";


var LAYER_MIN_ZOOM_1949 = 13;
var LAYER_MAX_ZOOM_1949 = 18;


var g_current_layer_id = null;
var g_layers = {};
var g_layer_boudns = {};

function old_map_init() {
	var mapOption = { 
		div: '#map', 
		zoom: MAP_DEFAULT_ZOOM,
		lat: MAP_DEFAULT_CENTER[0], 
		lng: MAP_DEFAULT_CENTER[1],
		streetViewControl: false,
		overviewMapControl: false,
		panControl: false,
		scaleControl: true,
		scaleControlOptions: {
			position: google.maps.ControlPosition.RIGHT_BOTTOM
		},
		mapTypeControl: true,
		mapTypeControlOptions: {
			style: google.maps.MapTypeControlStyle.DROPDOWN_MENU,
			position: google.maps.ControlPosition.TOP_LEFT
		},
		zoomControl: false,
	};
	map = new GMaps(mapOption);
	$('#map').fadeOut('fast');
	$('#map').fadeIn('slow');

	init_map_layers();
	init_map_buttons();
	init_slider();

	show_bounds(LAYER_1949_ID);
	show_layer(LAYER_1949_ID);
}

function init_map_layers() {
	var map_1949 = new google.maps.ImageMapType({ 
		getTileUrl: get_1949_tile,
	    tileSize: new google.maps.Size(256, 256),
	    name: "1949",
	    minZoom: LAYER_MIN_ZOOM_1949,
	    maxZoom: LAYER_MAX_ZOOM_1949,
	});

	var map_Bounds_1949 = new google.maps.LatLngBounds(
		new google.maps.LatLng(23.348972, 116.664980),
		new google.maps.LatLng(23.364400, 116.692866)); 

	g_layers[LAYER_1949_ID] = map_1949;
	g_layer_boudns[LAYER_1949_ID] = map_Bounds_1949;
}

function show_layer(layer_id) {
	if (layer_id in g_layers) { 
		layer = g_layers[layer_id];
		map.map.overlayMapTypes.insertAt(OVERLAY_INDEX, layer);
		layer.setOpacity($('#opacity_slider').slider('getValue')/100);
		g_current_layer_id = layer_id;

		if (!$('#opacity_slider').slider('isEnabled')) {
			$('#opacity_slider').slider('enable');
		}

	}
}

function show_bounds(layer_id) {
		if ((null != layer_id) && layer_id in g_layer_boudns) {
			map.fitBounds(g_layer_boudns[layer_id]);
		} else {
			map.setZoom(MAP_DEFAULT_ZOOM);
			map.setCenter(MAP_DEFAULT_CENTER[0], MAP_DEFAULT_CENTER[1]);
		}
}

function get_1949_tile (coord, zoom) {
	var proj = map.getProjection();
	var tileSize = 256 / Math.pow(2,zoom);
	var tileBounds = new google.maps.LatLngBounds(
		proj.fromPointToLatLng(new google.maps.Point(coord.x*tileSize, (coord.y+1)*tileSize)),
		proj.fromPointToLatLng(new google.maps.Point((coord.x+1)*tileSize, coord.y*tileSize))
		); 
	var inter = g_layer_boudns[LAYER_1949_ID].intersects(tileBounds);
	if (inter && (zoom >= LAYER_MIN_ZOOM_1949) && (zoom <= LAYER_MAX_ZOOM_1949))
		return STATIC_URL() + "old_map/map_data/1949/" +
			+ zoom + "/" + coord.x + "/" + (Math.pow(2, zoom)-coord.y-1) + ".png";
	else
		return "http://www.maptiler.org/img/none.png"; 
}

function init_map_buttons() {
	$(".map_buttons").click(function(e) {
		if (null != g_current_layer_id) {
			map.removeOverlayMapType(OVERLAY_INDEX);
			g_current_layer_id = null;
		}

		var layer_id = $(e.target).find('input')[0].id;
		show_layer(layer_id);

		if (null == g_current_layer_id) {
			$('#opacity_slider').slider('disable');
		}
	});

	$("#show_full_map").click(function(e) {
		show_bounds(g_current_layer_id);
	});

	$("#zoom_in").click(function(e) {
		map.zoomIn(1);
	});
	$("#zoom_out").click(function(e) {
		map.zoomOut(1);
	});
}


function init_slider() {
	$('#opacity_slider').slider({
		formater: function(value) {
			return '透明度：' + value + "%";
		}
	});
	$("#opacity_slider").on('slide', function(slideEvt) {
		if ((null != g_current_layer_id) && g_current_layer_id in g_layers) {
			g_layers[g_current_layer_id].setOpacity(slideEvt.value/100);
		}
	});
}
