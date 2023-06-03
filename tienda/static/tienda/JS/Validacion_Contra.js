$(document).ready(function(){
    $("#formCC").submit(function(e){
        
        var caracteres = "!@#$%^&*()_+{}:\"<>?|=[];',./`~";
        var mayusuculamin = /^(?=.*[A-Z])/;
        var contrasenar = $("#NuevaContrasena").val();
        var confcontrasenar = $("#ConfirmarContrasena").val();
    
        var mostrarmsj = "Advertencia:";
        let enviar = false;
    
        if(!caracteres.test(contrasenar)){
            mostrarmsj += "<br>- La contraseña debe tener minimo un caracter especial"
        }
        if(!mayusuculamin.test(contrasenar)){
            mostrarmsj += "<br>- La contraseña debe tener minimo una letra en MAYUSCULA"
            enviar = true;
        }
        if (contrasenar.trim().length < 4 || contrasenar.trim().length > 10) {
            mostrarmsj += "<br>- La nueva contraseña debe tener entre 4 y 20 caracteres";
            enviar = true;
        }
    
        if (contrasenar != confcontrasenar) {
            mostrarmsj += "<br>- Las contraseñas NO coinciden";
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