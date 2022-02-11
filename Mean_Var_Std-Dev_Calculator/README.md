Crea un funcion llamada 'calculate() en 'mean_var_std.py' que utilice Numpy para calcular la media, varianza, desviación estandar,
maximon, minimo y suma de filas, columnas y elementos en una matriz de 3x3

El input debe ser una lista que contenga 9 digitos. La funcion debe convertir la lista en un arreglo de Numpy de 3x3, y regresar un diccionario que contenga la media, varianza, desviación estandar, maximo, minimo, suma de los ejes y de la matriz aplanada

El diccionario debera seguir el siguiente formato:

{
    'mean': [axis1, axis2, flattened],
    'variance': [axis1, axis2, flattened],
    'standar deviation': [axis1, axis2, flattened],
    'max': [axis1, axis2, flattened],
    'min': [axis1, axis2, flattened],
    'sum': [axis1, axis2, flattened]
}

Si la lista contiene menos de 9 elementos entonces pasa a la función y debera mostrar un 'ValueError' con el mensaje: "La lista debe de contener minimo 9 digitos". Los valores resultantes deberan ser mostrados
como una lista y no en forma de arreglo.

Por ejemplo:
    'calculate([0,1,2,3,4,5,6,7,8])' debera mostrar los siguientes resultados:

    {
    'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
    'variance': [[6.0, 6.0, 6.0], [0.6666666, 0.6666666, 0.6666666], 6.6666666],
    'standar deviation': [[2.4494897, 2.4494897, 2.4494897], [0.8164965, 0.8164965, 0.8164965], 2.5819888],
    'max': [[6, 7, 8], [2, 5, 8], 8],
    'min': [[0, 1, 2], [0, 3, 6], 0],
    'sum': [[9, 12, 15], [3, 12, 21], 36]
}