

bicicletas = ['perrona','manuto','chooper']

print(bicicletas)
print(bicicletas[0].title())
print (bicicletas[-1])

bicicletas[0] = 'nueva pe causa'

print( bicicletas)
#agregando elementos al final de una lista
bicicletas.append('nueva bici')
print(bicicletas)

#Insertanndo elementos en una lista
bicicletas.insert(0,'nueva roski')
print(bicicletas)

#Eliminando elementos de una lista
del bicicletas[0]
del bicicletas[1]
print(bicicletas)

colores = ['rojo','verde','azul','amarillo']

# pop elimina elementto de una llista
color_eliminado = colores.pop(1)
print(color_eliminado)

colores.remove('azul')
print(colores)

colores.append('naranja')
colores.append('morado')
colores.append('rosa')
colores.append('cafe')
print(colores)
colores.sort(reverse=True)
print(colores)
