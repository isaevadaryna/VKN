import pylab
import numpy as np
with open('text.txt', 'r') as file:
    file_contents = file.read()
b = file_contents.split()
c = str(b).split()
b = len(c)
x = np.array([1,2,3,4])
y = np.array([b])

pylab.bar(x,y)
pylab.show()