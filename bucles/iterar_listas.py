# Iterar lista con for in

#TAMBIEN SIRVE CON TUPLAS

animales = ["gato" ,"perro", "gallo", "caballo", "vaca"]
numeros = [1,2,3,4,5]

for animal in animales:
    if animal == "gato":
        print(animal)
        
# Para iterar dos listas se puede utilizar  zip()

for animal,numero in zip(animales,numeros):
  print(f"iterando la lista 1 : {animal}")
  print(f"iterando la lista 2 : {numero}")

#Tabla de multiplicar 


numeros = [1,2,3,4,5,6,7,8,9,10]

tabla = input("pedes escribir el numero : ")

for numero in numeros:
    num = numero * int(tabla)
    print(f"{numero} x {tabla} = {num} ")
    

# determina el rango en un bucle for

for item in range(10):
  print(item)
   
   
 #Recorer una lista con su indice    
 
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f'el indice de la lista es : {indice} y el valor es : {valor}') 
    
    