'''
import matplotlib.pyplot as plt

# Sample data
x = [0,1, 2, 3, 4, 5]
y = [0,2, 4, 6, 8, 10]

# Create a figure and axis
fig, ax = plt.subplots()

# Add a title and axis labels
ax.set_title('My Line Plot')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

# Plot the data as a line
ax.plot(x, y)

# Display the plot
plt.show()
'''

import numpy as np
import matplotlib.pyplot as plt
import math

def e_arcsin(x):
    if x < -1 or x > 1:
        return None
    radians = math.asin(x)
    result = math.exp(radians)
    return result

# Create a range of x values from -1 to 1
x = np.linspace(-1, 1, 100)

# Compute y values using the e_arcsin function
y = [e_arcsin(xi) for xi in x]

# Create a figure and axis
fig, ax = plt.subplots()

# Add a title and axis labels
ax.set_title('e^(arcsin(x))')
ax.set_xlabel('x')
ax.set_ylabel('y')

# Plot the function
ax.plot(x, y)

# Display the plot
plt.show()
