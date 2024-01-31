"""
Module config
"""
import os


class Config:
    """
    Class Config

    For project settings
    """

    def __init__(self):
        """
        Constructor
        """

        self.warehouse = os.path.join(os.getcwd(), 'warehouse')
        self.points_storage = os.path.join(self.warehouse, 'environment', 'pollutants', 'points')

        # After the development phase, '732 days', i.e., 2 years.
        self.span = '28 days'

        # 1 Sulphur Dioxide [SO2]
        # 5 Particulate matter < 10 µm (aerosol)
        # 8 Nitrogen Dioxide (air) [NO2]
        # 38 Nitrogen Monoxide [NO]
        self.hazards = [1, 38]

        # Devices in focus, via their series codes
        # station: 907, sequence 161 | station: 900, sequence 154 | station: 1013, sequence 530 |
        self.sequence_id_filter = [161, 154, 530]
