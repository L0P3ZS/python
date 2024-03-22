# Iterar dicicionarios

dicicionario = {
    'nombre' : 'Sebastian',
    'apellido' : 'Lopez',
    'edad' : 19 
}

# Esta es es la forma de iterar un dicionario con la clave  
for key in dicicionario :
    key 
    print(f'la clave es : {key}')

# Esta es es la forma de iterar un dicionario con items() para obtener la clave y el valor
for datos in dicicionario.items():
    key = datos[0]
    valor = datos[1]
    print(f'la clave es : {key} y valor es : {valor} ')
