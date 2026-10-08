import logging

import pytest
import requests


logger = logging.getLogger(__name__)


class FrameworkUtils:

    @staticmethod
    def fire_api_with_custom_headers(request_method='GET',
                                     request_url=None,
                                     request_params=None,
                                     request_json=None,
                                     request_headers=None,
                                     expected_status_code=requests.codes.ok):

        safe_headers = FrameworkUtils._sanitize_headers(request_headers)
        logger.info("Sending %s request to %s", request_method, request_url)
        logger.info("Request headers: %s", safe_headers)
        logger.info("Request params: %s", request_params)
        logger.info("Request json: %s", request_json)

        req = requests.request(request_method,
                               request_url,
                               params=request_params,
                               json=request_json,
                               headers=request_headers)

        logger.info("Response status code: %s", req.status_code)
        logger.info("Response body: %s", req.text)

        try:
            assert req.status_code == expected_status_code, \
                f"API Call fail expected status code is {expected_status_code} , but found is {req.status_code}"
            return req.json()

        except AssertionError:
            logger.exception("API status code assertion failed")
            pytest.fail(f"API Call fail expected status code is {expected_status_code} , but found is {req.status_code}")

    @staticmethod
    def _sanitize_headers(headers):
        if not headers:
            return headers

        sanitized_headers = headers.copy()
        if "Authorization" in sanitized_headers:
            sanitized_headers["Authorization"] = "***"
        return sanitized_headers
