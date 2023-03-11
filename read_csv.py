#Aqui estamos haciendo la importacion de modulos
import csv

def Read(data):
    with open(data, 'r') as file:
        reader = csv.reader(file, delimiter=',')
        header = next(reader)
        
        countries = []
        for item in reader:
            result = dict(zip(header, item))
            countries.append(result)

        return countries
        
if __name__ == '__main__':

    dataBase = Read('./data.csv')
    print(dataBase[1])