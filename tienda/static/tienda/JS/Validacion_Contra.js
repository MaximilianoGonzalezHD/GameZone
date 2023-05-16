$(document).ready(function(){
    $("#formCC").submit(function(e){
        e.preventDefault();

        var contrasenar = $("#NuevaContrasena").val();
        var confcontrasenar = $("#ConfirmarContrasena").val();
    
        var mostrarmsj = "Advertencia:";
        let enviar = false;
    
    
        if (contrasenar.trim().length < 4 || contrasenar.trim().length > 10) {
            mostrarmsj += "<br>- La nueva contraseña debe tener entre 4 y 10 caracteres";
            enviar = true;
        }
    
        if (contrasenar != confcontrasenar) {
            mostrarmsj += "<br>- Las contraseñas NO coinciden";
            enviar = true;
        }
        
    
        var letra = contrasenar.trim().charAt(0);
        if (!esMayuscula(letra)) {
            mostrarmsj += "<br>- La primera letra de la contraseña debe ser mayúscula para mas seguridad";
            enviar = true;
            }
        if (enviar) {
            $("#warnings").html(mostrarmsj);
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