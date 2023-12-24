"""
This is the data type References
"""

import typing

import pandas as pd


class References(typing.NamedTuple):
    """
    The References class.
    """

    substances: pd.DataFrame
    stations: pd.DataFrame
    sequences: pd.DataFrame
