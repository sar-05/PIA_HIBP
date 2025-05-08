from os import getenv
from dotenv import load_dotenv

load_dotenv('.env')
hibp_key = getenv('HIBP_KEY')
app_id = getenv('APPLICATION_ID')
item_id = getenv('ITEM_ID')
