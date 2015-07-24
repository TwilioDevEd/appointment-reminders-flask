$(document).ready(function() {
    $("#time").datetimepicker({
        sideBySide: true,
        format: "MM-DD-YYYY HH:mma"
    });
    $("#timezone-field").chosen();
});
