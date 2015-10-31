import os,sys
import click


@click.group()
def cli():
    pass

@cli.command()
@click.argument('name')
def new(name):
    try:
        os.mkdir(name)
    except OSError:
        print("Directory {} already exists".format(name))
        sys.exit(-1)
