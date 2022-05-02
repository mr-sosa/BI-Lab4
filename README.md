<h3>Instrucciones de instalación</h3>
<p>Dado que en el archivo requirements.txt se encuentran todas las dependencias necesarias, basta con ejecutar el comando <i>pip3 install -r requirements.txt</i></p>

<h3>Instrucciones de despliegue</h3>
<p>Una vez las dependencias han sido instaladas, en la terminal (en la ruta del directorio con los archivos necesarios) ejecutar el comando <i>uvicorn main:app --reload</i></p>

<h3>Funcionamiento de la API</h3>
<p> Parte 1: Predicción</p> 
<p>Se hace POST al servidor en la dirección /predict enviando un JSON con un registro de la base de datos del laboratorio 3. El endpoint recibe este registro y lo integra al pipeline exportado que se encarga de recibir estos datos externos, procesarlos y generar la predicción correspondiente. </p>
<br>
<p> Parte 2: R^2</p> 
<p>Se hace POST al servidor en la dirección /r enviando un JSON con dos elementos. Primero, una lista de registros de la base de datos y, segundo, el valor esperado de la expectativa de vida correspondiente. El pipeline exportado se encarga de procesar cada uno de estos registros de la base de datos recibidos para calcular la expectativa de vida según el modelo exportado. Luego, usando la librería sklearn, se busca calcular el R^2.</p>
