import numpy as np
import matplotlib
import pandas as pd
from sklearn.cluster import AgglomerativeClustering


def annotate_heatmap(im, data=None, valfmt="{x:.2f}",
                     textcolors=("black", "white"),
                     threshold=None, **textkw):
    """
    A function to annotate a heatmap.

    Parameters
    ----------
    im
        The AxesImage to be labeled.
    data
        Data used to annotate.  If None, the image's data is used.  Optional.
    valfmt
        The format of the annotations inside the heatmap.  This should either
        use the string format method, e.g. "$ {x:.2f}", or be a
        `matplotlib.ticker.Formatter`.  Optional.
    textcolors
        A pair of colors.  The first is used for values below a threshold,
        the second for those above.  Optional.
    threshold
        Value in data units according to which the colors from textcolors are
        applied.  If None (the default) uses the middle of the colormap as
        separation.  Optional.
    **kwargs
        All other arguments are forwarded to each call to `text` used to create
        the text labels.
    """

    if not isinstance(data, (list, np.ndarray)):
        data = im.get_array()

    # Normalize the threshold to the images color range.
    if threshold is not None:
        threshold = im.norm(threshold)
    else:
        threshold = im.norm(data.max())/2.

    # Set default alignment to center, but allow it to be
    # overwritten by textkw.
    kw = dict(horizontalalignment="center",
              verticalalignment="center")
    kw.update(textkw)

    # Get the formatter in case a string is supplied
    if isinstance(valfmt, str):
        valfmt = matplotlib.ticker.StrMethodFormatter(valfmt)

    # Loop over the data and create a `Text` for each "pixel".
    # Change the text's color depending on the data.
    texts = []
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):

            kw.update(color=textcolors[int(im.norm(data[i, j]) > threshold)])
            if data[i, j] == 0:
                text = im.axes.text(j, i, ".", **kw)
            else:
                text = im.axes.text(j, i, valfmt(data[i, j], None), **kw)
            texts.append(text)

    return texts


def order_rows(data, linkage="single", metric="manhattan"):
    clst = AgglomerativeClustering(
        compute_full_tree=True,
        metric=metric,
        linkage=linkage).fit(data)
    n_samples = data.shape[0]
    t = clst.children_.flatten()
    order = t[t < n_samples]
    if isinstance(data, pd.DataFrame):
        data = data.iloc[order]
    else:
        data = data[order]
    return data


def order_rows_and_columns(data, linkage="single"):
    clst = AgglomerativeClustering(
        compute_full_tree=True,
        metric="precomputed",
        linkage=linkage).fit(data)
    n_samples = data.shape[0]
    t = clst.children_.flatten()
    order = t[t < n_samples]
    if isinstance(data, pd.DataFrame):
        data = data.iloc[order]
        data = data[data.columns[order]]
    else:
        data = data[order]
        data = data[:, order]
    return data
