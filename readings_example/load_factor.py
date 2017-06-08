from datetime import datetime, timedelta
import os
import json
from optparse import OptionParser

from oauthlib.oauth2 import LegacyApplicationClient
from requests_oauthlib import OAuth2Session

# Pass meter UUID via command line E.g.,
#   > python load_factor.py --meter a49816dc88b511e5b6315254008f220d
parser = OptionParser()
parser.add_option("-m", "--meter", action="store",
  type="string", dest="meter", help="Meter ID.")
options, _ = parser.parse_args()
meter_uuid = options.meter

# Load BOS credentials from environment variables
client_id = os.environ['BOS_CLIENT_ID']
client_secret = os.environ['BOS_CLIENT_SECRET']
username = os.environ['BOS_USERNAME']
password = os.environ['BOS_PASSWORD']

# Get authorized client token
oauth = OAuth2Session(client=LegacyApplicationClient(client_id=client_id))
token = oauth.fetch_token(token_url='https://api.buildingos.com/o/token/',
        username=username, password=password, client_id=client_id,
        client_secret=client_secret)
client = OAuth2Session(client_id, token=token)

# Construct URL to query quarter hour data from previous week
READINGS_URL = (
  'https://api.buildingos.com/meters/{meter_uuid}/data'
  '?start={start}&end={end}&order=asc&resolution=quarterhour'
)
end = datetime.now()
start = end - timedelta(days=7)
api_url = READINGS_URL.format(
  meter_uuid=meter_uuid,
  start=start.strftime('%Y-%m-%d'),
  end=end.strftime('%Y-%m-%d'),
)

# Call the API and calculate load factor
response = client.get(api_url)
data = json.loads(response.content) # Load JSON into Python data structure
values = [r['value'] for r in data['data']] # Extract consumption readings

max_demand = max(values)
avg_demand = sum(values) / len(values)
print "Max: %s" % max_demand
print "Mean: %s" % avg_demand
print "Load factor: %s%%" % round(100 * avg_demand / max_demand, 1)
