import sys
sys.path.append('../project_network_graph/')

# import networkx as nx
# import matplotlib.pyplot as plt
from package.modules import ManipulationFile as mf
from package.modules import NetworkGraph as ng

teste = mf.ManipulationFile('../project_network_graph/package/testing/Arquivo G5.txt')

G = ng.NetworkGraph(teste.edges_in_Graph(), teste.nodes_in_Graph())
print(G.get_type_edge_dict())
G.dfs()