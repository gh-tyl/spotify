import datetime
import json
import os
import time

import auth_spotipy


def main(event=False, context=False):
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

    # setup
    auth = auth_spotipy.Auth()
    spotify = auth.authWithScope()

    recently_played = spotify.current_user_recently_played(limit=50)
    with open(json_path, "w", encoding="utf-8") as f:
        f.write(json.dumps(recently_played))
    print("path is", json_path)


if __name__ == "__main__":
    while True:
        main()
        time.sleep(10000)
