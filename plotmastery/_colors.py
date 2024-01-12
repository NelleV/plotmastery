import numpy as np
from matplotlib import cm
from matplotlib import colors


def generate_colors_from_colormaps(n_colors, cmap="jet", as_hex=False):
    """
    Generate a list of n colors from colormap
    """

    colormap = cm.get_cmap(str(cmap))
    indx = np.linspace(0, 1, n_colors)
    indexed_colors = [colormap(i) for i in indx]
    if as_hex:
        indexed_colors = [colors.to_hex(i) for i in indexed_colors]
    return indexed_colors
