$(document).ready(function () {

    jQuery(document).on('click', '#mdl_registrar', function () {
        console.log("Enlazado correctamente")
        jQuery('#mdl_registro').modal('show');
    })

    jQuery(document).on('click', '#btn-registro', function () {


        let run = $('#inpt_run').val()
        let nombre = $('#inpt_nombre').val()
        let apellido = $('#inpt_apellido').val()
        let fecha_nac = $('#inpt_fecha_nac').val()
        let usuario = $('#inpt_usuario').val()
        let contrasena = $('#inpt_contrasenna').val()
        let correo_electronico = $('#inpt_correo').val()
        let telefono = $('#inpt_telefono').val()
        let ciudad = $('#select_ciudad').val()
        let comuna = $('#select_comuna').val()
        let direccion = $('#inpt_direccion').val()
        let sexo = $('#select_sexo').val()
        $.ajax({
            type: "POST",
            url: "mdl-registro/",
            data: {
                "run":run,
                "nombre": nombre,
                "apellido":apellido,
                "usuario":usuario,
                "contrasena":contrasena,
                "correo_electronico":correo_electronico,
                "telefono":telefono,
                "ciudad":ciudad,
                "comuna":comuna,
                "fecha_nac":fecha_nac,
                "sexo":sexo,
                // "direccion":direccion,
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