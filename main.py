#Aqui se hace la importacion de las librerias
from graphic import Graphic
from read_csv import Read
import matplotlib.pyplot as ptl


#Obtenemos los datos necesarios
dataBase = Read('./data.csv')
contries = {i['Country/Territory']: i['World Population Percentage'] for i in dataBase}


#Hacemos la conversion de los datos a variables directas
contriesName = list(contries.keys())
contriesValues = list(contries.values())


#Creamos la grafica de pastel
Graphic(contriesName, contriesValues, 'GRAFICA MUNDIAL')