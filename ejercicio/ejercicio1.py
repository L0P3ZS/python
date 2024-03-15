frase = input("puedes escibir un texto y se calcula cuanto se demora en decirla: ")

palabras = frase.split(" ")

palabras_separadas = len(palabras)

persona = palabras_separadas / 2

resultado = int(persona)

dalto_habla =  resultado / 2 * 0.30 

if resultado >= 60:
  print('--------------------------------------------------')
  print('para flaco tampoco te pedi un textamento')
  print('--------------------------------------------------')
else:
    print('--------------------------------------------------')
    print(f'te tardaste en decir : {resultado} segundos la frase')
    print(f'usted dijo {palabras_separadas} palabras')
    print('--------------------------------------------------')
    print(f'dalto tardo {dalto_habla} segundos')

