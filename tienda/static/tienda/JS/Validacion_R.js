$(document).ready(function(){
$("#formR").submit(function(e){
    var caracteres = "!@#$%^&*()_+{}:\"<>?|=[];',./`~";
    var mayusuculamin = /^(?=.*[A-Z])/;
    var correor = $("#emailR").val();
    var nombrer = $("#NombreR").val();
    var nombreus =  $("#NameOp").val();
    var contrasenar = $("#ContrasenaR").val();
    var confcontrasenar = $("#ConfirmContrasenaR").val();

    var mostrarmsj = "Advertencia:";
    let enviar = false;

    if (nombrer.trim().length < 4 || nombrer.trim().length > 15) {
        mostrarmsj += "<br>- El nombre debe tener entre 4 y 15 caracteres";
        enviar = true;
    }

    if (!mayusuculamin.test(contrasenar)){
        mostrarmsj += "<br>- La contraseña debe tener minimo una MAYUSCULA"
        enviar = true;
    }
    if (!caracteres.test(confcontrasenar)){
        mostrarmsj +="<br>- La contraseña debe tener minimo un caracter especial para mas seguridad"
    }

    if (contrasenar.trim().length < 4 || contrasenar.trim().length > 20) {
        mostrarmsj += "<br>- La contraseña debe tener entre 4 y 20 caracteres";
        enviar = true;
    }

    if (contrasenar != confcontrasenar) {
        mostrarmsj += "<br>- Las contraseñas NO coinciden";
        enviar = true;
    }
    

    var letra = nombreus.trim().charAt(0);
    if (!esMayuscula(letra)) {
        mostrarmsj += "<br>- La primera letra del Nombre debe ser en MAYUSCULA";
        enviar = true;
        }

    if (nombreus.trim().length < 3 || nombreus.trim().length > 8){
        mostrarmsj += "<br>- El nombre debe tener entre 3 y 8 caracteres"
        enviar = true;
    }
    if (enviar) {
        $("#warnings").html(mostrarmsj);
        e.preventDefault();
    }
    else {
        $("#warnings").html("Enviado");
        
    }
})

function esMayuscula(letra) {
    if (letra == letra.toUpperCase()) {
        return true;
    }
    else {
        return false;
    }
}


})