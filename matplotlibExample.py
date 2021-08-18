import matplotlib.pyplot as plt
import math

x = [1, 2, 3, 4, 5]
y = [math.sin(1), math.sin(2), math.sin(3), math.sin(4), math.sin(5)]

plt.plot(x, y)
plt.title("Sin of 1 to 5")
plt.show()