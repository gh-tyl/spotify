import os
import datetime
from pytz import timezone
from dateutil import parser
import pandas as pd
import auth4spotify
auth = auth4spotify.Auth()

# setup
# scope = "user-read-recently-played"
spotify = auth.authWithScope()

recently_played = spotify.current_user_recently_played(limit=50)
# print(recently_played)
pre_df = pd.json_normalize(recently_played['items'])
df = pre_df.copy()

# backup
df['track.artists.backup'] = df['track.artists'].copy()
# convert json to artist name
artists = []
for values in df['track.artists']:
    pre_artists = ''
    if len(values) >= 2:
        for val in values:
            pre_artists += val.get('name') + ', '
        pre_artists = pre_artists[:-2]
        artists.append(pre_artists)
    else:
        for val in values:
            artists.append(val.get('name'))

# update artists
df['track.artists'] = artists

# convert to jst
df = df.sort_values('played_at').reset_index(drop=True)
jst_list = [parser.parse(time).astimezone(timezone('Asia/Tokyo')) for time in df.played_at]
time_list = []
for i in jst_list:
    hour, minute, second, microsecond = str(i.hour), str(i.minute), str(i.second), str(i.microsecond)
    if len(hour) == 1:
        hour = '0'+hour
    if len(minute) == 1:
        minute = '0'+minute
    if len(second) == 1:
        second = '0'+second
    if len(microsecond) == 5:
        microsecond = '0'+microsecond
    time_list.append(hour+':'+minute+':'+second+'.'+microsecond)
df['jst'] = time_list

# record time for filename
dt_now = datetime.datetime.now()
jst_list = [dt_now.year, dt_now.month, dt_now.day, dt_now.hour]
time_list = ['0'+str(time)  if len(str(time)) == 1 else str(time) for time in jst_list]
idir_path = 'data'
if not os.path.isdir(idir_path):
    os.makedirs(idir_path)
file_path = f'{idir_path}/{time_list[0]}{time_list[1]}{time_list[2]}{time_list[3]}_recently.csv'

# save data as csv
df.to_csv(file_path)
print('path is', file_path)
