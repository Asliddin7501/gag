$('.a-menu').on('click', function (e) {
    $('.a-menu').removeClass('border-dark');
    $('.a-menu').children().removeClass('font-weight-bold');
    $(this).addClass('border-dark');
    $(this).children().addClass('font-weight-bold');
    if ($(this).children().html() == "Ro'yxat") {
        $('.a-students').show();
        $('.a-baholash, .a-jurnal, .a-vazifa-yuklash').hide();
    } else if ($(this).children().html() == "Baholash") {
        $('.a-baholash').show();
        $('.a-students, .a-jurnal, .a-vazifa-yuklash').hide();
    } else if ($(this).children().html() == "Jurnal") {
        $('.a-students, .a-baholash, .a-vazifa-yuklash').hide();
        $('.a-jurnal').show();
    } else if ($(this).children().html() == "Vazifa yuklash") {
        $('.a-students, .a-baholash, .a-jurnal').hide();
        $('.a-vazifa-yuklash').show();
    }
})