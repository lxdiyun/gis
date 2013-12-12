function index_init() {
	// map
	load_map();
	$('#map').fadeOut('fast');
	$('#map').fadeIn('slow');

	Dajaxice.inscription.display_area(Dajax.process, {'area_id':1});
}

var map;
function load_map() {
	var mapOption = { 
		div: '#map', 
		zoom: 12,
		lat: 23.37, 
		lng: 116.71,
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
		zoomControl: true,
		zoomControlOptions: {
			position: google.maps.ControlPosition.TOP_RIGHT
		},
	};
	map = new GMaps(mapOption);
}

var markers = [];
function add_locations(data) {
	var infowindow = new google.maps.InfoWindow();
	var locations = $.parseJSON(data)
		for (var i = 0; i < locations.length; ++i) {
			var loc = locations[i].fields;
			marker = GMaps.prototype.createMarker({
				lat: loc.latitude,
			       lng: loc.longitude,
			       title: loc.name,
			       animation: google.maps.Animation.DROP
			});
			marker.id = locations[i].pk;
			markers.push(marker);
			map.addMarker(marker);
			add_listener(marker, infowindow);
		};
}

function set_all_map(map) {
	for (var i = 0; i < markers.length; i++) {
		markers[i].setMap(map);
	}
}

function clean_all_locations() {
	set_all_map(null);
	markers.length = 0;
}

function add_listener(marker, infowindow) {
	google.maps.event.addListener(marker, 'click', function() {
		infowindow.setContent(marker.title);
		infowindow.open(marker.get('map'), marker);
		display_location(marker.id)
	});
}

function display_location(id) {
	Dajaxice.inscription.display_location(Dajax.process,{'location_id':id});
	$("#sub_location_info" ).fadeOut('fast');
	$("#inscription_info" ).fadeOut('fast');
	$("#sub_location_info" ).empty();
	$("#inscription_info" ).empty();
}
