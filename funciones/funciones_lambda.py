#creando una funcion con lambda 
mutiplicar = lambda x : x*2
print(mutiplicar(4))

# creando funcion que si es par o no

numero = [1,34,55,6,4]

# def es_par(num):
#   if num%2==0 :
#       return True
  
# numeros_par = filter(es_par,numero)

# numeros pares con lambda
numeros_par = filter(lambda numeros : numeros%2 == 0,numero)


print(list(numeros_par))