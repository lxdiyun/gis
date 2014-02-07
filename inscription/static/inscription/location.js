var add_marker_hook = null;

function location_init() {
	// map
	g_bounds_min_zoom = 15;
	load_map();
	$('#map').fadeOut('fast');
	$('#map').fadeIn('slow');

	if (null != add_marker_hook) {
		add_marker_hook();
	}
}
