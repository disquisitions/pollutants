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
        self.points_storage = os.path.join(self.warehouse, 'particulates', 'pollutants', 'points')

        # After the development phase, 732 days, i.e., 2 years.
        self.span: int = 244

        # Hazardous items in focus
        # 1 Sulphur Dioxide [SO2]
        # 5 Particulate matter < 10 µm (aerosol)
        # 8 Nitrogen Dioxide (air) [NO2]
        # 38 Nitrogen Monoxide [NO]
        # self.hazards = [1, 38]

        # Devices in focus, via their sequence identifiers
        # pollutant: Nitrogen Dioxide
        # area: Edinburgh
        # sequence (station): 155 (901), 531 (1014), 177 (460), 150 (791) 165(327), 173 (377),
        #                     146 (536), 142 (196), 169 (259),
        self.sequence_id_filter = [155, 531, 177, 150]

        # The points metadata
        self.metadata = {'epoch_ms': 'The milliseconds unix epoch time  when the measure was recorded',
                         'measure': 'The unit of measure of the pollutant under measure',
                         'timestamp': 'The timestamp of the measure',
                         'date': 'The date the measure was recorded',
                         'sequence_id': 'The identification code of the sequence this record is part of.'}
