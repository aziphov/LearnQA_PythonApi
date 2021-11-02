import time

from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests

class TestUserDelete(BaseCase):

    def test_Ex18_1(self):

        #Login
        login_data = {
            'email': "vinkotov@example.com",
            'password': "1234"
        }
        response2 = MyRequests.post("/user/login", data=login_data)
        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        #Delete
        response3 = MyRequests.delete(f"/user/2",
                                 headers={"x-csrf-token":token},
                                 cookies={"auth_sid":auth_sid}
                                 )

        Assertions.assert_code_status(response3, 400)

        # Get
        response4 = MyRequests.get(f"/user/2",
                                   headers={"x-csrf-token": token},
                                   cookies={"auth_sid": auth_sid}
                                   )
        Assertions.assert_code_status(response4, 200)

    def test_Ex18_2(self):
        #Register
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        password = register_data['password']
        user_id = self.get_json_value(response1, "id")

        #Login
        login_data = {
            'email': email,
            'password': password
        }
        response2 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # Delete
        response3 = MyRequests.delete(f"/user/{user_id}",
                                      headers={"x-csrf-token": token},
                                      cookies={"auth_sid": auth_sid}
                                      )

        Assertions.assert_code_status(response3, 200)

        # Get
        response4 = MyRequests.get(f"/user/{user_id}",
                                   headers={"x-csrf-token": token},
                                   cookies={"auth_sid": auth_sid}
                                   )
        Assertions.assert_code_status(response4, 404)

    def test_Ex18_3(self):
        # Register first user
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email1 = register_data['email']
        password1 = register_data['password']
        user_id1 = self.get_json_value(response1, "id")
        time.sleep(1)

        # Register second user
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email2 = register_data['email']
        password2 = register_data['password']

        # Login first user
        login_data = {
            'email': email1,
            'password': password1
        }
        response2 = MyRequests.post("/user/login", data=login_data)

        auth_sid1 = self.get_cookie(response2, "auth_sid")
        token1 = self.get_header(response2, "x-csrf-token")

        # Login second user
        login_data = {
            'email': email2,
            'password': password2
        }
        response2 = MyRequests.post("/user/login", data=login_data)

        auth_sid2 = self.get_cookie(response2, "auth_sid")
        token2 = self.get_header(response2, "x-csrf-token")

        # Delete first user
        response3 = MyRequests.delete(f"/user/{user_id1}",
                                      headers={"x-csrf-token": token2},
                                      cookies={"auth_sid": auth_sid2}
                                      )

        Assertions.assert_code_status(response3, 200)

        # Get first user
        response4 = MyRequests.get(f"/user/{user_id1}",
                                   headers={"x-csrf-token": token1},
                                   cookies={"auth_sid": auth_sid1}
                                   )
        Assertions.assert_code_status(response4, 200)