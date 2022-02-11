Se analizara un dataset del promedio de los cambios en el nivel del mar a nivel global desde 1880. Se utilizaran los datos para predecir el cambio en
el nivel del mar hasta el año 2050.

Utiliza los datos para completar las siguientes tareas:

    -Utiliza pandas para importar los datos del archivo 'epa-sea-level.csv'

    -Utiliza matplotlib para crear un grafico de dispersion utilizando la columna 'Year' como eje X y la columna 'CSIRO Adjusted Sea Level' como eje Y.

    -Utiliza la funcion linregress de scipy.stats para obetener la pendiente y la interseccion de la linea que mejor se ajuste. Traza la liena que mejor se
    ajuste sobre el grafico de dispersion. Haz que la linea pase por el año 2050 para predecir el aumento del nivel de mar en 2050.

    -Grafica una nueva linea que mejor se ajuste utilizando los datos del año 2000 a travez de los años mas recientes del dataset. Haz una liena que tambien vaya
    a travez del año 2050 para predecir el aumento del nivel del mar en 2050 si el ritmo de aumento sigue siendo el mismo desde el año 2000.

    -El eje X debera ser 'Year', el eje Y debera ser 'Sea Level(inches)', y el titulo 'Rise in Sea Level'.