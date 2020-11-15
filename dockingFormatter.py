
# from DockingFormatter import DockingFormatter 
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
    print("Hello it's a docking log")
    click.echo(click.format_filename(filename))

