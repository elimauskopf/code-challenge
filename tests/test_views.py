

# This function should return a parsed address
def test_api_parse_succeeds(client):
    address_string = '123 main st chicago il'
    response = client.get(f"http://localhost:8000/api/parse/?address=${address_string}")
    assert response.status_code == 200
    data = response.json()
    assert {'input_string': '$123 main st chicago il',
            'address_components':
            {'AddressNumber': '123', 'StreetName': 'main',
             'StreetNamePostType': 'st', 'PlaceName': 'chicago',
             'StateName': 'il'}, 'address_type': 'Street Address'} == data


# This function should return a 400 error and
# return a message saying the given address has repeated labels
def test_api_parse_raises_error(client):
    address_string = '123 main st chicago il 123 main st'
    response = client.get(f"http://localhost:8000/api/parse/?address=${address_string}")
    assert response.status_code == 400
    data = response.json()
    assert data['detail'] == "Address has repeated labels"
