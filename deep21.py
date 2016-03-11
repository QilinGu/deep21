'''
deep21 client
'''

import sys
import click

from two1.commands.config import Config
from two1.lib.wallet import Wallet
from two1.lib.bitrequests import BitTransferRequests

MODELS = {'coco', 'wikipedia', 'scene'}

#set up bitrequest client for BitTransfer requests
wallet = Wallet()
username = Config().username
requests = BitTransferRequests(wallet, username)

@click.command()
@click.option('--model', default='coco', help='Deep learning model to use: coco (captioning trained on COCO dataset), wikipedia (captioning trained on Wikipedia dataset), scene (scene classification using SUN dataset labels)')
# Uncomment this line to use your own server
# @click.option('--server', default='localhost:5000', help='ip:port to connect to')
# Comment this line to not use my server
@click.option('--server', default='10.254.18.23:5000', help='ip:port to connect to')
@click.argument('img_url', required=False)
def cli(model, server, img_url):
    if model not in MODELS:
        click.echo('Error: Invalid model chosen')
        return

    if not img_url:
        img_url = click.get_text_stream('stdin').read()

    # Send request to server with user input text and user's wallet address for payment
    sel_url = 'http://{}/deep?model={}&img_url={}&payout_address={}'
    response = requests.get(sel_url.format(server, model, img_url, wallet.get_payout_address()))

    # Print the caption/classification out to the terminal
    click.echo(response.text)

if __name__ == '__main__':
    cli()