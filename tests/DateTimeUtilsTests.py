import unittest
from datetime import datetime
from assertpy import assert_that

from src.DateTimeUtils import parse_datetime_with_microseconds


class TestDateTimeUtils(unittest.TestCase):
    def test_valid_datetime_without_microseconds(self):
        # Arrange
        dictionary = {"key": "2022-01-22 12:34:56"}

        # Act
        parse_datetime_with_microseconds(dictionary, "key")

        # Assert
        expected_date = datetime(2022, 1, 22, 12, 34, 56)
        assert_that(dictionary["key"]).is_equal_to(expected_date)

    def test_valid_datetime_with_microseconds(self):
        # Arrange
        dictionary = {"key": "2022-01-22 12:34:56.789"}

        # Act
        parse_datetime_with_microseconds(dictionary, "key")

        # Assert
        expected_date = datetime(2022, 1, 22, 12, 34, 56, 789000)
        assert_that(dictionary["key"]).is_equal_to(expected_date)

    def test_invalid_datetime_string(self):
        # Arrange
        dictionary = {"key": "invalid_datetime"}

        # Act and Assert
        with self.assertRaises(ValueError):
            parse_datetime_with_microseconds(dictionary, "key")

    def test_datetime_string_with_invalid_format(self):
        # Arrange
        dictionary = {"key": "2022-01-22 12:34:56.invalid"}

        # Act and Assert
        with self.assertRaises(ValueError):
            parse_datetime_with_microseconds(dictionary, "key")

    def test_datetime_string_with_unexpected_key(self):
        # Arrange
        dictionary = {"other_key": "2022-01-22 12:34:56"}

        # Act and Assert
        with self.assertRaises(KeyError):
            parse_datetime_with_microseconds(dictionary, "key")

    def test_empty_dictionary(self):
        # Arrange
        dictionary = {}

        # Act and Assert
        with self.assertRaises(KeyError):
            parse_datetime_with_microseconds(dictionary, "key")


if __name__ == '__main__':
    unittest.main()
