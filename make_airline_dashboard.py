#!/usr/bin/python

"""HELLO CLI
Usage:
    make_airline_dashboard.py airline_name
"""


# cli.py
import click
import pystache
import os
from pathlib import Path

@click.command()
@click.argument('airline_name')
def main(airline_name):
    TEMPLATE_FILENAME = os.path.join(Path.home(), "coalition/join18_hackathon1_faa/airline_dashboard_template.dashboard.lkml.template")
    ADDITIONAL_CHART = os.path.join(Path.home(), "coalition/join18_hackathon1_faa/airline_dashboard_add_cancellation_graph.template")
    OUTPUT_FILENAME = os.path.join(Path.home(), "coalition/join18_hackathon1_faa/airline_dashboard_{{airline_name}}.dashboard.lookml")
    LOOKER_ROOT_URL = 'https://hack.looker.com/dashboards/faa_redshift::airline_dashboard_{{airline_name}}'

    code_friendly_airline_name = airline_name.lower().replace(" ", "_")

    with open(TEMPLATE_FILENAME, 'r') as f:
        dashboard_lookml = f.read()


    # Add an additional chart for certain airlines:
    if 'Alaska' in airline_name:
        with open(ADDITIONAL_CHART, 'r') as f:
            additional_chart_lookml = f.read()
            print(f"Adding cancellation graph for {airline_name}")
            dashboard_lookml += additional_chart_lookml


    broker_dashboard_lookml = pystache.render(dashboard_lookml, {'airline_name': airline_name, 'code_friendly_airline_name': code_friendly_airline_name})

    OUTPUT_FILENAME = pystache.render(OUTPUT_FILENAME, {'airline_name': code_friendly_airline_name})

    with open(OUTPUT_FILENAME, 'w') as f:
        f.write(broker_dashboard_lookml)


    print(f"Dashboard for {airline_name} is locally at airline_dashboard_{code_friendly_airline_name}.dashboard.lookml \nWill be on looker at {pystache.render(LOOKER_ROOT_URL, {'airline_name': code_friendly_airline_name})}\n")

if __name__ == "__main__":
    main()
