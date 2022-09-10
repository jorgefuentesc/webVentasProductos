$(document).ready(function () {

    $(document).on('click', '#mdl_registrar', function () {
        console.log("Enlazado correctamente")
        $('#mdl_registro').modal('show');
    })

    $(document).on('click', '#btn-registro', function () {


        let run = $('#inpt_run').val()
        let nombre = $('#inpt_nombre').val()
        let snombre = $('#inpt_snombre').val()
        let teledono = $('#inpt_telefono').val()
        let sapellido = $('#inpt_sapellido').val()
        let direccion = $('#inpt_direccion').val()
        let apellido = $('#inpt_apellido').val()
        let correo_electronico = $('#inpt_correo').val()
        let contrasena = $('#inpt_contrasena').val()
        let fecha_nac = $('#inpt_fecha_nac').val()
        let ciudad = $('#select_ciudad').val()
        let comuna = $('#select_region').val()
        let sexo = $('#select_sexo').val()
        $.ajax({
            type: "POST",
            url: "mdl-registro/",
            data: {
                "run":run,
                "nombre": nombre,
                "snombre":snombre,
                "apellido":apellido,
                "sapellido":sapellido,
                "teledono":teledono,
                "correo_electronico":correo_electronico,
                // "direccion":direccion,
                "fecha_nac":fecha_nac,
                "direccion":contrasena,
                "ciudad":ciudad,
                "comuna":comuna,
                "sexo":sexo,
                'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
            },
            success: function (response) {
                let estado = response['estado']
                // console.log(response)
                console.log(estado)
            }
        });
    })




});