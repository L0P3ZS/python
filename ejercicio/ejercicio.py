# Escribir un programa que pregunte el nombre del usuario en la consola y un número entero
# e imprima por pantalla en líneas distintas 
# el nombre del usuario tantas veces como el número introducido.

# nombre_usuario = input("Cual es tu nombre : ")
# numero = input("escibe un numero : ")

# resultado = nombre_usuario * int(numero)

# print(resultado)


# Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla el nombre completo del usuario tres veces, 
# una con todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula.
# El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.

# nombre_completo = input("puedes escribir tu nombre completo : ")

# resultado_1 = nombre_completo.lower()
# resultado_2 = nombre_completo.upper()
# resultado_3 = nombre_completo.capitalize()

# print(resultado_1)
# print(resultado_2)
# print(resultado_3)



# Escribir un programa que pregunte el nombre del usuario en la consola y
# después de que el usuario lo introduzca muestre por pantalla
# <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas 
# y <n> es el número de letras que tienen el nombre.

# nombre_usuario = input("Me puedes decir tu nombre : ")

# nombre = nombre_usuario.upper()
# numero = len(nombre_usuario)

# print(f'{nombre} tiene {numero} letras')

# Escribir un programa que pida al usuario que introduzca una frase en la consola
# y muestre por pantalla la frase invertida.

# frase = input("puedes escribir una frase : ")


# print(frase[::-1])


# Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal,
# y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.

frac = input("escriba un frase : ")
vo = input("escriva una vocal : ")

print(frac +' '+ vo.upper())