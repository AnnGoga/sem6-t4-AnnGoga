import numpy as np
import matplotlib.pyplot as plt
import csv

Y1, Y2, names = [], [], []

with open("statistic_test1.csv") as file:
    reader = csv.reader(file, delimiter=';')
    for line in reader:
        names.append(line[0])
        Y1.append(int(line[1]))
        Y2.append(int(line[2]))


xs = range(len(names))

fig, ax = plt.subplots()
index = np.arange(len(names))

plt.scatter(xs, Y1, label=u'Ср. цена кв.м', color='gold')
plt.scatter(xs, Y2, label=u'Ср. цена квартиры', color='darkmagenta')

plt.xlabel('Районы Москвы')
plt.ylabel('Средняя цена')
plt.title('Ср. цена квартиры по районом Мск\n(РБК 27.02.19)')
plt.xticks(xs, names)
fig.autofmt_xdate(rotation=31)
plt.legend()

plt.show()
plt.savefig('plot.png')
