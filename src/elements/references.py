"""
This is the data type References
"""

import typing

import pandas as pd


class References(typing.NamedTuple):
    """
    The References class.
    """

    substances: pd.DataFrame = None
    stations: pd.DataFrame = None
    sequences: pd.DataFrame = None
