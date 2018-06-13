/*
	Mi EcmaScript

	consola web
	2+2
	'hola'
	console.log('hola')
	alert('Pop Up!')
*/

/*
* Conversión de tipos
*/

/*console.log('Comentario '+100)
console.log(52+ ' Comentario ')
console.log("37" + 7)
console.log("37" - 7)

console.log(parseInt("37") + 7)
console.log(parseInt("37") - 7)
*/

function saludar(nombre) {
  return "Intro a " + nombre; //Cuando se llama, esta funcion devuelve "Hola " y el nombre que se le ha pasado como argumento.
}

/*Llamar a la función e imprimir por pantalla / mensaje de alerta*/

/*
* Funciones
* var, let y const
* BOM y DOM
* Eventos
*/

(function() {
	/*Mostrar un mensaje de alerta al cargar*/
	//alert('Se cargo la pagina');

	/* Obtener el elemento con el id quote1 */
	//console.log(document.getElementById('quote1'));

	/* Obtener el elemento con el id quotes */
	//console.log(document.getElementById('quotes'));

	/* Obtener los elementos con la etiqueta div y mostrar el contenido*/
	/*var divs = document.getElementsByTagName('div');
	for (i in divs){
		console.log(divs[i]);
	}*/

	/* Obtener los elementos con la clase well */
	/*var wells = document.getElementsByClassName('well');
	for (i in wells){
		console.log(i);
	}*/

	/* Query Selector para los div's con clase well dentro del div con id quotes */
	/*var selector = document.querySelectorAll('div#quotes > div[class="well"]');
	console.log(selector);
	for (i in selector){
		console.log(i)
	}*/

	/*var author = document.querySelectorAll('div#quotes > div[class="well"]');
	for (i of author){
		console.log(i.getAttribute('author'));
	}*/

	/* Mostrar los autores de las frases */
	/*var author = document.querySelectorAll('div#quotes > div[author$="ous"]');
	for (i of author){
		console.log(i.getAttribute('author'));
	}*/

	/* Mostrar el texto de los div's cuyo autor termine en ous */
	/*var author = document.querySelectorAll('div#quotes > div[author$="ous"]');
	for (i of author){
		console.log(i.textContent);
	}*/

	/* Crear un h3 con el autor de cada div con clase well */
	/*var author = document.querySelectorAll('div#quotes > div[class="well"]');
	for (i of author){
		var h3 = document.createElement('h3');
		h3.textContent = i.getAttribute('author');
	}*/

	/* Insertar el h3 antes del p dentro de la cita */
	var author = document.querySelectorAll('div#quotes > div[class="well"]');
	for (i of author){
		console.log(i);
		var h3 = document.createElement('h3');
		h3.textContent = i.getAttribute('author');
		document.insertBefore(h3, i.getElementsByTagName('p'));
	}
	/* Obtener el texto del input con id texto */

	/* Al dar clic en el botón buscar debe ocultar las citas que no contengan el texto ingresado en input (id='texto')*/

})();

