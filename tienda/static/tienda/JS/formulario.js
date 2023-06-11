$(document).ready(function () {
    $("#formR").submit(function (e) {
        var mayusuculamin = /^(?=.*[A-Z])/;
        var mincontra = /[0-9]/;
        var minus = /[a-z]/;
        var correor = $("#email").val();
        var nombrer1 = $("#NombreR").val();
        var nombreopc = $("#NameOp").val();
        var contrasenar = $("#ContrasenaR").val();
        var confcontrasenar = $("#ConfirmContrasenaR").val();

        let enviar = true;

        if (nombrer1.trim().length < 5 || nombrer1.trim().length > 15) {
            $("#usuario_error").html("El nombre de usuario debe tener entre 5 y 15 caracteres");
            enviar = false;
        } else {
            $("#usuario_error").html("");
        }

        var letra = nombreopc.trim().charAt(0);
        if (!esMayuscula(letra)) {
            $("#error_nombre").html("La primera letra de su nombre debe ser en mayúscula<br>");
            enviar = false;
        } else {
            $("#error_nombre").html("");
        }

        if (!mayusuculamin.test(contrasenar)) {
            console.log("La contraseña no cumple con la expresión regular");
            $("#contraseña_error1").html("La contraseña debe tener mínimo una MAYÚSCULA<br>");
            enviar = false;
          } else {
            console.log("La contraseña cumple con la expresión regular");
            $("#contraseña_error1").html("");
          }

        if (!mincontra.test(contrasenar)) {
            $("#contraseña_error2").html("La contraseña debe tener mínimo un número<br>");
            enviar = false;
        } else {
            $("#contraseña_error2").html("");
        }

        if (!minus.test(contrasenar)) {
            $("#contraseña_errortres").html("La contraseña debe tener mínimo una minúscula<br>");
            enviar = false;
        } else {
            $("#contraseña_errortres").html("");
        }

        if (contrasenar.trim().length < 8 || contrasenar.trim().length > 15) {
            $("#contraseña_error4").html("La contraseña debe tener entre 8 y 15 caracteres<br>");
            enviar = false;
        } else {
            $("#contraseña_error4").html("");
        }

        if (contrasenar !== confcontrasenar) {
            $("#confcontraseña_error").html("Las contraseñas no coinciden<br>");
            enviar = false;
        } else {
            $("#confcontraseña_error").html("");
        }

        if (correor.trim().length > 30) {
            $("#correo_error").html("El correo no puede tener más de 30 caracteres<br>");
            enviar = false;
        } else {
            $("#correo_error").html("");
        }

        if (correor.trim().length < 4  ||correor.trim().length > 30 ) {
            $("#correo_error").html("Correo inválido");
            console.log("Correo inválido");
            enviar = false;
        } else {
            $("#correo_error").html("");
        }

        if (enviar) {
    
            $("#warnings").html("Enviado");
        } else {
            e.preventDefault();
            $("#warnings").html("Advertencia: Comprueba los errores en el formulario");
        }
    });

    function esMayuscula(letra) {
        if (letra == letra.toUpperCase()) {
            return true;
        } else {
            return false;
        }
    }
});