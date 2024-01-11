"""
Module glue_parameters.py
"""
import typing


class GlueParameters(typing.NamedTuple):
    """
    The data type class -> GlueParameters
    """

    crawler_name: str
    database_name: str
    description: str
    table_prefix: str
