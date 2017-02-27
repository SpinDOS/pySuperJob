import requests
import os

__all__= ['make_superjob_request']

SUPERJOB_API_KEY = os.environ.get('SUPERJOB_API_KEY')


def make_superjob_request(relative_url, url_params=None):
    headers = {'X-Api-App-Id' : SUPERJOB_API_KEY}
    response = requests.get('https://api.superjob.ru/2.0/%s' % relative_url,
                            params=url_params, headers=headers)
    return response.json()
