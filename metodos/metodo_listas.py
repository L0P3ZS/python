#len() cuenta la cantidad de elementos de una lista

#set conjuntos = set([23, "sebas"])

#dupla = (23,"sebas")
#diccionario = {
 #'nombre':'sebas',
 #'edad' : 23   
#}

#dir devuelve el conjunto de nombres asociados al objeto incluido como argumento.

lista = [5, 23, 3, True, 3]

#append() agrega un elemento a la lista 
lista.append("camilo")
#insert() agrega un elemento a la lista en el indiice especificado  
lista.insert(2, "loro")

#extend agrega  varios elementos a la lista 
lista.extend(["juan","erazo"])

#pop() elimina un elemento de una lista, pide indice y devuleve el valor y si quieres eliminar el ultimo elemento pones -1 
lista.pop(0)

#remove() remueve un elemento de una lista, pide valor 
lista.remove("loro")

#clear() elimina todos los elementos de la lista
# lista.clear()

#sort() ordena una lista de forma ascedente a desendente solo funciona si no tiene cadenas de txt
# y si colocamos el parametro reverse=true lo ordena en reversa
# lista.sort()

#reverse() invierte los elementos de una lista
lista.reverse()

# para llamar una lista se untiliza asi variable[indice]

print(lista[0])