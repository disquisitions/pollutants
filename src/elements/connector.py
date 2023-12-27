"""
This is data type Connector
"""
import typing


class Connector(typing.NamedTuple):
    """
    The data type class Connector
    """

    region_name: str
    location_constraint: str
    access_control_list: str
