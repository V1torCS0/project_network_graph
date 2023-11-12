import sys
sys.path.append('../project_network_graph/')

# import networkx as nx
# import matplotlib.pyplot as plt
from package.source import module_dfs as dfs

teste = dfs.NetworkGraphFile('../project_network_graph/package/testing/Arquivo G1.txt')
print(teste.nodes_in_Graph())
print(teste.edges_in_Graph())
