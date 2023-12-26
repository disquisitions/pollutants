"""
This is data type Connector
"""
import typing


class Connector(typing.NamedTuple):
    """
    The data type class Connector
    """

    region_name: str
    availability_zone: str
    regional_root: str
    zonal_root: str
    root_affix: str
    bucket_base_name_affix: str
