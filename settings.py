import os


HEROKU_APP_NAME = os.getenv('HEROKU_APP_NAME')


# webhook settings
WEBHOOK_HOST = 'https://igviddwdbot.herokuapp.com'
WEBHOOK_PATH = '/webhook/5075815121:AAHowhsyJHRxik-AfWsUjXdzITlp6iz_vuc'
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

# webserver settings
WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = int(os.getenv('PORT'))