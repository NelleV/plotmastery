import matplotlib.pyplot as plt


def heatmap(X, row_annotation=None, col_annotation=None):
    """
    Plot a heatmap

    Parameters
    X : ndarray (n, m)
        the heatmap to plot.

    row_annotation : ndarray (n, p)

    col_annotation : ndarray (m, l)

    Return
    ------
    something that I am not sure what it is yet
    """
    if row_annotation is None and col_annotation is None:
        fig, ax = plt.subplots()
        _heatmap(X, ax)
        return ax


def _heatmap(X, ax):
    ax.imshow(X)
    ax.set_xticks([])
    ax.set_yticks([])
