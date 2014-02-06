function index_init() {
	// map
	load_map();
	$('#map').fadeOut('fast');
	$('#map').fadeIn('slow');

	Dajaxice.inscription.display_area(Dajax.process, {'area_id':1});
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
	$("#photos_or_sublocation_info" ).fadeOut('fast');
	$("#photos_or_sublocation_info" ).empty();
}
