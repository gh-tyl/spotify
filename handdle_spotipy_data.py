import copy

import pandas as pd


def handdle_grpt_data(recently_played, json_path):
    csv_path = json_path.replace(".json", ".csv")
    df = pd.json_normalize(recently_played["items"])

    # backup
    df["track.artists.backup"] = copy.deepcopy(df["track.artists"])
    # convert json to artist name
    artists = []
    for values in df["track.artists"]:
        artists_ = ""
        if len(values) >= 2:
            for val in values:
                artists_ += val.get("name") + ", "
            artists_ = artists_[:-2]
            artists.append(artists_)
        else:
            for val in values:
                artists.append(val.get("name"))

    # update artists
    df["track.artists"] = artists

    # convert to jst
    df = df.sort_values("played_at").reset_index(drop=True)
    df["played_at"] = pd.to_datetime(df["played_at"])
    df["played_at"] = [
        played_at.tz_convert("Asia/Tokyo") for played_at in df["played_at"]
    ]

    # save data as csv
    df.to_csv(csv_path)
    print("path is", csv_path)
