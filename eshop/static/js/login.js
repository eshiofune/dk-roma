function validateForm() {


    if (!validateEmptyString($('#email'))) {
        return false;
    }

    if (!validateEmail($('#email'))) {
        return false;
    }

    if (!validateEmptyPassword($('#password'))) {
        return false;
    }


    return true;
}

function setPasswordIncorrect() {
    toggleValidationError($('#password'), false, 'Password incorrect');
}

$('.js-toggle-password-visibility').on('click', function() {

    var passwordFieldType = $('#password').attr('type') === 'password' ? 'text' : 'password';
    $('#password').attr('type', passwordFieldType);

    $('.js-toggle-password-visibility').toggleClass('password-visible');

});