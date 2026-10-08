import logging

from config.api_config import ApiUrls
from req_res.request.gorest import GoRest
from utils.common_utils import CommonUtility
from utils.framework_utils import FrameworkUtils


logger = logging.getLogger(__name__)


def test_api_chaining():
    # Arrange: prepare the endpoint, authenticated headers, and a unique user payload.
    get_user_url = ApiUrls.GET_USER
    logger.info("GET user URL: %s", get_user_url)

    headers = CommonUtility.get_custom_header()
    email = CommonUtility.get_unique_email()
    logger.info("Testing unique email: %s", email)
    json_create_request = dict(GoRest.CREATE_USER)
    json_create_request["email"] = email
    logger.info("Create user payload: %s", json_create_request)

    # Act: create a user first so the follow-up GET can use a fresh id.
    response2 = FrameworkUtils.fire_api_with_custom_headers("POST",
                                                            request_url=get_user_url,
                                                            request_headers=headers,
                                                            request_json=json_create_request,
                                                            expected_status_code=201)
    logger.info("Create user response: %s", response2)

    user_id = response2['id']
    logger.info("Created user id: %s", user_id)

    get_user_id_url = ApiUrls.GET_USER_BY_ID(user_id)
    logger.info("GET user by id URL: %s", get_user_id_url)

    # Act: retrieve the newly created user by id.
    response = FrameworkUtils.fire_api_with_custom_headers("GET",
                                                           request_url=get_user_id_url,
                                                           request_headers=headers)
    logger.info("Get user response: %s", response)
    get_response_id = response['id']

    # Assert: the GET response should return the same id from the POST response.
    assert user_id == get_response_id

