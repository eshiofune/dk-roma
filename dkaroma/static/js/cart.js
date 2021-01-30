$(document).ready(function() {

    const CART_VALUES = {
        max: 999
    };


    $('.js-quantity').inputFilter(function(value) {
        if (parseInt(value) < 1) {
            return 1;
        }
        return /^\d*$/.test(value); // Allow digits only, using a RegExp
    });

    $('.js-quantity').focusout(function() {

        if ($(this).val() == '' || parseInt($(this).val()) < 1) {
            $(this).val('1');
        }
    });



    $('.js-increment').click(function(e) {

        var quantityInput = $(this).siblings('.js-quantity');

        if (parseInt(quantityInput.val()) == CART_VALUES.max) {
            return;
        }
        quantityInput.val(parseInt(quantityInput.val()) + 1);

    });

    $('.js-decrement').click(function(e) {

        var quantityInput = $(this).siblings('.js-quantity');
        if (parseInt(quantityInput.val()) - 1 < 1) {
            return;
        }
        quantityInput.val(parseInt(quantityInput.val()) - 1);

    });


    $(function() {
        var cartItems = $('#cart--items-form .js-cart-items').find('.js-cart-row').length;

        if (cartItems == 0) {

            $('.shopping-cart-product-number ').addClass('hide');
            $('.shopping-cart-empty').removeClass('hide');
        } else {
            $('.page-layout-right').removeClass('hide');
            $('#cart--items-form').removeClass('hide');
        }

    });


});