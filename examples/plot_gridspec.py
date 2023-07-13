"""
Using gridspec
--------------

"""

import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec


def format_axes(fig):
    for i, ax in enumerate(fig.axes):
        ax.text(0.5, 0.5, "ax%d" % (i+1), va="center", ha="center")
        ax.set_xticks([])
        ax.set_yticks([])

fig = plt.figure(figsize=(10, 10), tight_layout=True)

gs = GridSpec(10, 10, figure=fig, top=0.9, left=0.1)
ax1 = fig.add_subplot(gs[1:, 1:])
# identical to ax1 = plt.subplot(gs.new_subplotspec((0, 0), colspan=3))
ax2 = fig.add_subplot(gs[1:, 0])
ax3 = fig.add_subplot(gs[0, 1:])

fig.suptitle("GridSpec")
format_axes(fig)

plt.show()

