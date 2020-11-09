from twython import Twython

APP_KEY = "rellenar"
APP_SECRET = "rellenar"
OAUTH_TOKEN = "rellenar"
OAUTH_TOKEN_SECRET = "rellenar"


twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

photo = open('Betis.png', 'rb')
#photo = open('Sevilla.png', 'rb')

response = twitter.upload_media(media=photo)
twitter.update_status(status="Musho Betis!", media_ids=[response['media_id']])
#twitter.update_status(status="Viva el Sevilla!", media_ids=[response['media_id']])

