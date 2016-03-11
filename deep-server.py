'''
deep21 server
'''

from flask import Flask, request
import requests
import pprint
import yaml, json

from two1.lib.wallet import Wallet
from two1.lib.bitserv.flask import Payment

SERVER = 'http://sanya.westus.cloudapp.azure.com'
PORT_MAPPING = {'coco': 8200,
                 'wikipedia': 8201,
                 'scene': 8202}
MODEL_API = {'coco': 'describe',
             'wikipedia': 'describe',
             'scene': 'classify'}
MODEL_ID = {'coco': 5090,
             'wikipedia': 5104,
             'scene': 5291}

# set up server sie wallet
app = Flask(__name__)
wallet = Wallet()
payment = Payment(app, wallet)

@app.route('/deep')
@payment.required(2500)
def deep():
    print(request.get_data)

    model = request.args.get('model')
    img_url = request.args.get('img_url')

    if model not in PORT_MAPPING:
        return 'Error: Invalid model chosen'

    url = '{}:{}/api/{}?model_id={}&image_url={}'.format(SERVER, PORT_MAPPING[model], MODEL_API[model], MODEL_ID[model], img_url)

    r = requests.get(url).json()
    if model == 'coco' or model == 'wikipedia':
        return r['caption']
    else:
        return pprint.pformat(r['results'])

@app.route('/manifest')
def docs():
    '''
    Serves the manifest to the 21 crawler.
    '''
    with open('manifest.yaml', 'r') as f:
        manifest_yaml = yaml.load(f)
    return json.dumps(manifest_yaml)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)