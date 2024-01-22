from datetime import datetime

class DateTimeUtils:
    """
    Utility class for handling date and time operations.

    :param row: Dictionary containing data.
    :param key: Key specifying the date field in the dictionary.
    :returns: None
    :raises ValueError: If the date format is invalid or if there's an issue with parsing the date.
    """

    @staticmethod
    def handle_date_microseconds(row, key):
        """
        Handles date parsing for microseconds in the specified dictionary.

        :param row: Dictionary containing data.
        :param key: Key specifying the date field in the dictionary.
        :returns: None
        :raises ValueError: If the date format is invalid or if there's an issue with parsing the date.
        """
        date_string = row[key]
        if '.' in date_string:
            date_format = "%Y-%m-%d %H:%M:%S.%f"
        else:
            date_format = "%Y-%m-%d %H:%M:%S"
        row[key] = datetime.strptime(date_string, date_format)
