En este proyecto se realizaran calculos y visualizaciones de datos sobre examinaciones medicas utilizando matplotlib, seaborn y pandas. Los valores del dataset
fueron colectados durante examinaciones medicas

Las filas del dataset representa a los pacientes y las columnas representa la información sobre las mediciones del cuerpo, resultados de pruebas de sangre y estilos de vida.

Se utilizara el dataset para explorar la relación entre las enfermedades cardiacas, mediciones corporales, marcadores de sangre y estilos de vida.

Archivo: medical_examination.csv

| Feature                     | Variable Type       | Variable      | Value Type                                       |
|:---------------------------:|:-------------------:|:-------------:|:------------------------------------------------:|
| Age                         | Objective Feature   | age           | int (days)                                       |
| Height                      | Objective Feature   | height        | int (cm)                                         |
| Weight                      | Objective Feature   | weight        | float (kg)                                       |
| Gender                      | Objective Feature   | gender        | categorical code                                 |
| Systolic blood pressure     | Examination Feature | ap_hi         | int                                              |
| Diastolic blood pressure    | Examination Feature | ap_lo         | int                                              |
| Cholesterol                 | Examination Feature | cholesterol   | 1: normal, 2: above normal, 3: well above normal |
| Glucose                     | Examination Feature | gluc          | 1: normal, 2: above normal, 3: well above normal |
| Smoking                     | Subjective Feature  | smoke         | binary                                           |
| Alcohol intake              | Subjective Feature  | alco          | binary                                           |
| Physical activity           | Subjective Feature  | active        | binary                                           |
| Pres or abs of card disease | Target Variable     | cardio        | binary                                           |


Ejercicios:

-Crear un grafico similar a 'examples/Figure_1.png', donde se muestra el conteo de resultados buenos y malos de las variables 'cholesterol', 'gluc', 'alco', 'active' y 'smoke' para
los pacientes con cardio=1 y cardio=0 en diferntes paneles

Utiliza los datos para completar los siguientes ejercicios en 'medical_data_visualizer.py':

-Agrega un columna de 'overwieght' para determinar si la persona tiene sobrepeso, primero calcula si IMC dividiendo su peso (kg) entre su altura (m) elevada al cuadrado. si el valor
es > 25 entonces la persona tiene sobrepeso. Utiliza el valor 0 para indicar que no tiene sobrepeso y valor 1 para sobrepeso.

-Normaliza los datos utilizando siempre el 0 para indicar algo bueno y 1 para malo. Si el valor de 'cholesterol' o 'gluc' es 1 entonces se indicara como 0, pero si este es mayor que uno,
se indicara como 1

-Convierte los datos en un formato largo y crea un grafico que muestre el conteo de valores (value_counts) por categoria utilizando seabron's 'caplot()'. El dataset debera estar dividido
por 'Cardio' por lo que habra un grafico por cada valor de cardio. El grafico debera ser como el de 'examples/Figure_2.png'

-Limpia los datos. Extrae los segmentos de pacientes que representen datos incorrectos:
    *La presion diastolica es mayor que la sistolica(Manten los datos correctos con `(df['ap_lo'] <= df['ap_hi'])`)
    *Su altura es menor que el percentil 2.5(Manten los datos correctos con `(df['height'] >= df['height'].quantile(0.025))`)
    *Su altura es mayor que el percentil 97.5 (Manten los datos correctos con `(df['height'] <= df['height'].quantile(0.975))`)
    *Su peso es menor que el percentil 2.5 (Manten los datos correctos con `(df['weight'] >= df['weight'].quantile(0.025))`)
    *Sup peso es mayor que el percentil 97.5 (Manten los datos correctos con `(df['weight'] <= df['weight'].quantile(0.975))`)

-Crea una matriz de correlación utilizando el dataset. Grafica la matriz de correlación utilizando seaborn's 'heatmap()'. Enmascara el triangulo superior. El grafico debera ser como el de
'examples/Figure_2.png'

Cada vez que una variable este como 'None', Asegurate que se indique con el codigo correcto