// $(document).foundation();
$('#product-details-tabs').foundation();

function addToCart() {
    return false;
}

$(document).ready(function() {



    var utils = new Utils();

    $(window).scroll(function() {

        if (utils.isElementInView($('.product-grid-block'), false)) {
            $('.js-sticky-add-to-cart').addClass('show-bar');
        } else {
            $('.js-sticky-add-to-cart').removeClass('show-bar');
        }

    });


    $('.dk-form').on('click', '.btn-add-to-cart', function(e) {
        // var pid = $(this).closest('form').find('[name=pid]').val();
        // addProductToCart(pid);
        getCartProducts();

    });



});

$('.back-button').on('click', function() {
    window.history.back();
});