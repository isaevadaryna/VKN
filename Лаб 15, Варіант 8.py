from tkinter import *
import pylab
import numpy as np
#event
x = np.array(['Jan','Feb','March','Ap','May',"June",'July',"August","Sep",'Oct','Nov',"Dec"])
y = np.array([30,40,26,50,78,43,89,56,90,83,65,79])

pylab.bar(x,y)
pylab.show()