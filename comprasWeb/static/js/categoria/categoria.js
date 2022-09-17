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
})