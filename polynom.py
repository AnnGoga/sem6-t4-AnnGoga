import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
import csv


def sq_error(_x, _y, f_x=None):
    squared_error = []
    for i in range(len(_x)):
        squared_error.append((f_x(_x[i]) - _y[i]) ** 2)
    return sum(squared_error)


X, Y = [], []

with open("coast.tsv") as tsvfile:
    tsv_reader = csv.reader(tsvfile, delimiter="\t")
    for line in tsv_reader:
        if line[1] != 'nan':
            X.append(float(line[0]))
            Y.append(float(line[1]))

x1 = [1, 743]

np_x = np.array(X)
np_y = np.array(Y)

x2 = list(range(743))

plt.scatter(X, Y, label=u'Исходные данные', linewidth = 0.1, color='c')

f3 = sp.poly1d(np.polyfit(np_x, np_y, 3))
plt.plot(x2, f3(x2), linewidth=3, color='b',label=u'3-ей степени')

f4 = sp.poly1d(np.polyfit(np_x, np_y, 4))
plt.plot(x2, f4(x2), linewidth=3, color='orangered',label=u'4-ой степени')

f5 = sp.poly1d(np.polyfit(np_x, np_y, 10))
plt.plot(x2, f5(x2), linewidth=3, color='darkmagenta',label=u'10-ой степени')

plt.legend()
plt.ylabel('y')
plt.xlabel('x')
plt.show()
plt.savefig('plot.png')
