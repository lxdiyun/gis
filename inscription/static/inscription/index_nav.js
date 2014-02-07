$('#area_list li a').click( function(e){
	e.preventDefault();
	if (! $(this).parent().hasClass('active')) {
		$('#area_list li.active').removeClass('active');
		$(this).parent().addClass('active');
		id = $(this).attr('id');
		Dajaxice.inscription.display_area(Dajax.process,{'area_id':id});

		$("#area_or_location_info" ).fadeOut('fast');
		$("#photos_or_sublocation_info" ).fadeOut('fast');
		$("#area_or_location_info" ).empty();
		$("#photos_or_sublocation_info" ).empty();
		clean_all_markers();
	}
});
