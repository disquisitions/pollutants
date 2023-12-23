"""Module url"""


class URL:
    """
    Class URL
    """

    def __init__(self) -> None:
        """
        Constructor
        """

    @staticmethod
    def __pattern(sequence_id: int, datestr: str) -> str:
        """

        :param sequence_id: The identification code of an air pollutant sequence
        :param datestr: Date string YYYY-mm-dd
        :return
        """

        string = f"""https://www.scottishairquality.scot/sos-scotland/api/v1/timeseries/{sequence_id}/getData?""" + \
                 f"""expanded=true&phenomenon=1&format=highcharts&timespan={datestr}T00:00:00Z/{datestr}T23:59:59Z"""

        return string

    def exc(self, sequence_id: int, datestr: str) -> str:
        """

        :param sequence_id: The identification code of an air pollutant sequence
        :param datestr: Date string YYYY-mm-dd
        :return
        """

        return self.__pattern(sequence_id=sequence_id, datestr=datestr)
