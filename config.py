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

        # After the development phase ...
        self.span: int = 244

        # Devices in focus, via their sequence identifiers
        # pollutant: Nitrogen Dioxide
        # area: Edinburgh
        # sequence (station): 155 (901), 531 (1014), 177 (460), 150 (791) 165(327), 142 (196)
        self.sequence_id_filter = [155, 531, 177, 150]

        # The points metadata
        self.metadata = {'epoch_ms': 'The milliseconds unix epoch time  when the measure was recorded',
                         'measure': 'The unit of measure of the pollutant under measure',
                         'timestamp': 'The timestamp of the measure',
                         'date': 'The date the measure was recorded',
                         'sequence_id': 'The identification code of the sequence this record is part of.'}
