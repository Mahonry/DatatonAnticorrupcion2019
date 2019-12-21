# Datómicos
### Dataton Anticorrupción 2019
Repositorio del trabajo desarrollado por el equipo Datómicos durante el dataton anticorrupción 2019.

Es necesario tener instaladas las lirerías de python "*pymongo*" y "*JSON*". El archivo "([contratacionesDirectas2018.json]())" contiene las contrataciones públicas que realizó el gobierno por medio de adjudicación directa en el ejercicio fiscal 2018.   

El proyecto desarrollado consta de un **sistema heurístico de detección de anomalías en las contrataciones públicas**, ([Nuestra Presentacion](./presentacion_Datomicos.pdf)), el método de adjudicación directa es el de mayor interés ya que el gobierno "elige directamente" a las empresas, de acuerdo al **Presupuesto de Egresos de la Federación (PEF)** hay limítes para el monto de estos contratos por cada dependencia ([límites establecidos](./limites_presupuestales.xlsx)), los cuáles no puden ser indentificados directamente en la base de datos de contrataciones públicas ya que esta carece del apartado de *Planeación*, considerando el limite superior y el limite inferior del PEF se obtuvo un promedio para evaluar las contrataciones que superaran ese monto. 

