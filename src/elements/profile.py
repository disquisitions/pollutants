"""
This is the data type Profile
"""
import typing


class Profile(typing.NamedTuple):
    """
    The data type class -> Sequence

    :var:
      profile: The identification code of the sequence the telemetric device records.
      account_id: The unit of measure of the recordings.
    """

    name: str
    account_id: int
