$(document).ready(function () {
    $("#formX").submit(function (e) {
        var caracteres = /[!@#$%^&*()_+{}:"<>?|=[\];',./`~]/;
        var nombrex = $("#NameGameX").val();
        var preciox = $("#PrecioX").val();
        var descripcionx = $("#DescripcionxX").val();
        
        let enviar = true;

        if (nombrex.trim().length < 5 || nombrex.trim().length > 30) {
            $("#error_nombrex1").html("El nombre  debe tener entre 5 y 30 caracteres<br>");
            enviar = false;
        } else {
            $("#error_nombrex1").html("");
        }
        if (descripcionx.length < 100) {
            $("#error_descx1").html("la descripción debe tener minimo 100 caracteres<br>");
            enviar = false;
        } else {
            $("#error_descx1").html("");
        }
        
        if (descripcionx.length > 800) {
            $("#error_descx2").html("la descripción debe tener maximo 800 caracteres<br>");
            enviar = false;
        } else {
            $("#error_descx2").html("");
        }
        if (preciox < 0) {
            $("#precio_errorx1").html("precio invalido: numeros negativos<br>");
          } else {
            $("#precio_errorx1").html("");
          }
        if (preciox < 1000 ){
            $("#precio_errorx2").html("El precio no puede ser menos de 1000$<br>")
        } else {
            $("#precio_errorx2").html("")
        }
        if (caracteres.test(preciox) ){
            $("#precio_errorx3").html("precio invalido: caracteres especiales<br>")
        } else {
            $("#precio_errorx3").html("")
        }
        if (enviar) {
    
            $("#warnings").html("Enviado");
        } else {
            e.preventDefault();
            $("#warnings").html("Advertencia: Comprueba los errores en el juego");
        }
    });

});