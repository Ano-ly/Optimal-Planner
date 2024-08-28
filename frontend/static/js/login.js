window.userId = {};
$(document).ready(function () {
  $('#loginuser').submit(function (event) {
    event.preventDefault();
    const userLoginForm = new FormData(this);
    $.ajax({
      url: 'http://0.0.0.0:5000/api/v1/auth',
      method: 'POST',
      data: userLoginForm,
      processData: false,
      contentType: false,
      success: function (response) {
        wondow.userId = response;
        window.location.href ='/event';
      },
      error: function (xhr, err, errStr) {
        console.log(errStr);
      }
    });
  });
});
