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

        # After the development phase, '732 days', i.e., 2 years.
        self.span = '5 days'

        # 1 Sulphur Dioxide
        # 5 Particulate matter < 10 µm (aerosol)
        # 8 Nitrogen Dioxide (air)
        self.hazards = [1, 8]
