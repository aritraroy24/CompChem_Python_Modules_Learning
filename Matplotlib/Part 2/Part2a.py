"""
Part 2a Tutorial: Creating a bar chart using the listed data
"""

from matplotlib import pyplot as plt
import numpy as np

ages_x = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]

# Creates an NumPy array having element from 0 to len(ages_x)
x_indexes = np.arange(len(ages_x))

# Giving custom width to the bars
width = 0.25
dev_y = [17784, 16500, 18012, 20628, 25206, 30252, 34368, 38496, 42000, 46752, 49320]

plt.bar(x_indexes-width, dev_y, width=width, color='#444444', label='All Devs')   # Giving the bar same width as mentioined above and shifting the bar to left to same width (ofset)

py_dev_y = [20046, 17100, 20000, 24744, 30500, 37732, 41247, 45372, 48876, 53850, 57287]   # Giving the bar same width
plt.bar(x_indexes, py_dev_y, width=width, color='#5a7d9a', label = 'Python Devs')

js_dev_y = [16446, 16791, 18942, 21780, 25704, 29000, 34372, 37810, 43515, 46823, 49293]   # Giving the bar same width as mentioined above and shifting the bar to right to same width (ofset)
plt.bar(x_indexes+width, js_dev_y, width=width, color='#adad3b', label = 'JS Devs')

# Fixing the labeling of X axis as it changed to 0 to len(ages_x)
plt.xticks(ticks=x_indexes, labels=ages_x)  

plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.title('Median Salary (USD) by Age')

plt.legend()

plt.tight_layout()

plt.show()