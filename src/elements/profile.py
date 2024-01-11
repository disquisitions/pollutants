"""
This is the data type Profile
"""
import typing


class Profile(typing.NamedTuple):
    """
    The data type class -> Profile

    Attributes
    ----------
    name: The profile name.
    account_id: The Account ID of the profile.
    """

    name: str
    account_id: int
