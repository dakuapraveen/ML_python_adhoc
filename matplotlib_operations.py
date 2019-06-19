# -*- coding: utf-8 -*-
"""matplotlib_operations

Automatically generated by Colaboratory.

"""

import matplotlib   # load

#  !pip3 install matplotlib       (for install any lib)

del matplotlib   # unload

import matplotlib.pyplot   as  plt  # only loading python ori lib

x=[2,3]
x1=[4,3,8]
y1=[2,9,7]
y=[9,5]

plt.xlabel("time")
plt.ylabel("speed")
plt.grid(color="green")                    #to form grid in graph
plt.plot(x,y,label="water")      # this will draw a straight line
plt.bar(x1,y1)                   # to plot bar for x1,y1
plt.bar(x,y)                     # to plot bar for x,y
plt.plot(x1,y1,label="sand")
plt.legend()                     # to show label with plot
plt.xlim(0,10)                   # to show min and max number in x axis
plt.ylim(0,12)                   # to show min and max number in y axis

plt.plot(x1,y1)

# numpy ,matplot
# requests module  --> web  ---> text---> data
