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

        # Devices in focus, via their series codes
        # station: 907, sequence 161, SO2 | station: 900, sequence 154, NO | station: 1013, sequence 530, NO | station: 136,
        # sequence: 228, NO2 | station: 148, sequence: 212, NO2
        #
        # sequences: 142, 169, 155, 531, 165, 173, 177, 146, 150 (NO2, EDB)
        self.sequence_id_filter = [142, 169, 155, 531, 165, 173, 177, 146, 150]

        # The points metadata
        self.metadata = {'epoch_ms': 'The milliseconds unix epoch time  when the measure was recorded',
                         'measure': 'The unit of measure of the pollutant under measure',
                         'timestamp': 'The timestamp of the measure',
                         'date': 'The date the measure was recorded',
                         'sequence_id': 'The identification code of the sequence this record is part of.'}
