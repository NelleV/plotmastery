"""
Plotting a basic heatmap
"""
import numpy as np
from heatmaps import heatmap

X = np.random.randint(0, 100, (100, 100))

heatmap(X)
