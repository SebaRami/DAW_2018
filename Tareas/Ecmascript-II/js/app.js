(function(){
	document.getElementById('buscar').onclick = function(){
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

	function OnSuccess(data){
		//var citas = data.getElementByTagName('cita');
		console.log(data);

	}

	$.ajax({
		type: 'GET',
		url: 'data/citas.xml',
		contentType: "text/xml",
		dataType: "xml",
		succes: OnSuccess,
	})
	
})();