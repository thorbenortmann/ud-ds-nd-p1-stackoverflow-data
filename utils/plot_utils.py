from typing import Optional, Tuple

from pandas import DataFrame


def plot_df(df: DataFrame,
            title: str,
            figsize: Tuple[int, int],
            column_to_sort_by: Optional[str] = None,
            ascending: bool = False) -> None:
    """
    Plot the given DataFrame as a bar chart, assuming that its first column holds the x data
    and all other columns hold y data.
    :param df: DataFrame to plot.
    :param title: title to use for the plot.
    :param figsize: tuple of width and height of the plot.
    :param column_to_sort_by: column_name to use to sort the DataFrame in advance of plotting.
    :param ascending: whether to sort in an ascending or descending order.
    :return: None
    """
    if column_to_sort_by:
        df: DataFrame = df.sort_values(column_to_sort_by, ascending=ascending)

    column_names = df.columns.tolist()

    df.plot.bar(
        x=column_names[0],
        y=column_names[1:],
        title=title,
        figsize=figsize)
