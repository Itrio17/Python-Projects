En este reto analizaremos datos demograficos utilizando Pandas. Se brindara un dataset que frue extraida de un censo de 1994.
Aquí se muestra una pequeña parte del dataset:

| |age| workclass       |fnlwgt|education|education-num|marital-status    |occupation       |relationship |race |sex   |capital-gain|capital-loss|hours-per-week|native-country|salary|
|-|---|:----------------|------|---------|-------------|------------------|-----------------|-------------|-----|------|------------|------------|--------------|--------------|------|
|0| 39| State-gov       | 77516|Bachelors|           13|Never-married     |Adm-clerical     |Not-in-family|White|Male  |        2174|           0|            40|United-States |<=50K |
|1| 50| Self-emp-not-inc| 83311|Bachelors|           13|Married-civ-spouse|Exec-managerial  |Husband      |White|Male  |           0|           0|            13|United-States |<=50K |
|2| 38| Private         |215646|HS-grad  |            9|Divorced          |Handlers-cleaners|Not-in-family|White|Male  |           0|           0|            40|United-States |<=50K |
|3| 53| Private         |234721|11th     |            7|Married-civ-spouse|Handlers-cleaners|Husband      |Black|Male  |           0|           0|            40|United-States |<=50K |
|4| 28| Private         |338409|Bachelors|           13|Married-civ-spouse|Prof-specialty   |Wife         |Black|Female|           0|           0|            40|Cuba          |<=50K |


Se debe de utilizar Pandas para responder las siguientes preguntas:
-Cuantas personas de cada raza estan representadas en el dataser? Esto debera ser una Series de Pandas con el nombre de las razas como indice(race column)
-Cual es la edad promedio de los hombres?
-Cual es el porcentaje de personas que tienen una carrera universitaria(Bachelors degree)
-Cual es el porcentaje de personas que tiene una educacion avanzada(Bachelor, Masters or Doctorate) y que genera mas de 50K?
-Cual es el porcentaje de personas que no tienen una educacion avanzada y genera mas de 50K?
-Cual es el minimo de horas que trabaja una persona por semana?
-Cual es el porcentaje de personas que trabaja el minimo de horas por semana y que tiene un salario mayor a 50K?
-Que pais tiene el porcentaje mas alto de personas que ganan mas de 50K y cual es ese procentaje?
-Identifica la ocupacion mas popular en india y que genera mas de 50K