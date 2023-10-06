from requests_oauthlib import OAuth2Session
import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('API_KEY')
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')

redirect_url = "https://www.thunderclient.com/oauth/callback"
#redirect_url = "https://0ytcgew3yd.execute-api.us-east-1.amazonaws.com/destiny"
base_auth_url = "https://www.bungie.net/en/OAuth/Authorize"
token_url = "https://www.bungie.net/platform/app/oauth/token/"

session = OAuth2Session(client_id=client_id, redirect_uri=redirect_url)

auth_link = session.authorization_url(base_auth_url)
print(f"Authorization link: {auth_link[0]}")

redirect_response = input(f"Paste url link here: ")

#print(f"Redirect URL: {redirect_response}")

print(session.fetch_token(
    client_id=client_id,
    client_secret=client_secret,
    token_url=token_url,
    authorization_response=redirect_response
))


additional_headers = { 'X-API-Key': api_key }
user_details_endpoint = "https://www.bungie.net/Platform/User/GetCurrentBungieNetUser/"
response = session.get(url=user_details_endpoint, headers = additional_headers)

# Print response
print("\n")
print(f"Response Status: {response.status_code}")
print(f"Response Reason: {response.reason}")
print(f"Time Elaspsed: {response.elapsed}")
print(f"Response Text: \n{'-'*15}\n{response.text}")
