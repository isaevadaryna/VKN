import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 10, 51)
y = 3*(x**(1/2))+x
plt.plot(x, y, 'g:', label='3*(x**(1/2))+x')
plt.axis([-1,6,-1,6])
plt.xlabel('x')
plt.ylabel('y')
plt.title('function')
plt.legend()

plt.savefig('restart.jpg')
plt.show()

