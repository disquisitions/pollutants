"""
This is data type Parameters
"""
import typing


class Parameters(typing.NamedTuple):
    """
    The data type class Parameters
    """

    region_name: str
    location_constraint: str
    access_control_list: str
