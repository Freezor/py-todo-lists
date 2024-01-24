from datetime import datetime


def parse_datetime_with_microseconds(dictionary, key):
    """
    Handles date parsing for microseconds in the specified dictionary.

    :param dictionary: Dictionary containing data.
    :param key: Key specifying the date field in the dictionary.
    :returns: None
    :raises ValueError: If the date format is invalid or if there's an issue with parsing the date.
    """
    date_string = dictionary[key]
    if '.' in date_string:
        date_format = "%Y-%m-%d %H:%M:%S.%f"
    else:
        date_format = "%Y-%m-%d %H:%M:%S"
    dictionary[key] = datetime.strptime(date_string, date_format)
