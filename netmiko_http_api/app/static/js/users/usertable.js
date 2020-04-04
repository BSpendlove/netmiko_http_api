$(document).ready(function(){
    var form = $('#tbl-viewallusers');

    $.ajax({
        url: "/api/users",
        dataType: 'json',
        contentType: 'application/json',
        type: 'get',
        cache:false,
        success: function(request){
            var event_data = '';
            console.log(request);
            $.each(request.data, function(index, value){
                event_data += '<tr>';
                event_data += '<td>'+value.username+'</td>';
                event_data += '<td>'+value.password+'</td>';
                event_data += '<td>';
                event_data += '<div class="form-group float-right">';
                event_data += '<a href="' + value.id + '" class="btn btn-sm btn-warning" title="View Device"><i class="far fa-edit" aria-hidden="true"></i></a>';
                event_data += '<a href="#" class="btn btn-sm btn-danger" title="Delete Device"><i class="fas fa-window-close" aria-hidden="true"></i></a>'
                event_data += '</div>';
                event_data += '</td>';
                event_data += '</tr>';
            });
            form.append(event_data);
        },
        error: function(d){
            //console.log(d);
            alert("404. Please wait until the File is Loaded.");
        }
    });

    
});