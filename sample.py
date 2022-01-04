import base64
from secrets import *

import environ
import requests

env = environ.Env()
env.read_env(".env")
client_id, client_secret = (env("CLIENT_ID"), env("CLIENT_SECRET"))

# Step 1 - Authorization
url = "https://accounts.spotify.com/api/token"
headers = {}
data = {}

# Encode as Base64
message = f"{client_id}:{client_secret}"
messageBytes = message.encode("ascii")
base64Bytes = base64.b64encode(messageBytes)
base64Message = base64Bytes.decode("ascii")


headers["Authorization"] = f"Basic {base64Message}"
data["grant_type"] = "client_credentials"
print(url, headers, data)
r = requests.post(url, headers=headers, data=data)
print(r)

token = r.json()["access_token"]
print(token)
