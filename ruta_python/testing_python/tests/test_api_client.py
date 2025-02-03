import unittest
from src.api_client import get_location
from unittest.mock import patch

class ApiClientTests(unittest.TestCase):
    """
    Unit tests for the API client functions.
    
    Methods
    -------
    test_get_location_returns_expected_data():
        Tests that the get_location function returns the expected data when called with a specific IP address.
    """

    @patch('src.api_client.requests.get')
    def test_get_location_returns_expected_data(self, mock_get):
        """
        Tests that the get_location function returns the expected data when called with a specific IP address.
        
        Mocks the requests.get method to return a predefined response and verifies that the get_location function
        correctly processes this response.
        
        Parameters
        ----------
        mock_get : unittest.mock.Mock
            The mock object for requests.get.
        """
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "countryName": "USA",
            "regionName": "FLORIDA",
            "cityName": "MIAMI",
        }
        result = get_location("8.8.8.8")
        self.assertEqual(result.get("country"), "USA")
        self.assertEqual(result.get("region"), "FLORIDA")
        self.assertEqual(result.get("city"), "MIAMI")

        mock_get.assert_called_once_with("https://freeipapi.com/api/json/8.8.8.8")