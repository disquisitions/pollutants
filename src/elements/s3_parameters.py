"""
This is data type S3Parameters
"""
import typing


class S3Parameters(typing.NamedTuple):
    """
    The data type class ⇾ S3Parameters

    Attributes
    ----------
    region_name : str
      The Amazon Web Services region code.

    location_constraint : str
      The region code of the region that the data is limited to.

    access_control_list : str
      Access control list selection.

    bucket_int : str
      The Amazon S3 (Simple Storage Service) bucket that hosts this project's data.

    path_int_points : str
      The bucket path of the telemetric data.

    path_int_references : str
      The bucket path of the telemetric data references.
    """

    region_name: str
    location_constraint: str
    access_control_list: str
    bucket_int: str
    path_int_points: str
    path_int_references: str
