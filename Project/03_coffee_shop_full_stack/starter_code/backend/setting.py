from dotenv import load_dotenv
import os
load_dotenv()

AUTH0_DOMAIN = os.environ.get('dev-4mgv-p94.us.auth0.com')
ALGORITHMS =os.environ.get('RS256')
API_AUDIENCE = os.environ.get('CoffeeShop')