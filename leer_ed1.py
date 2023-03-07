import utiles as ut

ut.tit(' Leyendo un archivo ', clr=ut.Ci, clrB=ut.NeB, simb='&')

# Creamos la instancia objeto "archivo" con la clase open
archivo = open("aposentos.txt", 'r')

# Usamos el método read() para guardar el contenido en "contenido"
contenido = archivo.read()

# Cerramos el objeto archivo.
archivo.close()

# Obtenemos el nombre del archivo con name.
nombre = archivo.name

print("El contenido de", nombre.upper(), "es:")
print()
ut.prcl(contenido)

input()
