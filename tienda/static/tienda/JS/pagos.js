$(document).ready(function () {
    $("#formPago").submit(function (e) {
        var rutc = $("#rut").val();
        var rutFormato = /^[0-9]{1,2}\.[0-9]{3}\.[0-9]{3}-[0-9kK]{1}$/;
        let enviar = true;

        if (!rutFormato.test(rutc)) {
          $("#error_rut").html("Rut inválido: Use el siguiente formato xx.xxx.xxx-x");
          enviar = false;
        } else {
          $("#error_rut").html("");
        }
          


          
        if (enviar) {
            $("#warnings").html("Enviado");
        } else {
            e.preventDefault();
            $("#warnings").html("Advertencia: Comprueba los errores en el juego");
        }
    });

});