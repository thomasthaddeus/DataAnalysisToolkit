import pytest
import requests
import requests_mock
from dataanalysistoolkit.interfaces.api_connector import APIConnector

@pytest.fixture
def api_connector():
    return APIConnector('https://api.example.com')

def test_get_request(api_connector):
    with requests_mock.Mocker() as m:
        m.get('https://api.example.com/test', json={'success': True}, status_code=200)
        response = api_connector.get('test')
        assert response.json() == {'success': True}
        assert response.status_code == 200

def test_post_request(api_connector):
    with requests_mock.Mocker() as m:
        m.post('https://api.example.com/test', json={'received': True}, status_code=201)
        response = api_connector.post('test', json={'data': 'value'})
        assert response.json() == {'received': True}
        assert response.status_code == 201

def test_put_request(api_connector):
    with requests_mock.Mocker() as m:
        m.put('https://api.example.com/test', json={'updated': True}, status_code=200)
        response = api_connector.put('test', json={'new_data': 'value'})
        assert response.json() == {'updated': True}
        assert response.status_code == 200

def test_delete_request(api_connector):
    with requests_mock.Mocker() as m:
        m.delete('https://api.example.com/test', status_code=204)
        response = api_connector.delete('test')
        assert response.status_code == 204

# Additional tests for error handling, other methods, etc., can be added here
