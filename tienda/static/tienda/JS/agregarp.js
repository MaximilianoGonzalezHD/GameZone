$(document).ready(function () {
    $("#formP").submit(function (e) {
        var caracteres = /[!@#$%^&*()_+{}:"<>?|=[\];',./`~]/;
        var nombrep = $("#NameGameP").val();
        var preciop = $("#PrecioP").val();
        var descripcionp = $("#DescripcionP").val();
        
        let enviar = true;

        if (nombrep.trim().length < 5 || nombrep.trim().length > 15) {
            $("#error_nombrep1").html("El nombre  debe tener entre 5 y 15 caracteres<br>");
            enviar = false;
        } else {
            $("#error_nombrep1").html("");
        }
        if (descripcionp.length < 100) {
            $("#error_desc1").html("la descripción debe tener minimo 100 caracteres<br>");
            enviar = false;
        } else {
            $("#error_desc1").html("");
        }
        
        if (descripcionp.length > 800) {
            $("#error_desc2").html("la descripción debe tener maximo 800 caracteres<br>");
            enviar = false;
        } else {
            $("#error_desc2").html("");
        }
        if (caracteres.test(descripcionp)) {
            $("#error_desc3").html("descripción invalida");
            enviar = false;
        } else {
            $("#error_desc3").html("");
        }
        if (preciop < 0) {
            $("#precio_error1").html("precio invalido: numeros negativos<br>");
          } else {
            $("#precio_error1").html("");
          }
        if (preciop < 1000 ){
            $("#precio_error2").html("El precio no puede ser menos de 1000$<br>")
        } else {
            $("#precio_error2").html("")
        }
        if (caracteres.test(preciop) ){
            $("#precio_error3").html("precio invalido: caracteres especiales<br>")
        } else {
            $("#precio_error3").html("")
        }
        if (enviar) {
    
            $("#warnings").html("Enviado");
        } else {
            e.preventDefault();
            $("#warnings").html("Advertencia: Comprueba los errores en el juego");
        }
    });

});