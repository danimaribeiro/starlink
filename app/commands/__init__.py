import json
import uuid
import click
import requests
from haversine import haversine, Unit

from models import Session
from models.satellite import SpaceTrack


@click.command()
def download_starlink_file():
    response = requests.get("https://github.com/BlueOnionLabs/api-spacex-backend/raw/master/starlink_historical_data.json")

    with open("/usr/src/app/starlink_historical_data.json", "w") as f:
        f.write(response.text)

    click.echo("File downloaded starlink_historical_data.json")


@click.command()
def clear_data():
    with Session() as session:
        session.query(SpaceTrack).delete()
        session.commit()


@click.command()
def import_starlink_data():
    json_data = ""
    with open("/usr/src/app/starlink_historical_data.json", "r") as f:
        json_data = json.loads(f.read())

    with Session() as session:

        item_number = 0

        for item in json_data:
            item_number += 1

            track = SpaceTrack()
            track.eid = uuid.uuid4()
            track.satellite_id = item["id"]
            track.name = item["spaceTrack"]["OBJECT_NAME"]
            track.created_date = item["spaceTrack"]["CREATION_DATE"]
            track.latitude = item["latitude"]
            track.longitude = item["longitude"]
            track.epoch = item["spaceTrack"]["EPOCH"]
            track.velocity_kms = item["velocity_kms"]
            session.add(track)

            if item_number % 100 == 0:
                print(f"Item {item_number} de {len(json_data)}")

        session.commit()


@click.command()
@click.option('--satellite', '-s', required=True)
@click.option('--time', '-t',required=True, type=click.DateTime())
def fetch_position(satellite, time):
    with Session() as session:

        # Broken down to explain
        # Filter by Satellite
        query = session.query(SpaceTrack).filter(
            SpaceTrack.satellite_id == satellite
        )
        # Filter by date
        query = query.filter(
            SpaceTrack.created_date < time
        )
        # Order by created_date and get the first result
        query = query.order_by(SpaceTrack.created_date.desc()).limit(1)

        print(query.all()[0])



@click.command()
@click.option('--latitute', '-la', required=True, type=float)
@click.option('--longitude', '-lo', required=True, type=float)
@click.option('--time', '-t',required=True, type=click.DateTime())
def closest_satellite(latitute, longitude, time):
    with Session() as session:

        query = session.query(SpaceTrack).filter(
            SpaceTrack.created_date < time
        ).limit(1000)

        minimum_distance = float("inf")
        closest_track = None
        for track in query:
            if not track.latitude or not track.longitude:
                continue

            distance = haversine((track.latitude, track.longitude), (latitute, longitude))
            if distance < minimum_distance:
                closest_track = track
                minimum_distance = distance
        
        print("Closest StarLink")
        print(closest_track)
        print(f"Distance from your point: {minimum_distance} KM")