from tests.functional_api_test.functional_param import Functional_Param


class ApiUrls:

    GET_USER = Functional_Param.get_base_endpoint() + "/public/v2/users"

    @staticmethod
    def GET_USER_BY_ID(user_id):
        return Functional_Param.get_base_endpoint() + f"/public/v2/users/{user_id}"
