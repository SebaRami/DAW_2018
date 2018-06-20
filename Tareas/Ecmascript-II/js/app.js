function onSuccessXml(data){
	//var citas = data.getElementByTagName('cita');
	//console.log(data);
	$(data).find('cita').each(function(){
      var author = $(this).find('autor').text();
      var texto = $(this).find('texto').text();
      $("<div></div>").attr('class','well').attr('author', author).append($("<p></p>").html(texto)).appendTo("#quotes");
      //$("<div></div>").addClass('well').attr('author', author).html(texto).appendTo("#quotes");
    });

}

function cargarCita(){
	$.ajax({
		type: "GET",
		url: "data/citas.xml",
		contentType: "text/xml",
		success: onSuccessXml,
	})
}

function busquedaFiltro(){
	text = document.getElementById('texto').value;
	var divs = document.querySelectorAll('div#quotes > div');
	for (div of divs){
		var content = div.textContent;
		if(content.includes(text)){
			div.classList.add('mostrar');
			div.classList.remove('ocultar');
		}
		else{
			div.classList.add('ocultar');
			div.classList.remove("mostrar");
		}
	}
}


(function(){
	document.getElementById('buscar').onclick = busquedaFiltro;
	document.getElementById('texto').onkeyup = busquedaFiltro;
	$('#texto').on('keyup', busquedaFiltro);
	cargarCita();
})();
