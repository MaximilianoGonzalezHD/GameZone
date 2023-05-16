 //se espera a que la pagina cargue por completo
 $(document).ready(function(){
    // se le agrega la fucion click al boton
    $("#Consulta").click(function(){
        //tipo de metodo a aplicar al webservice
        $.get("https://rickandmortyapi.com/api/character",function(data){
            //for* recorremos el archivo json
            $.each(data.results,function(i,item){
                //cada elemento del json lo muestro en la tabla
                $("#tablaC").append(
                    "<tr id=resultado>"+
                    "<td>"+item.id+"</td>"+
                    "<td><img  src='"+item.image +"' alt='sin foto'></td>"+
                    "<td>"+item.name+"</td>"+
                    "<td>"+item.status +"</td>"+
                    "<td>"+item.species+"</td>"+
                    "<td>"+item.gender+"</td>"+
                    "</tr>"
                );
            });
        })
    });
$("#limpiar").click(function(){
    $("#resultado").remove();
})
})
