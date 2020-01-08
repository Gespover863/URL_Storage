from core import encode, decode
import click


@click.command()
@click.option('--url', type=str, help='The URL that should be encoded')
@click.option('--redirect', type=str,
              help='The key of the url, the address of which you need to display')
def cli(url, redirect):
    if not url and not redirect:
        return click.echo('Specify the function you need.')
    if url and redirect:
        return click.echo('Specify one of two functions, not both!')
    if url:
        return click.echo(encode(url))
    if redirect:
        return click.echo(decode(redirect))
