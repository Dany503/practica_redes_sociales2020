from twython import Twython

APP_KEY = "rellenar"
APP_SECRET = "rellenar"
OAUTH_TOKEN = "rellenar"
OAUTH_TOKEN_SECRET = "rellenar"


twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

twitter.update_status(status="Mi primer tweet!! :D")

