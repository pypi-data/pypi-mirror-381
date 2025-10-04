"""Add significance bars to a plot.

Raises:
    ValueError: If pval is not provided.
"""

from typing import Optional
from matplotlib.axes import Axes
import matplotlib.pyplot as plt


def plot_significance_bars(
    x1: list,
    x2: list,
    pval: Optional[float] = None,
    show_non_significant: bool = False,
    show_pval_text: bool = False,
    ax: Optional[Axes] = None,
    round_pval: int = 2,
    p_value_text_size: int = 12,
    y_position_percentage: float = 0.95,
    bar_buffer: float = 0.025,
    sig_buffer: float = 0.001,
    text_buffer: float = 0.015,
    leg_length: float = 0.015,
    color: str = "black",
):
    """
    Add significance bars to a plot.
    Args:
        x1 (list): x-coordinates of the first set of points.
        x2 (list): x-coordinates of the second set of points.
        pval (float, optional): p-value for significance. Defaults to None.
        show_non_significant (bool, optional): Whether to show non-significant results. Defaults to False.
        show_pval_text (bool, optional): Whether to show p-value text. Defaults to False.
        ax (Axes, optional): Matplotlib Axes object to plot on. Defaults to None.
        round_pval (int, optional): Number of decimal places to round p-value. Defaults to 2.
        p_value_text_size (int, optional): Font size for p-value text. Defaults to 12.
        y_position_percentage (float, optional): Vertical position as a percentage of the y-axis. Defaults to 0.95.
        bar_buffer (float, optional): Vertical space between the top of the plot and the significance bar. Defaults to 0.025.
        sig_buffer (float, optional): Vertical space between the significance bar and the significance text. Defaults to 0.001.
        text_buffer (float, optional): Vertical space between the significance text and the p-value text. Defaults to 0.015.
        leg_length (float, optional): Length of the vertical legs of the significance bar. Defaults to 0.015.
        color (str, optional): Color of the significance bar and text. Defaults to "black".
    """

    if pval is None:
        raise ValueError("pval must be provided")

    if ax is None:
        ax = plt.gca()  # get current axes from the current figure

    pval_round = round(pval, round_pval)
    y_pval = y_position_percentage - text_buffer
    y_sig = y_position_percentage - sig_buffer
    y_bar = y_position_percentage - bar_buffer
    y_bar_bracket = y_bar - leg_length

    if pval_round <= 0.05 and pval_round > 0.01:
        sig = "*"
        sig_text = f"p = {pval_round}"
    elif pval_round <= 0.01 and pval_round > 0.001:
        sig = "**"
        sig_text = f"p = {pval_round}"
    elif pval_round <= 0.001:
        sig = "**"
        sig_text = "p < .001"
    else:
        if show_non_significant is False:
            return
        sig = ""
        sig_text = f"p = {pval_round}"

    ax.text(
        (x1[0] + x2[0]) / 2,
        y_sig,
        s=sig,
        size=p_value_text_size,
        c=color,
        horizontalalignment="center",
        transform=ax.get_xaxis_transform(),
    )
    ax.plot(
        [x1[0], x2[0]],
        [y_bar, y_bar],
        c=color,
        transform=ax.get_xaxis_transform(),
    )
    ax.plot(
        [x1[0], x1[0]],
        [y_bar, y_bar_bracket],
        c=color,
        transform=ax.get_xaxis_transform(),
    )
    ax.plot(
        [x2[0], x2[0]],
        [y_bar, y_bar_bracket],
        c=color,
        transform=ax.get_xaxis_transform(),
    )
    if show_pval_text:
        ax.text(
            (x1[0] + x2[0]) / 2,
            y_pval,
            sig_text,
            c=color,
            ha="center",
            size=p_value_text_size,
            horizontalalignment="center",
            transform=ax.get_xaxis_transform(),
        )
    return
