'''
deep21 API tester
'''

import requests
import pprint

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

def deep(model, img_url):
    if model not in PORT_MAPPING:
        print('Error: Invalid model chosen')
        return

    url = '{}:{}/api/{}?model_id={}&image_url={}'.format(SERVER, PORT_MAPPING[model], MODEL_API[model], MODEL_ID[model], img_url)

    r = requests.get(url).json()
    print(r)
    if model == 'coco' or model == 'wikipedia':
        print(r['caption'])
    else:
        print(pprint.pformat(r['results']))