import json
import logging

logging.basicConfig(level=logging.INFO)

def node(prefix, count, child):
    return {'prefix': prefix, 'count': count, 'child': child}

x1 = node(prefix='phone', count=30, child=[])
x2 = node(prefix='sms', count=25, child=[])
x3 = node(prefix='media', count=150, child=[])
x4 = node(prefix='encyclopedia', count=20, child=[])
x5 = node(prefix='translation', count=10, child=[])
x = node(prefix='', count=100, child=[x1, x2, x3, x4, x5])
logging.info('created node')

with open('mangrove1.json', 'w') as fout:
    fout.write(json.dumps(x, indent=2))
logging.info('wrote to file mangrove1.json')


