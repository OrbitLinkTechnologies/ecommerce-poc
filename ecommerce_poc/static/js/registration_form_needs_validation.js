// Example starter JavaScript for disabling form submissions if there are invalid fields
(() => {
  'use strict';

  // Fetch all the forms we want to apply custom Bootstrap validation styles to
  const forms = document.querySelectorAll('.registration_form_needs_validation');

  // Loop over them and prevent submission
  Array.prototype.slice.call(forms).forEach((form) => {
    form.addEventListener('submit', (event) => {
      if (!form.checkValidity()) {
        event.preventDefault();
        event.stopPropagation();
      }
      form.classList.add('was-validated');
    }, false);
  });
})();

// for some reason we can't get JQuery to work, so we just use vanilla JavaScript

var check_if_passwords_match = function() {
  if (document.getElementById('registerPassword').value == document.getElementById('registerRepeatPassword').value) {
    document.getElementById('registerPasswordMessage').innerHTML = 'Your passwords match.';
    document.getElementById('registerRepeatPasswordMessage').innerHTML = 'Your passwords match.';
  } else {
    document.getElementById('registerPasswordMessage').innerHTML = 'Your passwords do not match.';
    document.getElementById('registerRepeatPasswordMessage').innerHTML = 'Your passwords do not match.';
  }
}