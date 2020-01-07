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
        return click.echo(cli_interface(url, 'encode'))
    if redirect:
        return click.echo(cli_interface(redirect, 'decode'))


def cli_interface(url_or_code, func):
    if func == 'encode':
        return encode(url_or_code)
    elif func == 'decode':
        return decode(url_or_code)
    else:
        return 'Something incredible just happened.'
