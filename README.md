# decisionTrees

Imagina que trabajas en investigación médica. 
Se han recopilado datos sobre un conjunto de pacientes, todos los cuales padecían la misma enfermedad. 
Durante su tratamiento, cada paciente respondió a uno de 5 medicamentos:
 Drug A, Drug B, Drug C, Drugx e Drugy. 
El reto es construir un modelo para averiguar qué medicamento podría ser apropiado para un futuro paciente con la misma enfermedad. 
Las variables (features) de este conjunto de datos son: edad, sexo, presión arterial y colesterol de los pacientes, y el objetivo (target) es el fármaco al que respondió cada paciente. 
Este es un caso de clasificaión multiclase.

1. Crear un árbol de decision que permita predecir que medicamento debemos recetar a los siguientes pacientes. Indica para cada uno print() cual es la medicación correcta.

Age,Sex,BP,Cholesterol,Na_to_K

34,1,2,1,19.199

43,0,0,1,20.276

74,0,0,2,10


2. Adjunta una imagen del Arbol de decisión mas simple (menos nodos) que puedas construir.

DATA Source: IBM

En el dataset se han hecho los siguientes cambios para poder manipularlo numéricamente.

Drug A, Drug B, Drug C, Drugx e Drugy han sido cambiadas en el dataset por 0, 1, 2 , 3 y 4
Sex F = 0 M = 1

La presión y el colesterol se han traducido como:
Other = 0
Low = 1
High = 2

