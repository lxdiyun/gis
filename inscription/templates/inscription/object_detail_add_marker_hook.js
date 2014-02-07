add_marker_hook = function () {
	add_marker({{ location.id }},
		   {{ location.latitude }},
		   {{ location.longitude }},
		   "{{ location.name }}"
		  );
	zoom_to_show_all_markers();
};
