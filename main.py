from dockingFormatter import DockingFormatter
# import sys 
# import argparse

# parse = argparse.ArgumentParser()
# parse.add_argument("-s")
# args = parse.parse_args()

# df = DockingFormatter()
# df.findAffinityForCompound(args.s)

import click 

@click.command()
@click.argument('filename', type=click.Path(exists=True))
def run(filename):
    df = DockingFormatter()
    df.findAffinityForCompound(click.format_filename(filename))
    click.echo("Docker log formatted to xlsx file")

