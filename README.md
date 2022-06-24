

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






