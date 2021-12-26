import os
# import copy
import json
import datetime
# import pandas as pd
import auth_spotify

def main():
    # record time for filename
    dt_now = datetime.datetime.now()
    jst_list = [dt_now.year, dt_now.month, dt_now.day, dt_now.hour]
    time_list = ['0'+str(time)  if len(str(time)) == 1 else str(time) for time in jst_list]
    idir_path = 'data'
    if not os.path.isdir(idir_path):
        os.makedirs(idir_path)
    json_path = f'{idir_path}/{time_list[0]}{time_list[1]}{time_list[2]}{time_list[3]}_recently.json'
    csv_path = f'{idir_path}/{time_list[0]}{time_list[1]}{time_list[2]}{time_list[3]}_recently.csv'

    # setup
    auth = auth4spotify.Auth()
    spotify = auth.authWithScope()

    recently_played = spotify.current_user_recently_played(limit=50)
    with open(json_path, 'w', encoding='utf-8') as f:
        f.write(json.dumps(recently_played))
    print('path is', json_path)

    # df = pd.json_normalize(recently_played['items'])

    # # backup
    # df['track.artists.backup'] = copy.deepcopy(df['track.artists'])
    # # convert json to artist name
    # artists = []
    # for values in df['track.artists']:
    #     artists_ = ''
    #     if len(values) >= 2:
    #         for val in values:
    #             artists_ += val.get('name') + ', '
    #         artists_ = artists_[:-2]
    #         artists.append(artists_)
    #     else:
    #         for val in values:
    #             artists.append(val.get('name'))

    # # update artists
    # df['track.artists'] = artists

    # # convert to jst
    # df = df.sort_values('played_at').reset_index(drop=True)
    # df['played_at'] = pd.to_datetime(df['played_at'])
    # df['played_at'] = [played_at.tz_convert('Asia/Tokyo') for played_at in df['played_at']]

    # # save data as csv
    # df.to_csv(csv_path)
    # print('path is', csv_path)

if __name__=='__main__':
    main()