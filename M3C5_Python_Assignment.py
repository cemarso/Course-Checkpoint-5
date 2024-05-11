# Ejercicio práctico 1
# Crear un bucle for de Python

fruits = ['Melon', 'Orange', 'Lemon', 'Banana']
for fruit in fruits:
        print(f'I love ' + fruit)


# Ejercicio práctico 2
# Crear una función de Python llamada suma que tome 3 argumentos 
# y devuelva la suma de los 3.

def sum(a, b, c):
        return a + b + c
print(sum(1, 2, 3))


# Ejercicio práctico 3
# Crear una función lambda con la misma funcionalidad 
# que la función de suma que acaba de crear.

sum = lambda a, b, c: a + b + c
print(sum(1, 2, 3))


# Ejercicio práctico 4
# Utilizando la siguiente lista y variable,
# determine si el valor de la variable coincide o no con un valor de la lista. 
# *Sugerencia, si es necesario, utilice un bucle for in y el operador in.
# nombre = 'Enrique'
# lista_nombre = 'Jessica', 'Paul', 'George', 'Henry', 'Adán'

nombre = 'Enrique'
lista_nombre = 'Jessica', 'Paul', 'George', 'Henry', 'Adán'

if nombre in lista_nombre:
        print(f'{nombre} está en la lista')
else:
        print(f'{nombre} no está en la lista')