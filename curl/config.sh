source ../.env
curl -X POST $AUTH_ENDPOINT \
-H "Authorization: Basic <base64 encoded 934d5a606c5f4b5da61bd262cfc837b6:c4b714c5f0254445b823f6bf8f0d182a>" \
# -H "Authorization: Basic <base64 encoded $CLIENT_ID:$CLIENT_SECRET>" \
# -H "Content-Type: application/x-www-form-urlencoded" \
"Content-Type: application/x-www-form-urlencoded" \
-d grant_type=client_credentials


# # Get recently played tracks
# curl -X GET $ENDPOINT \
# -H "Accept: application/json" \
# -H "Content-Type: application/json" \
# -H "Authorization: Bearer BQC3W0x5eAsK-Hm9CamBmcSQ--4hrJx8ZO57P7bsw_xZ4Lvovj9DyPD_ZsYdM3HLHv2pTOqLWy9ReNhFC4klI7oohN-Wv8W6Hz8m9uRZ5BQCXNoFuHJmIa49COgK8dsSODnxQdG_qzOGAI0t4EQsUn7T0SSZDFhM6_neN86p"
