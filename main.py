#!/home/ubuntu/spotify/.venv/bin/python3
import datetime
import json
import os
import time

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

    def save_json(self, res):
        # record time for filename
        dt_now = datetime.datetime.now()
        jst_list = [dt_now.year, dt_now.month, dt_now.day, dt_now.hour]
        time_list = [
            "0" + str(time) if len(str(time)) == 1 else str(time) for time in jst_list
        ]
        idir_path = "data"
        if not os.path.isdir(idir_path):
            try:
                os.makedirs(idir_path)
            except Exception as e:
                idir_path = "/tmp/data"
                os.makedirs(idir_path)
                print(f"Error is {e}")
        json_path = f"{idir_path}/{time_list[0]}{time_list[1]}{time_list[2]}{time_list[3]}_recently.json"
        with open(json_path, "w", encoding="utf-8") as f:
            f.write(json.dumps(res))
        print("path is", json_path)


if __name__ == "__main__":
    try:
        while True:
            grpt = GetRecentlyPlayedTracks()
            res = grpt.get_recently_played_tracks()
            grpt.save_json(res)
            time.sleep(10000)
            # print(res)

    except KeyboardInterrupt:
        print("----DONE----")
