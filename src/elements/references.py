"""
This is the data type Interface
"""

import typing

import pandas as pd


class References(typing.NamedTuple):
    """
    The data type class Interface
    """

    sequences: pd.DataFrame = None
    stations: pd.DataFrame = None
    substances: pd.DataFrame = None
