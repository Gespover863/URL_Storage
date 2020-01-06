# coding=utf-8
from app import app, cli_encode, cli_decode
import click


@click.command()
@click.option('--url', type=str, help='The URL that should be encoded and written to the DB')
@click.option('--redirect', type=str,
              help='The key of the url recorded in DB, the address of which you need to display')
def func(url, redirect):
    with app.app_context():
        if url:
            click.echo(cli_encode(url))
        if redirect:
            click.echo(cli_decode(redirect))
