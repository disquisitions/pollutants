"""
This is the data type Sequence
"""
import typing


class Sequence(typing.NamedTuple):
    """
    The data type class -> Sequence
    """

    sequence_id: int
    unit_of_measure: str
    station_id: int
    pollutant_id: int
    station_label: str
    longitude: float
    latitude: float
    substance: str
    notation: str
