$(document).ready(function () {
    $("#formPc").submit(function (e) {
        var caracteres = /[!@#$%^&*()_+{}:"<>?|=[\];',./`~]/;
        var nombrePc1 = $("#NombrePc").val();
        var precioPc1 = $("#PrecioPc").val();
        var descripcionPc1 = $("#DescripcionPc").val();
        
        let enviar = true;

        if (nombrePc1.trim().length < 5 || nombrePc1.trim().length > 30) {
            $("#error_nombrePc1").html("El nombre  debe tener entre 5 y 30 caracteres<br>");
            enviar = false;
        } else {
            $("#error_nombrePc1").html("");
        }
        if (descripcionPc1.length < 100) {
            $("#error_descpc1").html("la descripción debe tener minimo 100 caracteres<br>");
            enviar = false;
        } else {
            $("#error_descpc1").html("");
        }
        
        if (descripcionPc1.length > 800) {
            $("#error_descpc2").html("la descripción debe tener maximo 800 caracteres<br>");
            enviar = false;
        } else {
            $("#error_descpc2").html("");
        }
        if (precioPc1 < 0) {
            $("#precio_errorpc1").html("precio invalido: numeros negativos<br>");
          } else {
            $("#precio_errorpc1").html("");
          }
        if (precioPc1 < 1000 ){
            $("#precio_errorpc2").html("El precio no puede ser menos de 1000$<br>")
        } else {
            $("#precio_errorpc2").html("")
        }
        if (caracteres.test(precioPc1) ){
            $("#precio_errorpc3").html("precio invalido: caracteres especiales<br>")
        } else {
            $("#precio_errorpc3").html("")
        }
        if (enviar) {
    
            $("#warnings").html("Enviado");
        } else {
            e.preventDefault();
            $("#warnings").html("Advertencia: Comprueba los errores en el juego");
        }
    });

});