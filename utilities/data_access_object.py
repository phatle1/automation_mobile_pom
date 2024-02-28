import requests
import json
from utilities import config_reader


class data_access_object:
    dev_env: str = "https://dev.api.hutbot.pizzahut.io"
    stag_env: str = "https://dev.api.hutbot.pizzahut.io"
    prod_env: str = "https://dev.api.hutbot.pizzahut.io"

    @staticmethod
    def get_access_token():
        try:
            url = "https://hutbot.auth.eu-west-1.amazoncognito.com/oauth2/token"
            client_id = "5jfhv8387ccnaqcudtaftp3jho"
            client_secret = "14jp8iq6grgehfb9c1211682da8sdns2p3oriatalh5ufbihvc84"
            grant_type = "client_credentials"
            scope = "hutbot/ssam.stores hutbot/ssam.users"
            cookie = "XSRF-TOKEN=0819db07-b017-4765-8e25-debaf17116cd"
            authorization = "Basic MXR0YWdtaHUwdmhmYjBxYWdobXM2Zjlra2w6Z2Z0aGlqNzJmMWNzamNoaW1oa2NldW5xYTJvdjM3dTU0ZzRuZzRtYTRjbDRmbTQwOGIz"

            payload = f'client_id={client_id}&client_secret={client_secret}&grant_type={grant_type}&scope={scope}'
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded',
                'Authorization': authorization,
                'Cookie': cookie
            }

            response = requests.request("POST", url, headers=headers, data=payload)

            response_as_dict = json.loads(response.text)
            print(f"access_token: {response_as_dict.get('access_token')}")
            access_token = response_as_dict.get('access_token')
            return access_token
        except requests.exceptions.Timeout:
            pass
        except requests.exceptions.TooManyRedirects:
            pass
        except requests.exceptions.RequestException as e:
            # catastrophic error. bail.
            raise SystemExit(e)

    @staticmethod
    def get_user_information(yum_id) -> dict:
        try:
            url = f"https://dev.api.hutbot.pizzahut.io/ssam-users/{yum_id}"

            payload = {}
            headers = {
                'Authorization': f'Bearer {data_access_object.get_access_token()}'
            }
            response = requests.request("GET", url, headers=headers, data=payload)
            response_as_dict = json.loads(response.text)
            print(f"user_info: {response_as_dict.get('response_as_dict')}")
            return response_as_dict
        except requests.exceptions.Timeout:
            pass
        except requests.exceptions.TooManyRedirects:
            pass
        except requests.exceptions.RequestException as e:
            # catastrophic error. bail.
            raise SystemExit(e)

    @staticmethod
    def update_user_information(yum_id) -> bool:
        try:
            url = f"https://dev.api.hutbot.pizzahut.io/ssam-users/{yum_id}"
            body: dict[str, any] = config_reader.load_devices_config("../configuration_data/api_body.json")
            user_info = body['apis']['update_user_info']
            payload = json.dumps(user_info)
            headers = {
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {data_access_object.get_access_token()}'
            }
            response = requests.request("PUT", url, headers=headers, data=payload)
            result = str(response)
            print(result)
            return '200' in result
        except requests.exceptions.Timeout:
            pass
        except requests.exceptions.TooManyRedirects:
            pass
        except requests.exceptions.RequestException as e:
            # catastrophic error. bail.
            raise SystemExit(e)

