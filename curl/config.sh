source ../.env
curl -X POST $AUTH_ENDPOINT \
-H "Authorization: Basic <base64 encoded $CLIENT_ID:$CLIENT_SECRET>" \
-H "Content-Type: application/x-www-form-urlencoded" \
-d grant_type=client_credentials


# # Get recently played tracks
# curl -X GET $ENDPOINT \
# -H "Accept: application/json" \
# -H "Content-Type: application/json" \
# -H "Authorization: Bearer "
