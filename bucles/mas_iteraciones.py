frutas = ["manzana", "pera", "papaya", "melon", "sandia", "fresa", "mora", "uva"]

cadena = "hola sebas como estas "

# Para saltar un valor en un bucle se hace con la sentencia continue dentro de condicion 
for fruta in frutas:
    if fruta == "pera":
      continue 
    print(f'la fruta que me gusta: {fruta}' )
    
print("---------------------------------------")   

# Y para que el bucle se detenga se utiliza break

for fruta in frutas:
  print(f'la fruta que me voy a comer : {fruta}')
  if fruta == "melon":
    break

print("------------------------------------------")

# Recorer un cadena 

for letra in cadena.split():
    print(letra)
 