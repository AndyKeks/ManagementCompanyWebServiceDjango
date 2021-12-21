$(document).on('submit','#send_msg',function(e){
        e.preventDefault();
        $.ajax({
          type:'POST',
          url:$("#send_msg").prop('action'),
          data:{
              content:$('#content').val(),
              csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
          },
          success: function(json){
             if (json.status === 'OK'){
                alert('added');
                $("#messages_area").append('<div class="alert alert-success">'+
                    '<p class="lead">'+ json.user +'</p>' +
                    '<p>' + json.content + '</p><br>' +
                    '<kbd>' + json.date + '</kbd></div>');
            }
            else{
                alert('сообщение не отправлено');
            }
          },
          error : function(xhr,errmsg,err) {
                console.log(xhr.status + ": " + xhr.responseText);
                }
        });
    document.getElementById('content').value = '';
});