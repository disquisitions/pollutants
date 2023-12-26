"""
This is the data type References
"""

import typing

import pandas as pd


class References(typing.NamedTuple):
    """
    The References class.
    """

    sequences: pd.DataFrame = None
    stations: pd.DataFrame = None
    substances: pd.DataFrame = None
