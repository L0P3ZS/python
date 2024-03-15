# para crear diccionarios se utiliza dict()

diccionario = dict(nombre = "sebastian", apellido = "lopez", )

#las listas no pueden ser claves y utilizamos fronzenset 

resultado =  {frozenset(["nombre", "apellido"]):"sebas" }
print(diccionario["nombre"])