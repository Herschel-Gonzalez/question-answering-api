// Crea una instancia de XMLHttpRequest
var xhr = new XMLHttpRequest();

// Define la función de manejo de la respuesta
xhr.onload = function() {
  if (xhr.status >= 200 && xhr.status < 400) {
    // La solicitud fue exitosa
    var response = JSON.parse(xhr.responseText);
    console.log(response);
  } else {
    // La solicitud falló
    console.error('Error en la solicitud: ', xhr.status);
  }
};

// Define la función de manejo de errores
xhr.onerror = function() {
  console.error('Error en la solicitud');
};

// Define los datos que deseas enviar en el cuerpo de la solicitud
var data = {
  question: 'donde vivo?',
  context: 'Hola mi nombre es Herschel y vivo en michoacan',
};

// Configura la solicitud POST
xhr.open('POST', 'http://127.0.0.1:5000/api/answer', true);
xhr.setRequestHeader('Content-Type', 'application/json');

// Envía la solicitud con los datos
xhr.send(JSON.stringify(data));
