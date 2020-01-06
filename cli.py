# coding=utf-8
from app import app, cli_encode, cli_decode
import click


@click.command()
@click.option('--url', type=str)  # Need typing used
@click.option('--redirect', type=str)
def func(url, redirect):
    with app.app_context():
        if url:
            click.echo(cli_encode(url))
        if redirect:
            click.echo(cli_decode(redirect))
