$('#area_list li a').click( function(e){
	e.preventDefault();
	if (! $(this).parent().hasClass('active')) {
		$('#area_list li.active').removeClass('active');
		$(this).parent().addClass('active');
		id = $(this).attr('id');
		Dajaxice.inscription.display_area(Dajax.process,{'area_id':id});

		$("#location_info" ).fadeOut('fast');
		$("#sub_location_info" ).fadeOut('fast');
		$("#inscription_info" ).fadeOut('fast');
		$("#location_info" ).empty();
		$("#sub_location_info" ).empty();
		$("#inscription_info" ).empty();
		clean_all_markers();
	}
});
