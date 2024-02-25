"""
Module config
"""
import os
import datetime


class Config:
    """
    Class Config

    For project settings
    """

    def __init__(self):
        """
        Constructor
        """

        self.warehouse: str = os.path.join(os.getcwd(), 'warehouse')

        # After the development phase the dates will be different
        self.starting = datetime.datetime.strptime(__date_string='2022-01-01', __format='%Y-%m-%d')
        self.ending = datetime.datetime.today()

        # Devices in focus, via their sequence identifiers
        # pollutant: Nitrogen Dioxide
        # area: Edinburgh
        # sequence (station): 155 (901), 531 (1014), 177 (460), 150 (791) 165(327), 142 (196)
        self.sequence_id_filter = [155, 531, 177, 150]
