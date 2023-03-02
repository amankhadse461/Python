#1
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 2.0*np.pi, 101)
y = np.sin(x)
z = np.sinh(x)
# separate the figure object and axes object
# from the plotting object
fig, ax1 = plt.subplots()
# Duplicate the axes with a different y axis
# and the same x axis
ax2 = ax1.twinx() # ax2 and ax1 will have common x axis and different y axis
# plot the curves on axes 1, and 2, and get the curve handles
curve1, = ax1.plot(x, y, label="sin", color='r')
curve2, = ax2.plot(x, z, label="sinh", color='b')
# Make a curves list to access the parameters in the curves
curves = [curve1, curve2]
# add legend via axes 1 or axes 2 object.
# one command is usually sufficient
# ax1.legend() # will not display the legend of ax2
# ax2.legend() # will not display the legend of ax1
ax1.legend(curves, [curve.get_label() for curve in curves])
# ax2.legend(curves, [curve.get_label() for curve in curves]) # also valid
# Global figure properties
plt.title("Plot of sine and hyperbolic sine")
plt.show()


#2
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 2.0*np.pi, 101)
y = np.sin(x)
# values for making ticks in x and y axis
xnumbers = np.linspace(0, 7, 15)
ynumbers = np.linspace(-1, 1, 11)
plt.plot(x, y, color='r', label='sin') # r - red colour
plt.xlabel("Angle in Radians")
plt.ylabel("Magnitude")
plt.title("Plot of some trigonometric functions")
plt.xticks(xnumbers)
plt.yticks(ynumbers)
plt.legend()
plt.grid()
plt.axis([0, 6.5, -1.1, 1.1]) # [xstart, xend, ystart, yend]
plt.show()

#3
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 2.0*np.pi, 101)
y = np.sin(x)
z = np.cos(x)
# values for making ticks in x and y axis
xnumbers = np.linspace(0, 7, 15)
ynumbers = np.linspace(-1, 1, 11)
plt.plot(x, y, 'r', x, z, 'g') # r, g - red, green colour
plt.xlabel("Angle in Radians")
plt.ylabel("Magnitude")
plt.title("Plot of some trigonometric functions")
plt.xticks(xnumbers)
plt.yticks(ynumbers)
plt.legend(['sine', 'cosine'])
plt.grid()