from jsonschema import validate
import pytest
import schemas
import api_helpers
from hamcrest import assert_that, contains_string, is_
import requests

'''
TODO: Finish this test by...
1) Troubleshooting and fixing the test failure
The purpose of this test is to validate the response matches the expected schema defined in schemas.py
'''
def test_pet_schema():
    test_endpoint = "/pets/1"

    response = api_helpers.get_api_data(test_endpoint)

    assert response.status_code == 200

    # Validate the response schema against the defined schema in schemas.py
    validate(instance=response.json(), schema=schemas.pet)

'''

'''

'''
TODO: Finish this test by...
1) Extending the parameterization to include all available statuses
2) Validate the appropriate response code
3) Validate the 'status' property in the response is equal to the expected status
4) Validate the schema for each object in the response
'''
@pytest.mark.parametrize("status", [("available")])
def test_find_by_status_200(status):
    test_endpoint = "/pets/findByStatus"
    params = {
        "status": status
    }

    response = api_helpers.get_api_data(test_endpoint, params)
    assert response.status_code == 200

    # Validate the 'status' property in the response is equal to the expected status
    for pet in response.json():
        assert pet['status'] == status

    # Validate the schema for each object in the response
    for pet in response.json():
        validate(instance=pet, schema=schemas.pet)


'''
TODO: Finish this test by...
1) Testing and validating the appropriate 404 response for /pets/{pet_id}
2) Parameterizing the test for any edge cases
'''
@pytest.mark.parametrize("pet_id", [-1, "abc", 9999999, None, 0])
def test_get_by_id_404(pet_id):
    # Testing and validating the appropriate 404 response for /pets/{pet_id}
    if pet_id is None:
        pytest.skip("Skipping test with None ID")
    
    test_endpoint = f"/pets/{pet_id}"
    response = api_helpers.get_api_data(test_endpoint)

    assert response.status_code == 404
    try:
        # Try to decode JSON
        response_json = response.json()
    except requests.exceptions.JSONDecodeError:
        # If JSON decoding fails, it indicates response content is not in JSON format
        pytest.fail("Response content is not in JSON format")
    assert response.json()["message"] == "Pet not found"
 