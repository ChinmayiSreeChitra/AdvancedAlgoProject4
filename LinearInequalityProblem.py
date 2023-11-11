import numpy as np
import matplotlib.pyplot as plt

# Define ranges for plotting
x_range = np.linspace(0, 10, 400)
y_range = np.linspace(0, 10, 400)

# Constraints
y1 = 5 - x_range

plt.figure(figsize=(10, 10))

# Plotting Constraints
plt.plot(x_range, y1, '-r', label=r'$x + y \leq 5$')
plt.axvline(x=3, color='g', label=r'$x \geq 3$')
plt.axhline(y=3, color='b', label=r'$y \geq 3$')

# Highlighting Feasible Region
y_values = np.minimum(y1, 10)  # Clip y1 to 10 for visualization purposes
plt.fill_between(x_range, 3, y_values, where=(x_range>=3) & (y_values>=3), color='gray', alpha=0.3, label='Feasible Region')

# Labels, Title, and Legend
plt.xlabel('x')
plt.ylabel('y')
plt.title('Feasibility Problem Visualization')
plt.legend()
plt.xlim((0, 10))
plt.ylim((0, 10))
plt.grid(True)

plt.show()
