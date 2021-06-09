$('.a-menu').on('click', function (e) {
    $('.a-menu').removeClass('border-dark');
    $('.a-menu').children().removeClass('font-weight-bold');
    $(this).addClass('border-dark');
    $(this).children().addClass('font-weight-bold');
    if ($(this).children().html() == "O'qituvchilar") {
        $('.a-oquvchilar, .a-fanlar, .a-dars-jadvallari, .a-elonlar').hide();
        $('.a-oqituvchilar').show();
    } else if ($(this).children().html() == "O'quvchilar") {
        $('.a-oqituvchilar, .a-fanlar, .a-dars-jadvallari, .a-elonlar').hide();
        $('.a-oquvchilar').show();
    } else if ($(this).children().html() == "Fanlar") {
        $('.a-oqituvchilar, .a-oquvchilar, .a-dars-jadvallari, .a-elonlar').hide();
        $('.a-fanlar').show();
    } else if ($(this).children().html() == "Dars jadvallari") {
        $('.a-oqituvchilar, .a-oquvchilar, .a-fanlar, .a-elonlar').hide();
        $('.a-dars-jadvallari').show();
    } else if ($(this).children().html() == "E'lonlar") {
        $('.a-oqituvchilar, .a-oquvchilar, .a-fanlar, .a-dars-jadvallari').hide();
        $('.a-elonlar').show();
    }
})

$('.a-style-button').on('click', function (e){
    if ($(this).html() == "Hafta kunlari") {
        $('.a-guruhlar').hide();
        $('.a-hafta-kunlari').show();
    } else if ($(this).html() == "Guruhlar") {
        $('.a-hafta-kunlari').hide();
        $('.a-guruhlar').show();
    }
})
