$(document).ready(function () {
    $("#formCC").submit(function (e) {
        var mayusuculamin = /^(?=.*[A-Z])/;
        var mincontra = /[0-9]/;
        var minus = /[a-z]/;

        var act_contrasena = $("#ContrasenaA").val();
        var contrasenar = $("#NuevaContrasena").val();
        var confcontrasenar = $("#ConfirmarContrasena").val();

        let enviar = true;


        if (!mayusuculamin.test(contrasenar)) {
            console.log("La contraseña no cumple con la expresión regular");
            $("#error_nueva_contrasena1").html("La contraseña debe tener mínimo una MAYÚSCULA<br>");
            enviar = false;
          } else {
            console.log("La contraseña cumple con la expresión regular");
            $("#error_nueva_contrasena1").html("");
          }

        if (!mincontra.test(contrasenar)) {
            $("#error_nueva_contrasena2").html("La contraseña debe tener mínimo un número<br>");
            enviar = false;
        } else {
            $("#error_nueva_contrasena2").html("");
        }

        if (!minus.test(contrasenar)) {
            $("#error_nueva_contrasena3").html("La contraseña debe tener mínimo una minúscula<br>");
            enviar = false;
        } else {
            $("#error_nueva_contrasena3").html("");
        }

        if (contrasenar.trim().length < 8 || contrasenar.trim().length > 15) {
            $("#error_nueva_contrasena4").html("La contraseña debe tener entre 8 y 15 caracteres<br>");
            enviar = false;
        } else {
            $("#error_nueva_contrasena4").html("");
        }
        if (contrasenar == act_contrasena) {
            $("#error_nueva_contrasena5").html("La contraseña es igual a la anterior<br>");
            enviar = false;
        } else {
            $("#error_nueva_contrasena5").html("");
        }

        if (contrasenar !== confcontrasenar) {
            $("#error_confirmar_contrasena1").html("Las contraseñas no coinciden<br>");
            enviar = false;
        } else {
            $("#error_confirmar_contrasena1").html("");
        }



        if (enviar) {
    
            $("#warnings").html("Enviado");
        } else {
            e.preventDefault();
            $("#warnings").html("Advertencia: Comprueba los errores en el formulario");
        }
    });

});