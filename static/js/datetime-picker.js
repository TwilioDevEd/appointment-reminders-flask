$(document).ready(function() {
    $("#time").datetimepicker({
        sideBySide: true,
        format: "MM-DD-YYYY hh:mma"
    });
    $("#timezone-field").chosen();
});
