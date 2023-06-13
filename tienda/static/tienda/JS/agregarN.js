$(document).ready(function () {
    $("#formN").submit(function (e) {
        var caracteres = /[!@#$%^&*()_+{}:"<>?|=[\];',./`~]/;
        var nombren1 = $("#NameGameN").val();
        var precionn1 = $("#PrecioN").val();
        var descripcionn = $("#DescripcionN").val();
        
        let enviar = true;

        if (nombren1.trim().length < 5 || nombren1.trim().length > 15) {
            $("#error_nombren1").html("El nombre  debe tener entre 5 y 15 caracteres<br>");
            enviar = false;
        } else {
            $("#error_nombren1").html("");
        }
        if (descripcionn.length < 100) {
            $("#error_descn1").html("la descripción debe tener minimo 100 caracteres<br>");
            enviar = false;
        } else {
            $("#error_descn1").html("");
        }
        
        if (descripcionn.length > 800) {
            $("#error_descn2").html("la descripción debe tener maximo 800 caracteres<br>");
            enviar = false;
        } else {
            $("#error_descn2").html("");
        }
        if (caracteres.test(descripcionn)) {
            $("#error_descn3").html("descripción invalida<br>");
            enviar = false;
        } else {
            $("#error_descn3").html("");
        }
        if (precionn1 < 0) {
            $("#precio_errorn1").html("precio invalido: numeros negativos<br>");
          } else {
            $("#precio_errorn1").html("");
          }
        if (precionn1 < 1000 ){
            $("#precio_errorn2").html("El precio no puede ser menos de 1000$<br>")
        } else {
            $("#precio_errorn2").html("")
        }
        if (caracteres.test(precionn1) ){
            $("#precio_errorn3").html("precio invalido: caracteres especiales<br>")
        } else {
            $("#precio_errorn3").html("")
        }
        if (enviar) {
    
            $("#warnings").html("Enviado");
        } else {
            e.preventDefault();
            $("#warnings").html("Advertencia: Comprueba los errores en el juego");
        }
    });

});