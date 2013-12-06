$('#sub_location_list a').click( function(e){
	e.preventDefault();
	if (! $(this).hasClass('active')) {
		$('#sub_location_list a.active').removeClass('active');
		$(this).addClass('active');
		id = $(this).attr('id');
		Dajaxice.inscription.display_sub_location(Dajax.process,{'sub_location_id':id});
		$("#inscription_info" ).empty();
	}
});
