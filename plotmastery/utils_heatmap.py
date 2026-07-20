import numpy as np
import matplotlib
import pandas as pd
from sklearn.cluster import AgglomerativeClustering


def annotate_heatmap(im, data=None, valfmt="{x:.2f}",
                     dot_instead_of_zeros=False,
                     textcolors=("black", "white"),
                     threshold=None, **textkw):
    """
    Annotate a heatmap with text labels for each cell.

    This function adds text annotations to a heatmap image, placing formatted
    values at the center of each cell. Text color is determined by comparing
    cell values to a threshold to enhance readability.

    Parameters
    ----------
    im : matplotlib.image.AxesImage
        The AxesImage object representing the heatmap to be annotated.
    data : array-like, optional
        Data used to annotate. If None, the image's data array is used.
        Should have same shape as the heatmap. Default is None.
    valfmt : str or matplotlib.ticker.Formatter, default="{x:.2f}"
        Format specification for the annotations. Can be a format string
        (e.g., "$ {x:.2f}") or a matplotlib.ticker.Formatter instance.
    dot_instead_of_zeros : bool, default=False
        If True, zero values are displayed as dots instead of their numeric value.
    textcolors : tuple of str, default=("black", "white")
        Pair of colors for the text annotations. The first color is used for
        values below the threshold, the second for values above the threshold.
    threshold : float, optional
        Threshold value in data units for choosing text color. If None (default),
        the midpoint of the colormap range is used as the threshold.
    **textkw : dict
        Additional keyword arguments passed to matplotlib.axes.Axes.text(),
        such as fontsize, fontweight, rotation, etc.

    Returns
    -------
    list of matplotlib.text.Text
        List of Text objects representing the annotations, one for each cell
        in the heatmap.

    Examples
    --------
    >>> import numpy as np
    >>> import matplotlib.pyplot as plt
    >>> fig, ax = plt.subplots()
    >>> data = np.random.rand(5, 5)
    >>> im = ax.imshow(data)
    >>> texts = annotate_heatmap(im, data, valfmt="{x:.1f}")
    """

    if not isinstance(data, (list, np.ndarray)):
        data = im.get_array()

    # Get extent of the images to know where to put the text:
    x_min, x_max, y_min, y_max = im.get_extent()

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
    x_ranges = np.linspace(x_min, x_max, data.shape[1] + 1)
    y_ranges = np.linspace(y_min, y_max, data.shape[0] + 1)[::-1]

    # Center
    x_ranges += (x_ranges[1] - x_ranges[0])/2
    y_ranges += (y_ranges[1] - y_ranges[0])/2

    for i in range(data.shape[0]):
        for j in range(data.shape[1]):

            kw.update(color=textcolors[int(im.norm(data[i, j]) > threshold)])
            if data[i, j] == 0 and dot_instead_of_zeros:
                text = im.axes.text(x_ranges[j], y_ranges[i], ".", **kw)
            else:
                text = im.axes.text(
                    x_ranges[j], y_ranges[i],
                    valfmt(data[i, j], None), **kw)
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


def order_rows_and_columns(data, linkage="single", connectivity=None):
    clst = AgglomerativeClustering(
        compute_full_tree=True,
        metric="precomputed",
        connectivity=connectivity,
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
