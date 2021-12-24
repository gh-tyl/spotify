from environ import environ
from spotipy import spotipy
from spotipy import spotipy.util as util
from spotipy.spotipy.oauth2 import SpotifyClientCredentials

class Auth:
    def __init__(self):
        self.env = environ.Env()
        self.env.read_env('.env')
        self.username, self.client_id, self.client_secret, self.scope = self.env('USERNAME'), self.env('CLIENT_ID'), self.env('CLIENT_SECRET'), self.env('SCOPE')
        pass

    def auth(self):
        client_credentials_manager = SpotifyClientCredentials(self.client_id, self.client_secret)
        # client_credentials_manager = SpotifyClientCredentials('0d4032665c5f405f9dc34c6a4a183013', 'd2b4a62e21ab447f81b75ee1e0428c64')
        spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
        return spotify

    def authWithScope(self):
        redirect_uri = "http://example.com"
        token = util.prompt_for_user_token(username=self.username,
                                        scope=self.scope,
                                        client_id=self.client_id,
                                        client_secret=self.client_secret,
                                        redirect_uri=redirect_uri)
        # token = util.prompt_for_user_token(username='fyj5u5er19cf0zmw8sdy1drc1',
        #                                 scope='user-read-recently-played',
        #                                 client_id='0d4032665c5f405f9dc34c6a4a183013',
        #                                 client_secret='d2b4a62e21ab447f81b75ee1e0428c64',
        #                                 redirect_uri=redirect_uri)
        spotify = spotipy.Spotify(auth=token)
        return spotify
