import numpy as np


def set_size(width_pt, fraction=1, subplots=(1, 1)):
    """Set figure dimensions to sit nicely in our document.

    Parameters
    ----------
    width_pt: float
            Document width in points
    fraction: float, optional
            Fraction of the width which you wish the figure to occupy
    subplots: array-like, optional
            The number of rows and columns of subplots.
    Returns
    -------
    fig_dim: tuple
            Dimensions of figure in inches
    """
    # Width of figure (in pts)
    fig_width_pt = width_pt * fraction
    # Convert from pt to inches
    inches_per_pt = 1 / 72.27

    # Golden ratio to set aesthetic figure height
    golden_ratio = (5**0.5 - 1) / 2

    # Figure width in inches
    fig_width_in = fig_width_pt * inches_per_pt
    # Figure height in inches
    fig_height_in = fig_width_in * golden_ratio * (subplots[0] / subplots[1])

    return (fig_width_in, fig_height_in)


def sort_u_by_x(basis, u):
    x_coords = basis.doflocs[0]  # [0, 1, 0.25, 0.5, 0.75]
    indeces = [i for i in range(len(x_coords))]  # [0, 1, 2, 3, 4]
    indeces_by_x = [id for _, id in sorted(zip(x_coords, indeces))]  # [0, 4, 1, 2, 3]
    x_sorted = np.sort(x_coords)  # [0, 0.25, 0.5, 0.75, 1]
    res = [u[i] for i in indeces_by_x]  # [u_0, u_0.25, u_0.5, u_0.75, u_1]
    return (x_sorted, res)
