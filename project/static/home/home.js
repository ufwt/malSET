function uploadFile() {
    var fn = $('#file_upload').val();
    var filename = fn.match(/[^\\/]*$/)[0]; // remove C:\fakename
    alert(filename);
}

$(document).ready(function () {
    $('#file_upload').on("change", function(){ uploadFile(); });
});