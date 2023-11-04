import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import pulp

# Linear programming setup
lp_problem = pulp.LpProblem("Widget_and_Gadget_Manufacturing", pulp.LpMaximize)
W = pulp.LpVariable('W', lowBound=0)
G = pulp.LpVariable('G', lowBound=0)
lp_problem += 50 * W + 60 * G, "Total_Profit"
lp_problem += 4 * W + 3 * G <= 240, "Material_A_constraint"
lp_problem += 3 * W + 5 * G <= 150, "Material_B_constraint"
lp_problem += 2 * W + 3 * G <= 100, "Labor_constraint"
lp_problem.solve()

# Constraints equations
x = np.linspace(0, 80, 400)  # Adjusted the x values for visibility
y1 = (240 - 4 * x) / 3
y2 = (150 - 3 * x) / 5
y3 = (100 - 2 * x) / 3

fig, ax = plt.subplots(figsize=(8, 8))


def update(frame):
    ax.clear()  # Clear the axes for the new frame
    ax.set_xlim(0, 80)
    ax.set_ylim(0, 60)
    ax.set_xlabel('Number of Widgets (W)')
    ax.set_ylabel('Number of Gadgets (G)')
    ax.set_title('Widget and Gadget Manufacturing Optimization')

    if frame == 0:
        ax.text(40, 30, 'Decision Variables:\nWidgets (W) and Gadgets (G)', ha='center')
    elif frame == 1:
        ax.text(40, 30, 'Objective Function:\nMaximize 50W + 60G', ha='center')
    elif frame == 2:
        ax.plot(x, y1, 'y-')
        ax.text(40, 30, 'Material A Constraint:\n4W + 3G ≤ 240', ha='center')
    elif frame == 3:
        ax.plot(x, y1, 'y-')
        ax.plot(x, y2, 'g-')
        ax.text(40, 30, 'Material B Constraint:\n3W + 5G ≤ 150', ha='center')
    elif frame == 4:
        ax.plot(x, y1, 'y-')
        ax.plot(x, y2, 'g-')
        ax.plot(x, y3, 'b-')
        ax.text(40, 30, 'Labor Constraint:\n2W + 3G ≤ 100', ha='center')
    elif frame == 5:
        ax.plot(x, y1, 'y-', label="Material A Constraint")
        ax.plot(x, y2, 'g-', label="Material B Constraint")
        ax.plot(x, y3, 'b-', label="Labor Constraint")
        y4 = np.minimum(np.minimum(y1, y2), y3)
        ax.fill_between(x, 0, y4, where=(y4 >= 0), color='gray', alpha=0.5)
        ax.text(40, 30, 'Feasible Region Defined by All Constraints', ha='center')
    elif frame == 6:
        ax.plot(x, y1, 'y-', label="Material A Constraint")
        ax.plot(x, y2, 'g-', label="Material B Constraint")
        ax.plot(x, y3, 'b-', label="Labor Constraint")
        y4 = np.minimum(np.minimum(y1, y2), y3)
        ax.fill_between(x, 0, y4, where=(y4 >= 0), color='gray', alpha=0.5)
        ax.scatter(W.varValue, G.varValue, color='red', s=100, zorder=5)
        ax.text(40, 30, f'Optimal Solution:\nWidgets(W)={W.varValue}, Gadgets(G)={G.varValue}', ha='center')
    elif frame == 7:
        ax.plot(x, y1, 'y-', label="Material A Constraint")
        ax.plot(x, y2, 'g-', label="Material B Constraint")
        ax.plot(x, y3, 'b-', label="Labor Constraint")
        y4 = np.minimum(np.minimum(y1, y2), y3)
        ax.fill_between(x, 0, y4, where=(y4 >= 0), color='gray', alpha=0.5)
        ax.scatter(W.varValue, G.varValue, color='red', s=100, zorder=5)
        ax.text(40, 30, f'Maximum Profit: ${pulp.value(lp_problem.objective)}', ha='center')

    ax.legend(loc='upper right')


ani = FuncAnimation(fig, update, frames=8, repeat=False, interval=2000)
plt.tight_layout()
plt.show()
