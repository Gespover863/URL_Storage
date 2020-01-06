# coding=utf-8
from app import app, cli_interface
import click


@click.command()
@click.option('--url', type=str, help='The URL that should be encoded and written to the DB')
@click.option('--redirect', type=str,
              help='The key of the url recorded in DB, the address of which you need to display')
def cli(url, redirect):
    with app.app_context():
        if not url and not redirect:
            return click.echo('Specify the function you need. If you are at a loss, select the "--help" flag')
        if url and redirect:
            return click.echo('Specify one of two functions, not both!')
        if url:
            return click.echo(cli_interface(url, 'encode'))
        if redirect:
            return click.echo(cli_interface(redirect, 'decode'))
