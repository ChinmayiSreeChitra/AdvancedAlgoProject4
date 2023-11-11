import numpy as np
import matplotlib.pyplot as plt

# Define ranges for plotting
L_range = np.linspace(0, 100, 400)
S_range = np.linspace(0, 100, 400)

# Constraints
S1 = 100 - L_range
S2 = [50 for _ in L_range]
L2 = 70

# Feasible Region
L_values = np.linspace(0, L2, 400)
S_values = np.linspace(0, S2[0], 400)

plt.figure(figsize=(10, 10))

# Plotting Constraints
plt.plot(L_range, S1, label=r'$L + S \leq 100$')
plt.axhline(y=S2[0], color='r', label=r'$S \leq 50$')
plt.axvline(x=L2, color='b', label=r'$L \leq 70$')

# Highlighting Feasible Region
plt.fill_between(L_values, 0, np.minimum(S1[:len(L_values)], S2[:len(L_values)]), color='gray', alpha=0.3)

# Labels, Title, and Legend
plt.xlabel('Lemons (L)')
plt.ylabel('Sugar (S)')
plt.title('Maximize Profit for a Lemonade Stand Visualization')
plt.legend()
plt.xlim((0, 100))
plt.ylim((0, 100))
plt.grid(True)

plt.show()
