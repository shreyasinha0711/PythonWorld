import requests
import json

KEY_ID = "11222"

get_token_path = 'https://www.google.com/{"key":"' + KEY_ID + '"}'
post_agent_path = 'https://www.google.com/post'


def lambda_handler(event, context):
    def get_jwt_token():
        try:
            get_token_request = requests.get(get_token_path, timeout=5)
            get_token_request.raise_for_status()
            token_response = get_token_request.json()["d"]["a"]
            print(token_response)
            print("\n")
        except requests.exceptions.HTTPError as errh:
            print(errh)
        except requests.exceptions.ConnectionError as errc:
            print(errc)
        except requests.exceptions.Timeout as errt:
            print(errt)
        except requests.exceptions.RequestException as err:
            print(err)
        except KeyError:
            print("The app key is not valid or Expired")
        return token_response

    def post_api_request():
        token_value = get_jwt_token()

        payload = {"runType": "FORCED", "destinationLocation": "https://s3_bucket_name.s3.amazonaws.com/"}
        headers = {"Authorization": token_value,
                   "Content-Type": "application/json",
                   }
        post_api_request = requests.post(post_agent_path, data=json.dumps(payload), headers=headers)
        post_api_response = post_api_request.content
        print(post_api_response)
        print("\n")
        return post_api_response

    post_api_request()

    return True
