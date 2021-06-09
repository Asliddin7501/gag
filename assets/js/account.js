$('.a-menu').on('click', function (e) {
    $('.a-menu').removeClass('border-dark');
    $('.a-menu').children().removeClass('font-weight-bold');
    $(this).addClass('border-dark');
    $(this).children().addClass('font-weight-bold');
    if ($(this).children().html() == "Homeworks") {
        $('.a-fanlar, .a-dars-jadvali, .a-elonlar').hide();
        $('.a-homeworks').show();
    } else if ($(this).children().html() == "Fanlar") {
        $('.a-homeworks, .a-dars-jadvali, .a-elonlar').hide();
        $('.a-fanlar').show();
    } else if ($(this).children().html() == "Dars jadvali") {
        $('.a-homeworks, .a-elonlar, .a-fanlar').hide();
        $('.a-dars-jadvali').show();
    } else if ($(this).children().html() == "E'lonlar") {
        $('.a-homeworks, .a-fanlar, .a-dars-jadvali').hide();
        $('.a-elonlar').show();
    }
})