import click
import requests


@click.command()
def download_starlink_file():
    response = requests.get("https://github.com/BlueOnionLabs/api-spacex-backend/raw/master/starlink_historical_data.json")

    with open("/usr/src/app/starlink_historical_data.json", "w") as f:
        f.write(response.text)

    click.echo("File downloaded starlink_historical_data.json")


@click.command()
def import_starlink_data():
    print("hello world")