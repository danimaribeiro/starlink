
## Steps

First step to initialize the database

    make run-migrations


Download the Starlink json file

    make download-data

Then load the starlink file into the database

    make import-data

If you need to reimport, first you have to delete the data to avoid errors inserting duplicated items

    make clear-data

Now you can query the data, here are some commands

    make fetch-satellite-position

    make closest-satellite

Or you can change the parameters for those queries

    docker compose run web python main.py fetch-position -s 5eed770f096e590006985610 -t 2021-01-26T02:30:01

    docker compose run web python main.py closest-satellite -la -27.686170 -lo -48.499287 -t 2022-06-24T02:30:01


## Some outputs

##### Fetch position by time and satellite

    docker compose run web python main.py fetch-position -s 5eed770f096e590006985610 -t 2021-01-26T02:30:01
    [+] Running 1/0
     ⠿ Container blue-onion-db-1  Running                                                                                     0.0s
    SpaceTrack(
            epoch=2021-01-25 20:20:03.823008
            eid=9e0feecd-f513-4a47-8f7d-9f001e797017
            latitude=25.453949445394215
            created_date=2021-01-26 02:30:00
            satellite_id=5eed770f096e590006985610
            name=STARLINK-76
            longitude=109.0
            velocity_kms=7.659206017683536
    )

##### Closest satellite

    docker compose run web python main.py closest-satellite -la -27.686170 -lo -48.499287 -t 2022-06-24T02:30:01
    [+] Running 1/0
     ⠿ Container blue-onion-db-1  Running                                                                                     0.0s
    Closest StarLink
    SpaceTrack(
            epoch=2021-01-25 15:55:48.202176
            eid=651622dd-f7f5-4d5e-8283-327e33077f32
            latitude=-40.536907961367824
            created_date=2021-01-26 02:30:00
            satellite_id=5eed7714096e590006985689
            name=STARLINK-1097
            longitude=1.0
            velocity_kms=7.578890237952381
    )
    Distance from your point: 4709.078119645219 KM



