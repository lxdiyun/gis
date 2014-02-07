function index_init() {
	// map
	g_bounds_min_zoom = 15;
	load_map();
	$('#map').fadeOut('fast');
	$('#map').fadeIn('slow');

	Dajaxice.inscription.display_area(Dajax.process, {'area_id':1});
}

function display_location_with_marker(marker) {
	display_location(marker.id);
}

function add_locations(data) {
	var locations = $.parseJSON(data);
	var infowindow = new google.maps.InfoWindow();

	for (var i = 0; i < locations.length; ++i) {
		var loc = locations[i].fields;
		add_marker(locations[i].pk, 
			   loc.latitude, 
			   loc.longitude, 
			   loc.name,
			   display_location_with_marker,
			   infowindow)
	};
}

function display_location(id) {
	Dajaxice.inscription.display_location(Dajax.process,{'location_id':id});
	$("#photos_or_sublocation_info" ).fadeOut('fast');
	$("#photos_or_sublocation_info" ).empty();
}
