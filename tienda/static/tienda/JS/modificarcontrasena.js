$(document).ready(function () {
    $("#formModC").submit(function (e) {
        var mayusuculamin = /^(?=.*[A-Z])/;
        var mincontra = /[0-9]/;
        var minus = /[a-z]/;
        var actualC = $("#ContrasenaA").val();
        var contrasenar = $("#ContrasenaR").val();
        var confcontrasenar = $("#ConfirmContrasenaR").val();

        let enviar = true;


        if (contrasenar == actualC) {
            console.log("La Contraseña NO debe ser igual a la anterior");
            $("#contrasena_error5").html("La Contraseña NO debe ser igual a la anterior<br>");
            enviar = false;
          } else {
            console.log("La contraseña cumple con la expresión regular");
            $("#contrasena_error5").html("");
          }

        if (!mayusuculamin.test(contrasenar)) {
            console.log("La contraseña no cumple con la expresión regular");
            $("#contrasena_error1").html("La contraseña debe tener mínimo una MAYÚSCULA<br>");
            enviar = false;
          } else {
            console.log("La contraseña cumple con la expresión regular");
            $("#contrasena_error1").html("");
          }

        if (!mincontra.test(contrasenar)) {
            $("#contrasena_error2").html("La contraseña debe tener mínimo un número<br>");
            enviar = false;
        } else {
            $("#contrasena_error2").html("");
        }

        if (!minus.test(contrasenar)) {
            $("#contrasena_errortres").html("La contraseña debe tener mínimo una minúscula<br>");
            enviar = false;
        } else {
            $("#contrasena_errortres").html("");
        }

        if (contrasenar.trim().length < 8 || contrasenar.trim().length > 15) {
            $("#contrasena_error4").html("La contraseña debe tener entre 8 y 15 caracteres<br>");
            enviar = false;
        } else {
            $("#contrasena_error4").html("");
        }

        if (contrasenar !== confcontrasenar) {
            $("#confcontrasena_error").html("Las contraseñas no coinciden<br>");
            enviar = false;
        } else {
            $("#confcontrasena_error").html("");
        }


        if (enviar) {
    
            $("#warnings").html("Enviado");
        } else {
            e.preventDefault();
            $("#warnings").html("Advertencia: Comprueba los errores en el registro");
        }
    });

    
});