#Variant №14
#Y(x)=1/x*sin(5*x), x=[-5...5]

import numpy as np
from matplotlib import pyplot as plt

x = np.arange(-5, 5)
y = 1/x * np.sin(5*x)

fig, ax = plt.subplots()
plt.plot(x,y)
plt.show()

fig.savefig('мій графік')
print("Ваш графік збереженний біля файла .py")
