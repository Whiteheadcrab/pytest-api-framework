import logging
from pytest import mark

from config.api_config import ApiUrls
from utils.common_utils import CommonUtility
from req_res.request.gorest import GoRest
from utils.framework_utils import FrameworkUtils


logger = logging.getLogger(__name__)


class TestGetUser:
    @mark.getUser
    def test_get_user_details(self):

        # Arrange: prepare the user list endpoint and authenticated headers.
        get_user_url = ApiUrls.GET_USER
        headers = CommonUtility.get_custom_header()

        # Act: request the current user list.
        response = FrameworkUtils.fire_api_with_custom_headers("GET",
                                                               request_url=get_user_url,
                                                               request_headers=headers)
        logger.info("Get users response: %s", response)

        # Assert: the API should return a list of users.
        assert isinstance(response, list)

    @mark.createUser
    def test_create_user(self):

        # Arrange: prepare a unique user payload.
        get_user_url = ApiUrls.GET_USER
        headers = CommonUtility.get_custom_header()
        json_create_request = dict(GoRest.CREATE_USER)
        json_create_request['email'] = CommonUtility.get_unique_email()

        # Act: send the user creation request.
        response = FrameworkUtils.fire_api_with_custom_headers("POST",
                                                               request_url=get_user_url,
                                                               request_headers=headers,
                                                               request_json=json_create_request,
                                                               expected_status_code=201)
        logger.info("Create user response: %s", response)

        # Assert: the response should include the same email that was submitted.
        assert response["email"] == json_create_request["email"]
