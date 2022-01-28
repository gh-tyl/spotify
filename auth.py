import base64

import environ
import requests
from requests.models import Response


class Auth:
    def __init__(self):
        self.env = environ.Env()
        self.env.read_env(".env")
        self.username = self.env("USERNAME")
        self.client_id, self.client_secret = (
            self.env("CLIENT_ID"),
            self.env("CLIENT_SECRET"),
        )
        self.redirect_uri = self.env("REDIRECT_URI")
        self.scope = self.env("GRPT_SCOPE")
        # self.scope = 'user-read-recently-played'

    def accessToken(self):
        url = "https://accounts.spotify.com/api/token"
        headers = {}
        data = {}
        message = f"{self.client_id}:{self.client_secret}"
        base64Bytes = base64.b64encode(message.encode())
        headers["Authorization"] = f"Basic {base64Bytes.decode()}"
        # data["username"] = self.username
        # data["client_id"] = self.client_id
        # data["client_secret"] = self.client_secret
        data["grant_type"] = "client_credentials"
        # data["response_type"] = "code"
        # data["response_type"] = "token"
        data["redirect_uri"] = self.redirect_uri
        data["scope"] = self.scope
        auth_response = requests.post(url, headers=headers, data=data)
        print("----------------------------------------")
        print(auth_response.json())
        print(auth_response.json()["access_token"])
        print("----------------------------------------")
        access_token = auth_response.json()["access_token"]
        return access_token


if __name__ == "__main__":
    auth = Auth()
    access_token = auth.accessToken()
    print(access_token)
