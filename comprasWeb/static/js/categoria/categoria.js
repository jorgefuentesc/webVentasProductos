$(document).ready(function () {
    console.log("funciona categoria")

    $(document).on('click', '#btn_ctg_publicar', function () {
        console.log("inside categoria")
        let gte_nombre = $("#ctg_nombre").val()
        let ctg_fecha_act = $("#ctg_fecha_act").val()
        $.ajax({
            type: "POST",
            url: "crear_categoria",
            data: {
                "gte_nombre": gte_nombre,
                "ctg_fecha_act": ctg_fecha_act,
                'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
            },
            success: function (response) {
                console.log("response = ", response)
            }
        });
    })

    $(document).on('click','#btn-registrar-categoria', function() {

        let ctg_nombre = $("#ctg_nombre").val()
        let ctg_fecha = $("#ctg_fecha").val()
        // let fecha_creacion = new Date.now()
        console.log("fecha de ahoraaaa")
        $.ajax({
            type: "POST",
            url: "http://localhost:8000/nueva_categoria/",
            data: {
                "nombre":ctg_nombre,
                "fecha":ctg_fecha,
                'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
            },
            success: function (response) {
                console.log("works")
            }
        });
        
    })
})