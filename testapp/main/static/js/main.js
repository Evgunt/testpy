$(document).ready(function () {
    // Фильтрация Категорий и подкатегорий при Update
    let url = window.location.href;
    if (url.indexOf('recordUpdate') !== -1) {
        let typeId = $('#id_type').val(); // id Типа
        let categoryId = $('#id_category').val(); // id категории
        // Показ скрытых select
        $("#id_category").parent().parent().show().css('display', 'flex');
        $("#id_subcategory").parent().parent().show().css('display', 'flex');
        // Получение категории по Типу
        $.ajax({
            url: "/getCategories",
            data: {'typeId': typeId},
            success: function (data) {
                $("#id_category option").fadeOut(0); // Скрыть все option
                $.each(data, function (index, item) {
                    $('#id_category option[value="' + item.id + '"]').fadeIn(0); // Показываем нужные
                });
            }
        });
        // Получаем подкатегории по категории
        $.ajax({
            url: "/getSubcategories",
            data: {'categoryId': categoryId},
            success: function (data) {
                $("#id_subcategory option").fadeOut(0);
                $.each(data, function (index, item) {
                    $('#id_subcategory option[value="' + item.id + '"]').fadeIn(0);
                });
            }
        });
    }
    // Функция для фильтрации категорий
    $('#id_type').change(function () {
        let typeId = $(this).val(); // id типа
        // Получение категорий по типу
        $.ajax({
            url: "/getCategories",
            data: {'typeId': typeId},
            success: function (data) {
                // Скрыть все option
                $("#id_subcategory option").fadeOut(0);
                $("#id_category option").fadeOut(0);
                // Если select скрыт, то показать
                if ($("#id_category").parent().parent().is(':hidden')) {
                    $("#id_category").parent().parent().fadeToggle(400).css('display', 'flex');
                }
                // Скрыть подкатегории
                if (!$("#id_subcategory").parent().parent().is(':hidden'))
                    $("#id_subcategory").parent().parent().fadeToggle(400).css('display', 'flex');
                // Убрать выбранные значения
                $('#id_category option').prop('selected', false);
                $('#id_subcategory option').prop('selected', false);
                $.each(data, function (index, item) {
                    // Показать нужные категории
                    $('#id_category option[value="' + item.id + '"]').fadeIn(0);
                });
            }
        });
    });
    // Функция для фильтрации подкатегорий
    $('#id_category').change(function () {
        let categoryId = $(this).val(); // id категории
        // получение подкатегорий по категории
        $.ajax({
            url: "/getSubcategories",
            data: {'categoryId': categoryId},
            success: function (data) {
                $("#id_subcategory option").fadeOut(0); // Скрываем все option
                // Если select скрыт, то показать
                if ($('#id_subcategory').parent().parent().is(':hidden'))
                    $('#id_subcategory').parent().parent().fadeToggle(400).css('display', 'flex');
                // Убрать выбранные значения
                $('#id_subcategory option').prop('selected', false);
                $.each(data, function (index, item) {
                    // Показать нужные категории
                    $('#id_subcategory option[value="' + item.id + '"]').fadeIn(0);
                });
            }
        });
    });
    // Функция для показа модального окна удаления
    $('.pre_delete_record').click(function () {
        let id = $(this).attr('data-id');
        let typeDelete = $(this).attr('data-type');
        $('#delete_button').attr('data-type', typeDelete)
        $('#delete_button').attr('data-id', id)
        $('.modal-record').fadeIn(300);
    });
    // Функция для закрытия модального окна
    $('.modal-record').click(function (event) {
        /* Проверяем, что клик не внутри самого модального окна
         Чтобы при клике по оверлею вне окна — закрыть,
         а при клике внутри окна — не закрывать. */
        if (!$(event.target).closest('.modal-record-content').length) {
            $('.modal-record').fadeOut(300);
        }
    });
    // Отдельный обработчик для кнопки "Отмена"
    $('#cancel_delete').click(function () {
        $('.modal-record').fadeOut(300);
    });
    // Функция удаления записи
    $('#delete_button').click(function () {
        let id = $(this).attr('data-id');
        let typeDelete = $(this).attr('data-type');
        let CSRF = $(this).parent().find('input').val();
        switch (typeDelete) {
            case 'record':
                $.ajax({
                    url: "/recordDelete/" + id,
                    type: 'POST',
                    headers: {
                        'X-CSRFToken': CSRF  // CSRF-токен
                    },
                    success: function () {
                        // Перезагружаем страницу, для результата
                        window.location.reload();
                    }
                });
                break;
            case 'type':
                $.ajax({
                    url: "/deleteType/" + id,
                    type: 'POST',
                    headers: {
                        'X-CSRFToken': CSRF  // CSRF-токен
                    },
                    success: function () {
                        // Перезагружаем страницу, для результата
                        window.location.reload();
                    }
                });
                break;
            case 'category':
                $.ajax({
                    url: "/deleteCategory/" + id,
                    type: 'POST',
                    headers: {
                        'X-CSRFToken': CSRF  // CSRF-токен
                    },
                    success: function () {
                        // Перезагружаем страницу, для результата
                        window.location.reload();
                    }
                });
                break;
            case 'subcategory':
                $.ajax({
                    url: "/deleteSubcategory/" + id,
                    type: 'POST',
                    headers: {
                        'X-CSRFToken': CSRF  // CSRF-токен
                    },
                    success: function () {
                        // Перезагружаем страницу, для результата
                        window.location.reload();
                    }
                });
                break;
            case 'status':
                $.ajax({
                    url: "/deleteStatus/" + id,
                    type: 'POST',
                    headers: {
                        'X-CSRFToken': CSRF  // CSRF-токен
                    },
                    success: function () {
                        // Перезагружаем страницу, для результата
                        window.location.reload();
                    }
                });
                break;
        }
    });
    // Функции фильтрации select для record на главной
    $('#type').change(function () {
        let typeId = $(this).val();
        if (typeId === '0') {
            $("#subcategory").parent().fadeIn(300);
            $("#category option").fadeIn(300);
            $('#category option[value="0"]').prop('selected', true);
            $('#subcategory option[value="0"]').prop('selected', true);
        } else {
            $.ajax({
                url: "/getCategories",
                data: {'typeId': typeId},
                success: function (data) {
                    // Скрыть все option
                    $('#category option').fadeOut(0);
                    $('#category option[value="0"]').fadeIn(0);
                    // Скрыть подкатегории
                    $("#subcategory").parent().fadeOut(400);
                    $('#subcategory option').fadeIn(0);
                    // Убрать выбранные значения
                    $('#category option[value="0"]').prop('selected', true);
                    $('#subcategory option[value="0"]').prop('selected', true);
                    $.each(data, function (index, item) {
                        // Показать нужные категории
                        $('#category option[value="' + item.id + '"]').fadeIn(0);
                    });
                }
            });
        }
    });
    $('#category').change(function () {
        let categoryId = $(this).val();
        if (categoryId === '0') {
            $("#subcategory").parent().fadeIn(300);
            $('#subcategory option[value="0"]').prop('selected', true);
        } else {
            $.ajax({
                url: "/getSubcategories",
                data: {'categoryId': categoryId},
                success: function (data) {
                    // Скрыть все option
                    $('#subcategory option').fadeOut(0);
                    $('#subcategory option[value="0"]').fadeIn(0);
                    $("#subcategory").parent().fadeIn(300);
                    // Убрать выбранные значения
                    $('#subcategory option[value="0"]').prop('selected', true);
                    $.each(data, function (index, item) {
                        // Показать нужные категории
                        $('#subcategory option[value="' + item.id + '"]').fadeIn(0);
                    });
                }
            });
        }
    });
    $('#filter-button').click(function(){
        $('.hidden').toggle(300);
    });
});