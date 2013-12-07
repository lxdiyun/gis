$('#sub_location_list li a').click( function(e){
	e.preventDefault();
	if (! $(this).hasClass('active')) {
		$('#sub_location_list li.active').removeClass('active');
		$(this).parent().addClass('active');
		id = $(this).attr('id');
		Dajaxice.inscription.display_sub_location(Dajax.process,{'sub_location_id':id});
		$("#inscription_info" ).fadeOut('fast');
		$("#inscription_info" ).empty();
	}
});
