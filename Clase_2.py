#Comprender como se manejan los arreglos de python
#Realizar operaciones basicas u añlgunas avanzadas para resolver problemas de la vida cotidiana
#Aplicas logica d eprogramacion para manipular datos almacenados en arreglos

#Conceptos fundamientales del tema de los arreglos

# 1. Validar que es un arreglo
#Es una lista o una forma de estructura de datos que almacena una secuencia de elementos de forma consecutiva
#Cada elemento se puede encontrar por medio de su indice 

# 2. Uso comun de los vectores/Arreglos/lista/Array
#Guarda datos relacionados como nombres numeros o resultados
#Tambien sirve para procesar grandes cantidades de informacion, esto de forma ordenada

# 3. Operaciones basicas
#Crear y llenar
#Recorrer y manipular datos
#Realizar busquedas, filtros y transformaciones 

#Ejemplos detallados
#Crear y mostrr un vector

vector = []

#Vamos a llenar el vector por valores definidos por el usuario

for i in range(5):
    valor = int(input(f"Ingrese un numero para la posicion {i}:"))
    vector.append(valor) #.Append es una funcion de python que recibe como parametro lo que se va agregar a un arreglo 
    #y lo coloca en la ultima posicion disponible
print(f"Arreglo ingresado: {vector}")

##################################################################################

#recorrer y modificar valores dentro de un vector arreglo / array

vector2 = [10, 20, 30, 40,50]
#lo recorremos o iteramos, haciendo alguna operacion en cada uno de los elementos que contiene el arreglo. La mejor
#Herramienta para hacerlo, es un ciclo for

print("Elementos originales")
for i in range(len(vector2)):
    #Len cuenta cuantos elementos tiene el vector y se usa para hacer algunas operaciones basicas

    print(f"indice {i}: {vector2[i]}")
    #[n] hace referencia a la posicion donde esta cada elemento del arreglo


#Modificar cada elemento multiplicandolo por 2 
for i in range(len(vector2)):
    vector2[i] *= 2

#Volvemos a imprimirlo
print("Vector luego de ser modificado: ")
for i in range(len(vector2)):
    print("Indice {i}: {vector2[i]}")


##################################################################################
    

