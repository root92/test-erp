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


});


