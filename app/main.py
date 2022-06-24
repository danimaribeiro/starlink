import click
import commands


@click.group()
def entry_point():
    pass

entry_point.add_command(commands.download_starlink_file)
entry_point.add_command(commands.import_starlink_data)
entry_point.add_command(commands.clear_data)
entry_point.add_command(commands.fetch_position)
entry_point.add_command(commands.closest_satellite)

if __name__ == "__main__":
    entry_point()