$(document).ready(function () {
    $("#formM").submit(function (e) {
        var caracteres = /[!@#$%^&*()_+{}:"<>?|=[\];',./`~]/;
        var nombrev1 = $("#NameGameV").val();
        var preciov1 = $("#PrecioV").val();
        var descripcionv1 = $("#DescripcionV").val();
        
        let enviar = true;

        if (nombrev1.trim().length < 5 || nombrev1.trim().length > 30) {
            $("#error_nombrev1").html("El nombre  debe tener entre 5 y 30 caracteres<br>");
            enviar = false;
        } else {
            $("#error_nombrev1").html("");
        }
        if (descripcionv1.length < 100) {
            $("#error_descripcionv1").html("la descripción debe tener minimo 100 caracteres<br>");
            enviar = false;
        } else {
            $("#error_descripcionv1").html("");
        }
        
        if (descripcionv1.length > 800) {
            $("#error_descripcionv2").html("la descripción debe tener maximo 800 caracteres<br>");
            enviar = false;
        } else {
            $("#error_descripcionv2").html("");
        }
        
        if (preciov1 < 0) {
            $("#error_preciov1").html("precio invalido: numeros negativos<br>");
          } else {
            $("#error_preciov1").html("");
          }
        if (preciov1 < 1000 ){
            $("#error_preciov2").html("El precio no puede ser menos de 1000$<br>")
        } else {
            $("#error_preciov2").html("")
        }
        if (caracteres.test(preciov1) ){
            $("#error_preciov3").html("precio invalido: caracteres especiales<br>")
        } else {
            $("#error_preciov3").html("")
        }
        if (enviar) {
    
            $("#warnings").html("Enviado");
        } else {
            e.preventDefault();
            $("#warnings").html("Advertencia: Comprueba los errores en el juego");
        }
    });

});