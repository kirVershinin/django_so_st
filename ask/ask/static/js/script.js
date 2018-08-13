
$(document).ready(function(){

	


	$('#signup').on('click', function(){
		$('#overlay').fadeIn(300);
		$('#auth').fadeIn(300);
		$("#authContent").html('<object data="http://127.0.0.1:8000/signup/">');
	})

	$('#login').on('click', function(){
		$('#overlay').fadeIn(300);
		$('#auth').fadeIn(300);
		$("#authContent").html('<object data="http://127.0.0.1:8000/login/">');
	})

	$('#closeAuth').on('click', function(){
		$('#overlay, #auth').fadeOut(300);
	})
	$('input[type="submit"]').on('click', function(){
		window.parent.$('#overlay, #auth').fadeOut(300);
	})

})
