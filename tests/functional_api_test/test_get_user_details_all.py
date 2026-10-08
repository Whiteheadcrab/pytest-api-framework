import logging
from pytest import mark

from config.api_config import ApiUrls
from utils.common_utils import CommonUtility
from utils.framework_utils import FrameworkUtils


logger = logging.getLogger(__name__)


class TestGetUserAll:
    @mark.getUser
    @mark.user1
    def test_get_user_details_valid(self):

        # Arrange: prepare the user list endpoint and authenticated headers.
        get_user_url = ApiUrls.GET_USER
        headers = CommonUtility.get_custom_header()

        # Act: call the users endpoint with valid authorization.
        response = FrameworkUtils.fire_api_with_custom_headers("GET",
                                                               request_url=get_user_url,
                                                               request_headers=headers)

        # Assert: a successful request should return a JSON list of users.
        assert isinstance(response, list)
        logger.info("Authorized users response: %s", response)

    @mark.getUser
    @mark.user1
    def test_get_user_invalid_auth(self):

        # Arrange: replace the valid bearer token with an invalid value.
        get_user_url = ApiUrls.GET_USER
        headers = CommonUtility.get_custom_header()
        headers["Authorization"] = "wrong"

        # Act: call the users endpoint with invalid authorization.
        response = FrameworkUtils.fire_api_with_custom_headers("GET",
                                                               request_url=get_user_url,
                                                               request_headers=headers,
                                                               expected_status_code=401)

        # Assert: the API should return an authorization error payload.
        assert "message" in response
        logger.info("Invalid auth response: %s", response)
