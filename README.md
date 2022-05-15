# DAMAVIS CHALLENGE

## DESCRIPCIÓN DEL RETO

Este proyecto es un reto de la empresa Damavis. Tenemos un tablero de 
mxn celdas. En el tablero se encuentra una serpiente que ocupa s
celdas con s<=m y s<=n, todas sus celdas son adyacentes vertical
u horizontalmente. Los movimientos disponibles son L, R, D y U (left, rigth,
down y up). Debemos realizar una función que, dada una profundidad, devuelva
el número de posibles movimientos que puede realizar la serpiente de tamaño
igual a dicha profundidad. La serpiente se mueve con todas las celdas
de manera simultánea por lo que puede tomar la cabeza el valor de la cola.
No está permitido que la serpiente tome un valor fuera del tablero ni 
tampoco se interseccione con una de sus casillas (que no sea la cola).

## SOLUCIÓN PLANTEADA

Emplearemos Python para resolver el problema. Para resolver este reto 
vamos a emplear la técnica de Divide y Vencerás (Divide-and-Conquer). 
Es un algoritmo que trata de dividir el problema en subproblemas para 
poder tratarlos de una manera más sencilla. 

Haremos uso de una función recursiva que se llamará a sí misma con distinos
movimientos de la serpiente (L, R, D o U). El caso base de nuestra función
es cuando depth=0 pues habremos llegado al maximo de caminos deseados, 
si llegamos a este caso quiere decir que hemos encontrado un camino viable
por lo que devolveremos un 1 indicando un camino encontrado. En el caso
recursivo llamamos la funcion cada uno con un movimiento distinto posible y
decrementando en uno la profundidad (depth)

Dado que se deben emplear arrays vamos a trabajar con Tuplas, que es un 
tipo de array en python.
