import json
import logging
import networkx

logging.basicConfig(level=logging.INFO)

#################
# JSON-style
#################

DATA_FILE = "banyan1.json"

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

with open(DATA_FILE, 'w') as fout:
    fout.write(json.dumps(x, indent=2))
logging.info('wrote to file ' + DATA_FILE)

#################
# networkx style
#################

# create directed graph
dev_graph = networkx.DiGraph()

# create daughters of root by adding edges from 'root' to 'root.<domain>'
for domain in ['phone', 'sms', 'media', 'encyclopedia', 'translation']:
    dev_graph.add_edge('root', 'root.'+domain, name=domain)
# make tree have depth 2 to force recursion and avoid flatness-errors
for verb in ['call', 'callback']:
    dev_graph.add_edge('root.phone', 'root.phone.'+verb, name=verb)

# assign 'count' attribute to terminals
ct_map = {
    'root.phone.call': 29,
    'root.phone.callback': 1,
    'root.sms': 25,
    'root.media': 150,
    'root.encyclopedia': 20,
    'root.translation': 10
}
for nodename, node_ct in ct_map.items():
    dev_graph.nodes[nodename]['count'] = node_ct

# aggregate 'count' attribute from terminals under 'root.phone'
dev_graph.nodes['root.phone']['count'] = sum([dev_graph.nodes[node]['count']
            for node in networkx.descendants(dev_graph, 'root.phone')])
# ^ only works properly because all children of 'root.phone' are terminals
# to do same for 'root', need to restrict to children of 'root'
dev_graph.nodes['root']['count'] = sum([dev_graph.nodes[node]['count']
            for node in dev_graph.succ['root']])




