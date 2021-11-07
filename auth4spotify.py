import environ
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials

class Auth:
    def __init__(self):
        self.env = environ.Env()
        self.env.read_env('.env')
        self.username, self.client_id, self.client_secret, self.scope = self.env('USERNAME'), self.env('CLIENT_ID'), self.env('CLIENT_SECRET'), self.env('SCOPE')

    def auth(self):
        client_credentials_manager = SpotifyClientCredentials(self.client_id, self.client_secret)
        spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
        return spotify

    def authWithScope(self):
        redirect_uri = "http://example.com"
        token = util.prompt_for_user_token(username=self.username,
                                        scope=self.scope,
                                        client_id=self.client_id,
                                        client_secret=self.client_secret,
                                        redirect_uri=redirect_uri)
        spotify = spotipy.Spotify(auth=token)
        return spotify
