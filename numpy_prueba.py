import numpy as np
l = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
n1 = np.array(l)
print(n1)
print(type(n1))

# Principale atributos
print(n1.ndim)
print(n1.shape)
print(n1.size)
print(n1.dtype)

# Acceso a los elementos
print(n1[1,2]) # primer número es y (renglon), segundo numero es x (columna)
print(n1 * 2)
print(np.linalg.norm(n1)) #normalizar datos
print(n1.T) # transforma los renglones en columnas
print(n1.transpose()) # transforma los renglones en columnas

print(n1.mean())
print(n1[0, :].mean()) # promedio del renglon 0
print(n1[:, 0].mean()) # promedio de la columna 0
"""    Ecuaciones    
x +2y = 1    
3x + 5y = 2"""
ecuaciones = [[1,2],[3,5]]
np_ecuaciones = np.array(ecuaciones)
resultados = np.array([1,2])
print(np.linalg.solve(np_ecuaciones, resultados))