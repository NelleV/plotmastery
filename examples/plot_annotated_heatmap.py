"""
Plotting annotated heatmap
--------------------------

Well… not plotting right now…
"""

import numpy as np
from heatmaps import heatmap

X = np.random.randint(0, 100, (100, 100))
row_annotation = np.random.randint(0, 1, (100, ))
col_annotation = np.random.randint(0, 1, (100, ))

#heatmap(X, row_annotation=row_annotation, col_annotation=col_annotation)
