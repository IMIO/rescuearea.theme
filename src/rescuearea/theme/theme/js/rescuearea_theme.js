/*
 * rescuearea_theme.js
 * Copyright (C) 2018 AuroreMariscal <aurore@affinitic.be>
 *
 * Distributed under terms of the LICENCE.txt license.
 */
$(document).ready(function() {
    $( ".tab-fieldset" ).click(function() {
        id = $(this).attr('id').replace('tab_fieldset-', '');
        $(".tab-fieldset").removeClass('active').addClass('desactived');
        $(this).removeClass('desactived').addClass('active');
        $(".content-fieldset").hide();
        $("#" + id).show();
    });
});
