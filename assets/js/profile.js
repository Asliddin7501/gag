$('.a-menu').on('click', function (e) {
    $('.a-menu').removeClass('border-dark');
    $('.a-menu').children().removeClass('font-weight-bold');
    $(this).addClass('border-dark');
    $(this).children().addClass('font-weight-bold');
    if ($(this).children().html() == "Notification") {
        $('.a-classes, .a-dars-jadvali').hide();
        $('.a-bildirishnomalar').show();
    } else if ($(this).children().html() == "Classes") {
        $('.a-bildirishnomalar, .a-dars-jadvali').hide();
        $('.a-classes').show();
    } else if ($(this).children().html() == "Dars jadvali") {
        $('.a-classes, .a-bildirishnomalar').hide();
        $('.a-dars-jadvali').show();
    }
})