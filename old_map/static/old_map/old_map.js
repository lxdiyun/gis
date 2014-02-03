var MAP_1949_ID = 0

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
	$('#map').fadeOut('fast');
	$('#map').fadeIn('slow');


	init_map_button();
	init_slider();

	show_1949_map();
}

function show_1949_map() {
	map.map.overlayMapTypes.insertAt(MAP_1949_ID, map_1949);
	map_1949.setOpacity($('#map_opacity_slider').slider('getValue')/100);
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
		return "/website/static/old_map/map_data/1949/" +
			+ zoom + "/" + coord.x + "/" + (Math.pow(2, zoom)-coord.y-1) + ".png";
	else
		return "http://www.maptiler.org/img/none.png"; 
}

function init_map_button() {
	$("#1949_toggle").click(function() {
	if (! $(this).hasClass('active')) {
		show_1949_map();
	}
	else {
		map.map.overlayMapTypes.removeAt(MAP_1949_ID);
	}
});
}


function init_slider() {
	$('#map_opacity_slider').slider({
		formater: function(value) {
			return '透明度：' + value + "%";
		}
	});
	$("#map_opacity_slider").on('slide', function(slideEvt) {
		map_1949.setOpacity(slideEvt.value/100);
	});
}
