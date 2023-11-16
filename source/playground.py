import networkx as nx
from matplotlib import pyplot as plt


node_list = [] #a posição em 0 armazena o total de vértices e a posição em 1 armazena o tipo de grafo
edge_list = [] # o primeiro elemento será a quantidade de arestas e depois as arestas

with open('../project_network_graph/package/testing/Arquivo G3.txt', 'r') as file_network_graph:

  text_file = file_network_graph.readlines()

  for line in text_file:

    if line is text_file[0]:
      node_list.append(line.split()[0])
      edge_list.append(line.split()[1])
      node_list.append(line.split()[2])

    else:
      edge_list.append(tuple(line.split()))

      for index in range(len(line.split())):
        if not(line.split()[index] in node_list):
          node_list.append(line.split()[index])


print(node_list, edge_list)

# graph_mapping = {'D': nx.DiGraph(), 'G': nx.Graph()}
G = nx.DiGraph()
# graph_mapping.get(node_list[1], nx.DiGraph())

G.add_nodes_from(node_list[2:])
for node in list(G.nodes):
  G.nodes[node]['color'] = 'red'

G.add_edges_from(edge_list[1:])

"""<h3>Como teste, iremos plotar o grafo com a biblioteca <b>Pyplot</b>"""
'>'
position = nx.spectral_layout(G)
fig, ax = plt.subplots()
nx.draw(G, position, with_labels= True, node_size= 650,
        node_color=[G.nodes[node]['color'] for node in list(G.nodes)],
        edgecolors= 'black', ax= ax)
plt.title("Network Graph Original")
plt.pause(2.0)
"""<h3>Para visualizarmos o funcionamento do <b>DFS</b>, criaremos um procedimento que demonstrará o algoritmo em ação"""

def visualization_dfs(ax):

    ax.clear()
    plt.title('DFS Visualization')
    nx.draw(G, position, node_size= 650,
            node_color= [G.nodes[node]['color'] for node in G.nodes],
            edgecolors= 'black', edge_color=[edge[1] for edge in edge_type_dict.items()],
            ax= ax)

    for node, (x, y) in position.items():
      ax.text(x, y, f'{d_dict[node]}/{f_dict[node]}',
              color= 'white' if G.nodes[node]['color'] != 'white' else 'black',
              fontsize= 10, ha= 'center', va= 'center')
    plt.pause(1.0)


"""Além disso, precisaremos de outro procedimento que será responsável em categorizar o tipo de aresta: <b>Árvore</b>, <b>Avanço</b>, <b>Cruzamento</b> e <b>Retorno</b>"""

edge_type_dict = {edge: 'black' for edge in G.edges}

def set_edge_type(node_out, node_in, graph):
    if graph.nodes[node_in]['color'] == color_list[0]:
        edge_type_dict[(node_out, node_in)] = 'blue' # Árvore
    elif graph.nodes[node_in]['color'] == color_list[1]:
        edge_type_dict[(node_out, node_in)] = 'deeppink' # Retorno
    else:
      if d_dict[node_out] < d_dict[node_in]:
          edge_type_dict[(node_out, node_in)] = 'orange' # Avanço
      else:
          edge_type_dict[(node_out, node_in)] = 'red' # Cruzamento


"""<h3>Implementando o algoritmo <b>DFS</b>"""

color_list = ['white', 'gray', 'black']
nodes_out_degree = {node: G.out_degree[node] for node in G.nodes}
nodes_out_degree = dict(sorted(nodes_out_degree.items(),
                               key=lambda value: value[1],
                               reverse=True))
d_dict = {}
f_dict = {}
mark = 0


def dfs(graph: nx.DiGraph | nx.Graph):

    for node in graph.nodes:
        graph.nodes[node]['color'] = color_list[0]
        d_dict[node], f_dict[node] = mark, mark

    for accessed_node in nodes_out_degree.items():
        if graph.nodes[accessed_node[0]]['color'] == color_list[0]:
            dfs_visit(accessed_node[0], graph)

    visualization_dfs(ax)


def dfs_visit(node, graph: nx.DiGraph | nx.Graph):

    global mark

    visualization_dfs(ax)

    graph.nodes[node]['color'] = color_list[1]
    mark += 1
    d_dict[node] = mark

    for adjacency_node in graph.neighbors(node):
        if graph.nodes[adjacency_node]['color'] == color_list[0]:
            set_edge_type(node, adjacency_node, graph)
            dfs_visit(adjacency_node, graph)
        else:
            set_edge_type(node, adjacency_node, graph)

    visualization_dfs(ax)

    graph.nodes[node]['color'] = color_list[2]
    mark += 1
    f_dict[node] = mark


dfs(G)
plt.show()

d_dict = dict(sorted(d_dict.items()))
f_dict = dict(sorted(f_dict.items()))

print(d_dict)
print(f_dict)
print(edge_type_dict)