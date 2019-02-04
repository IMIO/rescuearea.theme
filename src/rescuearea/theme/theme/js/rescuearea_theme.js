/*
 * rescuearea_theme.js
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
    $("#searchbox_currentfolder_only").attr("checked", true);
});
