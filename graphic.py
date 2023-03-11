import matplotlib.pyplot as ptl


def Graphic(labels, values, name):
    fig, ax = ptl.subplots()
    ax.pie(values, labels = labels)
    ptl.axis('equal')
    ax.set_title(name)
    ptl.show()


if __name__ == '__main__':
    gener = ['male', 'female']
    population = [50, 50]


    Graphic(gener, population, 'prueba')


