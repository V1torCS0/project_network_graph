import sys
sys.path.append('../project_network_graph/')

from package.modules import ManipulationFile as mf
from package.modules import NetworkGraph as ng

# Rodaremos uma bateria de testes com alguns tipos de grafos
# que se encontram nas dependências do projeto (../package/testing/)

test_array = ['Arquivo G1.txt', 'Arquivo G2.txt',
              'Arquivo G3.txt', 'Arquivo G4.txt',
              'Arquivo G5.txt', 'Arquivo G6.txt']

for sample in test_array:

    file = mf.ManipulationFile(sample)

    G = ng.NetworkGraph(file.edges_in_Graph(), file.nodes_in_Graph())
    G.dfs()
    file.generate_output(G.get_edge_types_dict(), G.get_d_dict(), G.get_f_dict())