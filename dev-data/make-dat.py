import json
import logging

logging.basicConfig(level=logging.INFO)

def node(label, count=None, child=None):
    node = {'label': label}
    node['child'] = child or []
    node['count'] = count or sum([child['count'] for child in node['child']])
    return node

x11 = node(label='call', count=29)
x12 = node(label='callback', count=1)
x1 = node(label='phone', child=[x11, x12])

x2 = node(label='sms', count=25)
x3 = node(label='media', count=150)
x4 = node(label='encyclopedia', count=20)
x5 = node(label='translation', count=10)

x = node(label='', count=None, child=[x1, x2, x3, x4, x5])
logging.info('created node')

with open('mangrove1.json', 'w') as fout:
    fout.write(json.dumps(x, indent=2))
logging.info('wrote to file mangrove1.json')


