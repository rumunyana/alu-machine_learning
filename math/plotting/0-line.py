#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

y = np.arange(0, 11) ** 3
x = np.arange(0, 11)
# Plotting the graph with a red line
plt.plot(x, y, 'r-')

# Setting the x-axis limit
plt.xlim(0, 10)

# Display the plot
plt.show()
