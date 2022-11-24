$(document).ready(function () {

    $(document).on('click', '#loginInicio', function () {
        console.log("Enlazado correctamente Inicio sesion")
        $('#mdl_inicio_sesion').modal('show');
    })

    // $(document).on('click', '#btn-logggin', function () {



    //     let correo_electronico = $('#loginEmail').val()
    //     let contrasena = $('#loginPassword').val()
    //     console.log(correo_electronico,contrasena,"oww")
    //     $.ajax({
    //         type: "POST",
    //         url: "login/",
    //         data: {
            
    //             "correo_electronico":correo_electronico,
    //             "contrasena":contrasena,
    //             // "direccion":direccion,
    //             'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
    //         },
    //         success: function (response) {
    //             // let estado = response['estado']
    //             // console.log(response)
    //             console.log("worrrr")
    //         }
    //     });
    // })




});