jQuery(document).ready(function(){

$(".btn-delete").on('click', function(){
	
	var registration = $(this);

	deleteRegistration(registration);

	function deleteRegistration(param) {
    swal({
      title: "Etes vous sûre?", 
      text: "Ete vous sûre de vouloir supprimer cette saisie?", 
      type: "warning",
      showCancelButton: true,
      closeOnConfirm: false,
      confirmButtonText: "Oui, Supprimer!",
      confirmButtonColor: "#ec6c62"
    }, function() {
       $.ajax({
	        	type: "POST",
	        	url: "/admission/registration/delete/",
	        	data: {pk: registration.attr("data-pk")},
	        	success: function(response){
              // registration.remove();
            }
      })
      .done(function(data) {
        swal("Supprimé", "La saisie a été supprimée!", "succès");
        // element.closest('tr').remove();
      })
      .error(function(data) {
        swal("Oops", "Nous n'avons pas pu se connecté au serveur!", "Erreur");
      });
    });


  }

});

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

});