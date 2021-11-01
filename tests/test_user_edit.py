import time

from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.my_requests import MyRequests

class TestUserEdit(BaseCase):

    def test_edit_just_created_user(self):
        #Register
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        first_name = register_data['firstName']
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

        #Edit
        new_name = "Change Name"

        response3 = MyRequests.put(f"/user/{user_id}",
                                 headers={"x-csrf-token":token},
                                 cookies={"auth_sid":auth_sid},
                                 data={"firstName":new_name}
                                 )

        Assertions.assert_code_status(response3, 200)

        #Get
        response4 = MyRequests.get(f"/user/{user_id}",
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid}
                                 )

        Assertions.assert_json_value_by_name(response4, "firstName", new_name, "Wrong name of the user after edit")

    def test_Ex17_1(self):
        #Register
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        user_id = self.get_json_value(response1, "id")

        #Edit
        new_name = "Change Name"

        response3 = MyRequests.put(f"/user/{user_id}",
                                 headers={"x-csrf-token":"111"},
                                 cookies={"auth_sid":"222"},
                                 data={"firstName":new_name}
                                 )

        Assertions.assert_code_status(response3, 400)

    def test_Ex17_2(self):
        # Register first user
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email1 = register_data['email']
        first_name1 = register_data['firstName']
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

        # Edit first user
        new_name = "Change Name"

        response3 = MyRequests.put(f"/user/{user_id1}",
                                   headers={"x-csrf-token": token2},
                                   cookies={"auth_sid": auth_sid2},
                                   data={"firstName": new_name}
                                   )

        Assertions.assert_code_status(response3, 200)

        # Get first user
        response4 = MyRequests.get(f"/user/{user_id1}",
                                   headers={"x-csrf-token": token1},
                                   cookies={"auth_sid": auth_sid1}
                                   )

        Assertions.assert_json_value_by_name(response4, "firstName", first_name1, "Wrong name of the user after edit")

    def test_Ex17_3(self):
        # Register
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        first_name = register_data['firstName']
        password = register_data['password']
        user_id = self.get_json_value(response1, "id")

        # Login
        login_data = {
            'email': email,
            'password': password
        }
        response2 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # Edit
        new_email = "123mail.ru"

        response3 = MyRequests.put(f"/user/{user_id}",
                                   headers={"x-csrf-token": token},
                                   cookies={"auth_sid": auth_sid},
                                   data={"email": new_email}
                                   )

        Assertions.assert_code_status(response3, 400)

        # Get
        response4 = MyRequests.get(f"/user/{user_id}",
                                   headers={"x-csrf-token": token},
                                   cookies={"auth_sid": auth_sid}
                                   )

        Assertions.assert_json_value_by_name(response4, "email", email, "Wrong email of the user after edit")

    def test_Ex17_4(self):
        #Register
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        first_name = register_data['firstName']
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

        #Edit
        new_first_name = "a"

        response3 = MyRequests.put(f"/user/{user_id}",
                                 headers={"x-csrf-token":token},
                                 cookies={"auth_sid":auth_sid},
                                 data={"firstName":new_first_name}
                                 )

        Assertions.assert_code_status(response3, 400)

        #Get
        response4 = MyRequests.get(f"/user/{user_id}",
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid}
                                 )

        Assertions.assert_json_value_by_name(response4, "firstName", first_name, "Wrong name of the user after edit")