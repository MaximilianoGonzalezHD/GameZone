$(document).ready(function () {
    $("#formPago").submit(function (e) {
        var rutFormato = /^\d{1}\.\d{3}\.\d{3}-[\dkK]{1}$/;
        var correo = $("#correo").val();
        var rut = $("#rut").val();
        var emailFormato = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        let enviar = true;

        if (!rutFormato.test(rut)) {
            $("#error_rut").html("RUT inválido. Utiliza el formato x.xxx.xxx-x");
            enviar = false;
          } else {
            $("#error_rut").html("");
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