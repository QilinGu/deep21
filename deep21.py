'''
deep21 client
'''

import sys
import click

from two1.commands.config import Config
from two1.lib.wallet import Wallet
from two1.lib.bitrequests import BitTransferRequests

SERVER = 'http://sanya.westus.cloudapp.azure.com'
PORT_MAPPINGS = {'coco': 8200,
                 'wikipedia': 8201,
                 'scene': 8202}
MODEL_IDS = {'coco': 5090,
             'wikipedia': 5104,
             'scene': 5291}
MODEL_API = {'coco': 'describe',
             'wikipedia': 'describe',
             'scene': 'classify'}

#set up bitrequest client for BitTransfer requests
wallet = Wallet()
username = Config().username
requests = BitTransferRequests(wallet, username)

@click.command()
@click.option('--model', default='coco', help='Deep learning model to use: coco (captioning trained on COCO dataset), wikipedia (captioning trained on Wikipedia dataset), scene (scene classification using SUN dataset labels)')
@click.argument('img_url')
def cli(model, img_url):
    if model not in PORT_MAPPINGS:
        click.echo('Invalid model chosen')

    # Send request to server with user input text and user's wallet address for payment
    url = '{}:{}/api/{}?model_id={}&image_url={}'.format(SERVER, PORT_MAPPINGS[model], MODEL_API[model], img_url)
    response = requests.get(url)

    # Print the caption/classification out to the terminal
    click.echo(response.text)