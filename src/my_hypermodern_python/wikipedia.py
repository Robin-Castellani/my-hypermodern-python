"""
Get data from the Wikipedi API.
"""

import requests
import click


def random_page(lang):
    api_url = f'https://{lang}.wikipedia.org/api/rest_v1/page/random/summary'

    try:
        with requests.get(api_url) as response:
            response.raise_for_status()  # if bad status, raises exception
            return response.json()  # the API provide its data in json
    except requests.HTTPError:
        raise click.ClickException(
            f'Wikipedia API not reachable OR given language "{lang}" not valid'
        )
    except requests.exceptions.ConnectionError:
        raise click.ClickException(
            f'Given language "{lang}" not valid'
        )
