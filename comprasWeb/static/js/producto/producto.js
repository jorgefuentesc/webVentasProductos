$(document).ready(function () {




    $(document).on('click', '#btn_publicar', function () {

        console.log("producto funcionaaa")
        let inp_nombre = $("#prc_nombre").val()
        let inp_precio = $("#prc_precio").val()
        let inp_descripcion = $("#prc_descripcion").val()
        let slug = inp_nombre
        console.log("jeje")
        $.ajax({
            type: "POST",
            url: "publicar_prod/",
            data: {
                "nombre": inp_nombre,
                "precio": inp_precio,
                "descripcion": inp_descripcion,
                "slug": slug,
                'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),

            },
            success: function (response) {
                console.log(response)
                console.log("entro en prod")
            }
        });

    })

})