import logging

from config.api_config import ApiUrls
from req_res.request.gorest import GoRest
from utils.common_utils import CommonUtility
from utils.framework_utils import FrameworkUtils


logger = logging.getLogger(__name__)


def test_url():
    # Arrange: prepare the user endpoint, headers, and a unique create-user payload.
    get_user_url = ApiUrls.GET_USER
    logger.info("GET user URL: %s", get_user_url)
    email = CommonUtility.get_unique_email()
    logger.info("Testing unique email: %s", email)
    json_create_request = dict(GoRest.CREATE_USER)
    json_create_request["email"] = email
    logger.info("Create user payload: %s", json_create_request)

    headers = CommonUtility.get_custom_header()

    # Act: verify the users endpoint is reachable.
    response = FrameworkUtils.fire_api_with_custom_headers("GET",
                                                           request_url=get_user_url,
                                                           request_headers=headers)
    logger.info("Get users response: %s", response)

    # Act: create a user with the unique payload.
    response2 = FrameworkUtils.fire_api_with_custom_headers("POST",
                                                            request_url=get_user_url,
                                                            request_headers=headers,
                                                            request_json=json_create_request,
                                                            expected_status_code=201)
    logger.info("Create user response: %s", response2)

    # Assert: both API calls should return JSON payloads in the expected shape.
    assert isinstance(response, list)
    assert response2["email"] == json_create_request["email"]
