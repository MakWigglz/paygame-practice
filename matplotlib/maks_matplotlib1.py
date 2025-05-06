import matplotlib.pyplot as plt
from matplotlib.patches import Patch

legend_patches = [
    Patch(color='red', label='Category 1'),
    Patch(color='blue', label='Category 2')
]

fig, ax = plt.subplots()
ax.legend(handles=legend_patches)
plt.show()
