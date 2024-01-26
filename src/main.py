import sys
sys.path.append('../project_network_graph/')

# from package.modules.ManipulationFile import ManipulationFile
# from package.modules.NetworkGraph import NetworkGraph
from package.algorithms import Base, DFS, BFS, Dijkstra

lista = [Base.Base(), DFS.DFS(), BFS.BFS(), Dijkstra.Dijkstra()]

for instance in lista:
    print(instance.exec())