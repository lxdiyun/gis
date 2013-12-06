$('#inscription_list a').click( function(e){
	e.preventDefault();
	if (! $(this).hasClass('active')) {
		$('#inscription_list a.active').removeClass('active');
		$(this).addClass('active');
		id = $(this).attr('id');
		Dajaxice.inscription.display_inscription(Dajax.process,{'inscription_id':id});
	}
});
