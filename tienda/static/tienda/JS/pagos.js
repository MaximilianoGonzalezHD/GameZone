$(document).ready(function () {
    $("#formPago").submit(function (e) {
        var rutc = $("#rut1").val();
        var rutc1 = $("#rut2").val();
        var correo = $("#correo").val();
        var rutFormato = /^[0-9]{1,2}\.[0-9]{3}\.[0-9]{3}-[0-9kK]{1}$/;
        var emailFormato = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        let enviar = true;

  
          if(!rutFormato.test(rutc)){
            $("#error_rut1").html("Rut invalido");
            enviar = false;
          } else {
            $("#error_rut1").html("");
          }
          if(!rutFormato.test(rutc1)){
            $("#error_rut2").html("Rut invalido");
            enviar = false;
          } else {
            $("#error_rut2").html("");
          }

          if (!emailFormato.test(correo)) {
            $("#error_correo").html("Correo electrónico inválido");
            enviar = false;
          } else {
            $("#error_correo").html("");
          }

          
        if (enviar) {
            $("#warnings").html("Enviado");
        } else {
            e.preventDefault();
            $("#warnings").html("Advertencia: Comprueba los errores en el juego");
        }
    });

});