
import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

plt.style.use('fivethirtyeight')

x_vals = []
y_vals = []


index = count()

def animate(i):
    x_vals.append(next(index))  # sequential count
    y_vals.append(random.randint(0, 5))  # random value between 0 and 5

    plt.cla()  # clears the previous chart to prevent the stacking of diff diff plots every time resulting to give diff diff colours each time
    plt.plot(x_vals, y_vals)

ani = FuncAnimation(plt.gcf(), animate, interval=1000)  # animating the plot with a interval of 1 second

plt.tight_layout()


# saving the animation as .gif file type
f = r"Plot9a_LiveDataPlot_Basics.gif" 
writergif = PillowWriter(fps=120) 
ani.save(f, writer=writergif)

plt.show()