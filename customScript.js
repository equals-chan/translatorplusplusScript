var query = this.cells[0];
var tmp;
$.ajax({
    url: 'http://127.0.0.1:9999',
    type: 'post',
    dataType: "json",
    async: false,
    data: {
        'q': query,
    },

    success: function (data) {
        console.log(data)
        tmp = data['det'];
    },
    error:function(XMLHttpRequest, textStatus, errorThrown) {
        console.log("error");
        }
    });
    
this.cells[1] = tmp;