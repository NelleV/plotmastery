

def add_letter_and_title(ax, letter, title=None, extra_x_shift=0,
                         fontsize="medium"):
    """
    Add letter and title on an axis, positionned exactly at same shift.
    """
    x1, y1 = ax.transAxes.transform_point((0, 1))
    # Shift 0.4 inch on the x-axis and 0.1 inch on the y-axis
    x, y = ax.transAxes.inverted().transform_point(
        (x1 - 45 + extra_x_shift, y1 + 10))
    ax.text(
        x, y,
        letter, fontweight="bold", fontsize=fontsize,
        horizontalalignment="left",
        transform=ax.transAxes)

    if title is not None:
        x, y = ax.transAxes.inverted().transform_point(
            (x1 + extra_x_shift, y1 + 10))
        ax.text(
            x, y,
            title, fontweight="bold", fontsize=fontsize,
            horizontalalignment="left",
            transform=ax.transAxes)


def prepare_axes(ax):
    if isinstance(ax, list):
        [a.spines["right"].set_linewidth(0) for a in ax]
        [a.spines["top"].set_linewidth(0) for a in ax]
    else:
        ax.spines["right"].set_linewidth(0)
        ax.spines["top"].set_linewidth(0)
