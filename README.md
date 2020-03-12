# Competencia Doble Rendija

En este experimento se tratara de evidenciar el efecto de la doble rendija, para esto, contaremos con tres pruebas; 
la primera tendra una rendija, la segunda dos y la tercera tres. Se realizara además las respectivas simulaciones 
de manera probabilistica. Para las simulaciones se uso Python, el archivo que contiene el codigo esta adjunto en este repositorio

A continuación, se verán los materiales, construcción y realización del experimento

## Materiales 
- Carton paja
- Papel aluminio
- Silicona
- Lasér

## Construcción experimento 

1. Se corta en un trozo de carton paja tres ventanas en las cuales posteriormente se colocaran las rendijas.
2. Se realizan los cortes correspondientes en el papel aluminio, en este veremos las diferentes rendijas. Luego
de tenerlas, se pegan en el carton paja previamente cortado
3. Se pega un carton paja detrás de las rendijas, en este se podrán ver los patrones de interferencia que generan
las rendijas
4. Para mayor comodidad, se colocan dos pequeños trozos como base de el carton que tiene las ventanas para que 
pueda ser movido hacia las diferentes rendijas.

## Ejecución

Para realizar el experimento, se toma el lasér y se apunta en dirección a la ventana de la rendija que se prefiera,
teniendo en cuenta que este logre cubrir todas las rendijas para obtener un mejor patrón de interferencia.
 
## Explicación

En este experimento se trata de comprender la influencia que tienen los diferentes universos entre ellos, la
interferencia que se genera en los fotones es causada porque ellos interactuan cin sus versiones o historias 
en los universos ajenos a ella; paar poderlo entender, lo estudiamos con probabilidades, con ellas podemos ver 
que tan probable es que una particula tome uno u otro camino, de esta misma manera, podemos ver en  que puntos
o blancos se van a concentrar en mayor o menor medida

# Pruebas

En esta sección se mostrarán 4 puntos por cada experimento a las rendijas. Se podrá ver la foto del experimento, el
analísis el grafo, la simulación en Python, y finalmente, la matriz de estados y el estado final. Para estas
simulaciones, se tomo como estándar el número de clicks, el cual fue 2.

### *Experimento*
![slits2](https://user-images.githubusercontent.com/60012037/76479390-a2497e80-63d9-11ea-89ff-b59073c86d27.jpg)
### *Grafo*
![2slits_grafo](https://user-images.githubusercontent.com/60012037/75947828-b0464f00-5e6f-11ea-8850-72f84f0e7fec.png)
### *Simulación*
![2slits_sim](https://user-images.githubusercontent.com/60012037/75947836-b63c3000-5e6f-11ea-9d06-7865433d6687.png)
![newslits](https://user-images.githubusercontent.com/60012037/76480047-9a8ad980-63db-11ea-8051-9ebeb09b7c56.png)
### *Gráfica de probabilidades*
![probabilities](https://user-images.githubusercontent.com/60012037/76480066-a70f3200-63db-11ea-9d7c-192929f0cabd.png)


## Ejecución de la simulación
Para ejecutar la simulación, es necesario descargar el archivo que se encuentra adjunto en este repositorio; luego de descargarlo,
puedes ejecutarlo con la función expRendijas, en ella se solicitaran 3 parámetros los cuales son: slits(rendijas), targets(blancos),
clicks(cantidad de clicks). Dicha función imprimirá la matriz de probabilidades, el vector final luego de la cantidad ingresada de clicks, y la confirmación de que cada estado tiene salida 1.

