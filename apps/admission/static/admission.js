jQuery(document).ready(function(){

  var loadForm = function () {
    var btn = $(this);
    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-registration .modal-content").html("");
        $("#modal-registration").modal("show");
      },
      success: function (data) {
        $("#modal-registration .modal-content").html(data.html_form);
      }
    });
  };

  var saveForm = function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
          console.log("deleted")
          $("#modal-registration").modal("hide");
        }
        else {
          $("#modal-registration .modal-content").html(data.html_form);
        }
      }
    });
    return false;
    
  };

  $(".btn-delete").on("click", loadForm);
  $(".js-delete-registration-form").on("submit", saveForm);

  // payement fees delete link in payment app
  // load the delete confirmation form
  $(".fee-delete").on("click", loadForm);
  // Delete the object
  $(".js-delete-fee-form").on("submit", saveForm);

  
  // Adding datepicker for dates
  $( function() {
    $( "#datepicker" ).datepicker($.datepicker.regional[ "fr" ]);
  } );

  // Add datatable to registration page
  $('#registration-table, #inscription-table, #student-table').DataTable(
      {
        "language": {
          "sProcessing":     "Traitement en cours...",
          "sSearch":         "Rechercher&nbsp;:",
            "sLengthMenu":     "Afficher _MENU_ &eacute;l&eacute;ments",
          "sInfo":           "Affichage d'&eacute;l&eacute;ments _START_ &agrave; _END_ sur _TOTAL_ &eacute;l&eacute;ments",
          "sInfoEmpty":      "Affichage de l'&eacute;l&eacute;ment 0 &agrave; 0 sur 0 &eacute;l&eacute;ment",
          "sInfoFiltered":   "(filtr&eacute; de _MAX_ &eacute;l&eacute;ments au total)",
          "sInfoPostFix":    "",
          "sLoadingRecords": "Chargement en cours...",
            "sZeroRecords":    "Aucun &eacute;l&eacute;ment &agrave; afficher",
          "sEmptyTable":     "Aucune donn&eacute;e disponible dans le tableau",
          "oPaginate": {
            "sFirst":      "Premier",
            "sPrevious":   "Pr&eacute;c&eacute;dent",
            "sNext":       "Suivant",
            "sLast":       "Dernier"
          },
          "oAria": {
            "sSortAscending":  ": activer pour trier la colonne par ordre croissant",
            "sSortDescending": ": activer pour trier la colonne par ordre d&eacute;croissant"
          }
        }

    } );
  


  
});


