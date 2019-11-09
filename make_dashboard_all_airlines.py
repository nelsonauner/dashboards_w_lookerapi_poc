import time
import make_airline_dashboard
from lookerapi.rest import ApiException
import lookerapi as looker
import config

# replace with your custom Looker API Host domain and port, if applicable.
base_url = 'https://hack.looker.com:19999/api/3.0/'
#Looker admins can create API3 credentials on Looker's **Admin/Users** page

# instantiate Auth API
unauthenticated_client = looker.ApiClient(base_url)
unauthenticated_authApi = looker.ApiAuthApi(unauthenticated_client)

# authenticate client
token = unauthenticated_authApi.login(client_id=config.client_id, client_secret=config.client_secret)
client = looker.ApiClient(base_url, 'Authorization', 'token ' + token.access_token)

# instantiate Look API client
queryAPI = looker.QueryApi(client)

# Retreive all airlines (or customers, or users, etc)
# Edit here:
body = {
  "model":"faa_redshift",
  "view":"flights",
  "fields":["carriers.name"],
  "limit":"500",
}

resp = queryAPI.run_inline_query("json",body)
carriers = [d['carriers.name'] for d in eval(resp)]
carriers = [name.rstrip() for name in carriers if name]

for carrier in carriers:
    make_airline_dashboard.main.callback(carrier)
