"""Module url"""


class URL:
    """
    Class URL
    """

    def __init__(self) -> None:
        """
        Constructor
        """

    def __pattern(self, datestr: str) -> str:
        """
        
        :param datestr: Date string YYYY-mm-dd
        :return
        """

        string = """https://www.scottishairquality.scot/sos-scotland/api/v1/timeseries/214/getData?""" + \
        """expanded=true&phenomenon=1&format=highcharts&timespan={datestr}T00:00:00Z/{datestr}T23:59:59Z"""

        return string.format(datestr=datestr)

    def exc(self, datestr: str) -> str:
        """
        
        :param datestr: Date string YYYY-mm-dd
        :return
        """

        return self.__pattern(datestr=datestr)
