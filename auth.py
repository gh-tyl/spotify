import environ
import requests


class Auth:
    def __init__(self):
        self.env = environ.Env()
        self.env.read_env(".env")
        self.username, self.client_id, self.client_secret, self.scope = (
            self.env("USERNAME"),
            self.env("CLIENT_ID"),
            self.env("CLIENT_SECRET"),
            self.env("SCOPE"),
        )
        self.auth_endpoint, self.redirect_uri = (
            self.env("AUTH_ENDPOINT"),
            self.env("REDIRECT_URI"),
        )

    def accessToken(self):
        # headers = {'Authorization':f'Basic <base64 encoded {self.client_id}:{self.client_secret}>', 'Content-Type':'application/x-www-form-urlencoded'}
        # params = {'scope':self.scope, 'grant_type': 'client_credentials'}
        params = {
            "grant_type": "client_credentials",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "scope": self.scope,
        }
        auth_response = requests.post(
            self.auth_endpoint,
            {
                "grant_type": "client_credentials",
                "client_id": self.client_id,
                "client_secret": self.client_secret,
                "scope": self.scope,
            },
        )
        # auth_response = requests.post(
        #     url=self.auth_endpoint,
        #     # headers=headers,
        #     params=params,
        #     # redirect_uri=self.redirect_uri
        #     )
        access_token = auth_response.json
        print(access_token)
        return access_token


if __name__ == "__main__":
    auth = Auth()
    access_token = auth.accessToken()
    print(access_token)
