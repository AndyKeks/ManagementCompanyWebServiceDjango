$(document).on('submit','#set_work',function(e){
        e.preventDefault();
        $.ajax({
          type:'POST',
          url:$("#set_work").prop('action'),
          data:{
              csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
          },
          success: function(json){
             if (json.status === 'OK'){
                alert('on work');
                $("#messages_area").append('<div class="alert alert-success">'+
                    '<p class="lead">'+ json.user +' <b>(менеджер)</b></p>' +
                    '<code>' + json.content + '</code><br>' +
                    '<kbd>' + json.date + '</kbd></div>');
                $("#set_work").hide();
            }
            else{
                alert('сообщение не отправлено');
            }
          },
          error : function(xhr,errmsg,err) {
                console.log(xhr.status + ": " + xhr.responseText);
                }
        });
});