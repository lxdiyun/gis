$('#sublocation_list li a').click( function(e){
	e.preventDefault();
	if (! $(this).hasClass('active')) {
		$('#sublocation_list li.active').removeClass('active');
		$(this).parent().addClass('active');
		id = $(this).attr('id');
		Dajaxice.inscription.display_sublocation(Dajax.process,{'sublocation_id':id});
		$("#inscription_info" ).fadeOut('fast');
		$("#inscription_info" ).empty();
	}
});
