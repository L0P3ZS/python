#crear un conjunto con set()

conjunto = set(["sebas","lopez"])

#para crear un conjundo detro de otro conjunto se debe utilizar frozenset

conjunto1 = frozenset(["lopez", "sebastian", "erazo"])

conjunto2 = {conjunto1,"alejandra"}

print(conjunto2)

# TEORIA DE CONJUNTOS 

conjunto_a = {3,4,6,53,}
conjunto_b = {3,6,4}

# para verificar si conjunto b es un subconjunto de a se utiliza issubset() tambien esta issuperset
resultado = conjunto_b.issubset(conjunto_a)

# tambien se puede utiliza de la siguiente manera 

resultado = conjunto_b <= conjunto_a

# para verificar si hay algun numero en comun se utiliza isdisjoint() si hay un numero en comun devulve false y si no hay devuelve true

resultado = conjunto_b.isdisjoint(conjunto_a)

print(resultado)