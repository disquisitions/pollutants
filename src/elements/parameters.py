"""
This is data type Parameters
"""
import typing


class Parameters(typing.NamedTuple):
    """
    The data type class -> Parameters

    :parameter:
      region_name: The Amazon Web Services region code
      location_constraint: The region code of the region that the data is limited to
      access_control_list:
      bucket_name: The Amazon S3 bucket that hosts this project's data
      points_: The bucket path of the telemetric data
      references_: The bucket path of the telemetric data references
    """

    region_name: str
    location_constraint: str
    access_control_list: str
    bucket_name: str
    points_: str
    references_: str
