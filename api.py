from rich import print
import twitter
from env import *

# api of the account you want to copy the "followers" and "following"
api_1 = twitter.Api(consumer_key=API_KEY_1,
                      consumer_secret=API_KEY_SECRET_1,
                      access_token_key=ACCESS_TOKEN_1,
                      access_token_secret=ACCESS_TOKEN_SECRET_1)

print(api.VerifyCredentials())

