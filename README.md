# Scaling Data Delivery with LookML Dashboards & LookerAPI

A proof of concept tool that should be easy to start from
This demo was done on Looker's flights data


# Setup

1. Install requirements with `pipenv`

2. Set up the API-related auth details in a `config.py` file with the following
contents:

```
client_id = 'valid_api_client_id'
client_secret = 'valid_api_client_secret'
looker_root_url = 'https://yourinstance.looker.com'
```

# Usage

`python make_airline_dashboard.py 'Alaska Airlines'` should work without any
additional work

`make_dashboard_all_airlines.py` uses the LookerAPI to get all the airlines in
the sample data. Subsitute `carriers.name` with whatever `view.field` your
customers are stored in

`schedule_dashboard_delivery_all_airlines.ipynb` contains code to show how to
retrieve all of your dashboards with the Looker API and set up scheduled jobs
for them

# Contributing

Feel free to open pull requests or issues
