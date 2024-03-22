# para crear una funcion simple
# def saludar():
#     print("hola sebas como estas")
    


# for item in range(10):
#    item = saludar()
   
# funcion con parametros 

# def  nombre(nombre):
    
#  print(f"hola {nombre}")
  
# nombre("maria")

#Funcion que retorna multiples valores

def contraseña_aleatoria(num):
    caracter = "asjkdoefvd"
    numero_entero = str(num)
    num = int(numero_entero[0])
    
    c1 = num - 2
    c2 = num 
    c3 = num - 4 
    contraseña = f"{caracter[c1]}{caracter[c2]}{caracter[c3]}{num*2}"
    return contraseña

contra = contraseña_aleatoria(2)  

print(contra)


