from jsonschema import validate
import pytest
import schemas
import api_helpers
from hamcrest import assert_that, contains_string, is_

'''
TODO: Finish this test by...
1) Creating a function to test the PATCH request /store/order/{order_id}
2) *Optional* Consider using @pytest.fixture to create unique test data for each run
2) *Optional* Consider creating an 'Order' model in schemas.py and validating it in the test
3) Validate the response codes and values
4) Validate the response message "Order and pet status updated successfully"
'''
@pytest.fixture
def order_data():
    # Define unique test data for each run
    return {
        "pet_id": 3
    }

def test_place_and_patch_order(order_data):
    # Send POST request to place the order
    response_place = api_helpers.post_api_data("/store/order", order_data)

    # Validate response status code
    assert response_place.status_code == 201


    # Extract the order ID from the response
    order_id = response_place.json()["id"]

    # Validate response schema (optional)
    # validate(instance=response_place.json(), schema=schemas.order)

    # Send PATCH request to update the order status
    response_patch = api_helpers.patch_api_data(f"/store/order/{order_id}", {"status":"available"})

    # Validate response status code
    assert response_patch.status_code == 200

    # Validate response message
    assert response_patch.json()["message"] == "Order and pet status updated successfully"

