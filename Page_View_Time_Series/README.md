En este proyecto se visualizara una serie de datos de tiempo utilizando un grafico lineal, de barras y de cajas. Se utilizara Pandas, Matplotlib y Seaborn
para visualizar el dataset que contiene el numero de vistas de la pagina por día en el foro defreeCodeCamp.org del 2016-05-09 al 2019-12-03. La visualizacion
de los datos ayudaran a entender el patron de las visitas e identificar el crecimiento mensual y anual.

Utiliza los datos para completar las siguientes tareas:

    -Utiliza pandas para importar los datos de 'fcc-forum-pageviews.csv'. coloca la columna 'date' como el index

    -Limpia los datos sacando los dias cuando las visitas de la pagina esten en el 2.5% en el top del dataset o dentro del 2.5% del fondo

    -Crea la funcion draw_line_plot que utilice Matplotlib para dibujar un grafico lineal similar a 'example/Figure_1.png'. El titulo debe ser 'Daily freeCodeCamp Forum
    Page Views 5/2016-12/2019'. El titulo del eje x debera ser 'Date' y el eje y 'Page Views'.

    -Crea la funcion draw_bar_plot para dibujar un grafico de barras similar a 'example/Figure_2.png'. Debera mostrar el promedio de las vistas de la pagina por mes agruapdo por año
    La leyenda debera mostrar los meses y mostrar el titulo 'Months'. En el grafico el eje x seran 'Years' y en el eje Y seran 'Average Page Views'.

    -Crea la funcion draw_box_plot que utilice Seaborn para dibujar dos graficos de cajas adyacentes similar a 'example/Figure_3.png'.