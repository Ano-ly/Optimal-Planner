$(document).ready(function () {
  $('#loginuser').submit(function (event) {
    event.preventDefault();
    const userLoginForm = new FormData(this);
    $.ajax({
      url: 'http://0.0.0.0:5000/api/v1/auth',
      method: 'POST',
      data: userLoginForm,
      dataType: 'json',
      processData: false,
      contentType: false,
      success: function (response) {
        $('#error').text(`Response: ${response}`);
        window.location.href = "/";
      },
      error: function (xhr, err, errStr) {
        $('#error').text(errStr);
      }
    });
  });
});
