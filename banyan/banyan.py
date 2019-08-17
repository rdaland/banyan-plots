import networkx


def make_dev_graph():
    # create directed graph
    dev_graph = networkx.DiGraph()

    # create daughters of root by adding edges from 'root' to 'root.<domain>'
    for domain in ['phone', 'sms', 'media', 'encyclopedia', 'translation']:
        dev_graph.add_edge('root', 'root.' + domain, name=domain)
    # make tree have depth 2 to force recursion and avoid flatness-errors
    for verb in ['call', 'callback']:
        dev_graph.add_edge('root.phone', 'root.phone.' + verb, name=verb)

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
    dev_graph.nodes['root.phone']['count'] = \
        sum([dev_graph.nodes[node]['count']
             for node in networkx.descendants(dev_graph, 'root.phone')])
    # ^ only works properly because all children of 'root.phone' are terminals
    # to do same for 'root', need to restrict to children of 'root'
    dev_graph.nodes['root']['count'] = \
        sum([dev_graph.nodes[node]['count']
             for node in dev_graph.succ['root']])

    return dev_graph

def get_scatterplot_nodes_and_edges(G):
    # obtain a dictionary of form {'nodename': array([x, y, z])}
    start_pos = networkx.layout.kamada_kawai_layout(G, dim=3)
    layout = networkx.layout.fruchterman_reingold_layout(G, pos=start_pos, dim=3)

    x_pos = lambda node: layout[node][0]
    y_pos = lambda node: layout[node][1]
    z_pos = lambda node: layout[node][2]

    # project/extract layout into separate x, y, z vectors
    node_order = sorted(layout)
    x_node = [x_pos(node) for node in node_order]
    y_node = [y_pos(node) for node in node_order]
    z_node = [z_pos(node) for node in node_order]

    # in scatterplots, the 'line' mode draws lines from each point to the next
    # None values are a mechanism to introduce 'gaps' (needed since edges aren't connected)
    x_edge, y_edge, z_edge = [], [], []
    for edge in dev_graph.edges():
        start, end = edge[0], edge[1]
        x_edge.extend([x_pos(start), x_pos(end), None])
        y_edge.extend([y_pos(start), y_pos(end), None])
        z_edge.extend([z_pos(start), z_pos(end), None])

    return {'x_node': x_node, 'y_node': y_node, 'z_node': z_node,
            'x_edge': x_edge, 'y_edge': y_edge, 'z_edge': z_edge}

def make_3d_scatterplot(G):
    nodes_and_edges = get_scatterplot_nodes_and_edges(G)

    dev_plot = graph_objects.Figure()
    dev_plot.add_trace(graph_objects.Scatter3d(x=nodes_and_edges['x_edge'],
                                               y=nodes_and_edges['y_edge'],
                                               z=nodes_and_edges['z_edge'],
                                               mode='lines'))
    dev_plot.add_trace(graph_objects.Scatter3d(x=nodes_and_edges['x_node'],
                                               y=nodes_and_edges['y_node'],
                                               z=nodes_and_edges['z_node'],
                                               mode='markers'))
    # TODO: find some way to save this to a figure


