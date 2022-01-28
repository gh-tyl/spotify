import environ
import requests

from auth import Auth


class GetRecentlyPlayedTracks:
    def __init__(self):
        self.auth = Auth()
        self.env = environ.Env()
        self.env.read_env(".env")
        self.scope = (self.env("GRPT_SCOPE"),)
        self.grpt_endpoint = self.env("GRPT_ENDPOINT")
        self.access_token = self.env("ACCESS_TOKEN")

    def get_recently_played_tracks(self):
        access_token = self.auth.accessToken()
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            # "Authorization": f"Bearer {access_token}",
            "Authorization": f"Bearer {self.access_token}",
        }
        res = requests.get(self.grpt_endpoint, headers=headers).json()
        return res


if __name__ == "__main__":
    grpt = GetRecentlyPlayedTracks()
    res = grpt.get_recently_played_tracks()
    print(res)
