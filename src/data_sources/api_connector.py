"""api_connector.py
_summary_

_extended_summary_

Returns:
    _type_: _description_

# Example usage
connector = APIConnector('https://api.example.com', auth=('username', 'password'))
response = connector.get('endpoint', params={'key': 'value'})
update_response = connector.put('endpoint', json={'key': 'updated_value'})
delete_response = connector.delete('endpoint', params={'key': 'value'})
patch_response = connector.patch('endpoint', json={'key': 'new_value'})
print(response.json())
"""

import requests

class APIConnector:
    """
     _summary_

    _extended_summary_
    """
    def __init__(self, base_url, auth=None):
        """
        Initialize the APIConnector with the base URL and optional authentication.

        Args:
            base_url (str): The base URL for the API.
            auth (tuple, optional): A tuple for authentication, typically (username, password) or an API token.
        """
        self.base_url = base_url
        self.auth = auth
        self.session = requests.Session()
        if auth:
            self.session.auth = auth

    def get(self, endpoint, params=None):
        """
        Send a GET request to the API.

        Args:
            endpoint (str): The API endpoint to send the request to.
            params (dict, optional): A dictionary of parameters to send with the request.

        Returns:
            Response: The response from the API.
        """
        url = f"{self.base_url}/{endpoint}"
        response = self.session.get(url, params=params)
        response.raise_for_status()  # Will raise an HTTPError if the HTTP request returned an unsuccessful status code
        return response

    def post(self, endpoint, data=None, json=None):
        """
        Send a POST request to the API.

        Args:
            endpoint (str): The API endpoint to send the request to.
            data (dict, optional): A dictionary of data to send in the body of the request.
            json (dict, optional): A JSON serializable object to send in the body of the request.

        Returns:
            Response: The response from the API.
        """
        url = f"{self.base_url}/{endpoint}"
        response = self.session.post(url, data=data, json=json)
        response.raise_for_status()
        return response


    def put(self, endpoint, data=None, json=None):
        """
        Send a PUT request to the API.

        Args:
            endpoint (str): The API endpoint to send the request to.
            data (dict, optional): A dictionary of data to send in the body of the request.
            json (dict, optional): A JSON serializable object to send in the body of the request.

        Returns:
            Response: The response from the API.
        """
        url = f"{self.base_url}/{endpoint}"
        response = self.session.put(url, data=data, json=json)
        response.raise_for_status()
        return response

    def delete(self, endpoint, params=None):
        """
        Send a DELETE request to the API.

        Args:
            endpoint (str): The API endpoint to send the request to.
            params (dict, optional): A dictionary of parameters to send with the request.

        Returns:
            Response: The response from the API.
        """
        url = f"{self.base_url}/{endpoint}"
        response = self.session.delete(url, params=params)
        response.raise_for_status()
        return response

    def patch(self, endpoint, data=None, json=None):
        """
        Send a PATCH request to the API.

        Args:
            endpoint (str): The API endpoint to send the request to.
            data (dict, optional): A dictionary of data to send in the body of the request.
            json (dict, optional): A JSON serializable object to send in the body of the request.

        Returns:
            Response: The response from the API.
        """
        url = f"{self.base_url}/{endpoint}"
        response = self.session.patch(url, data=data, json=json)
        response.raise_for_status()
        return response
