import math
import numpy as np
import matplotlib.pyplot as plt

# Declare empty lists for functions
sineList = []
coseList = []

# Get sine values in a list 
for i in range(360):
    sineList.append(math.sin(math.radians(i)))

# Get cosine values in a list 
for i in range(360):
    coseList.append(math.cos(math.radians(i)))

plt.plot(sineList, label = "sinx")
plt.plot(coseList, label = "cosx")
# Add the legend to the upper left corner
plt.legend(loc="upper right")
# Set y and x limits
plt.ylim(-1, 1)
plt.xlim(0, 360)
# Add 90 degree steps
plt.xticks([0, 90, 180, 270, 360])
plt.show()