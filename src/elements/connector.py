import typing


class Connector(typing.NamedTuple):

    region_name: str
    availability_zone: str
    regional_root: str
    zonal_root: str
    root_affix: str
    bucket_base_name_affix: str
