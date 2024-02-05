import networkx as nx
from package.algorithms import DFS, BFS, Dijkstra


class NetworkGraph:
    
    def __init__(self, edge_list: list[tuple], node_list: list[str]) -> None:
        self.__num_of_edges = int(edge_list[0])
        self.__num_of_nodes = int(node_list[0])
        self.__graph = self.__init_graph(edge_list[1])
        self.__algorithm = {'dfs': DFS.DFS(), 'bfs': BFS.BFS(), 'dijkstra': Dijkstra.Dijkstra()}.get(...)
        self.__edges = self.__set_edge_list(edge_list)
        self.__nodes = self.__set_node_list(node_list)   


    def __set_edge_list(self, edge_list: list[tuple]) -> list[tuple] | list[None]:
        if len(edge_list) > 2:
            return sorted(edge_list[2:])
        return []
    

    def __set_node_list(self, node_list: list[str]) -> list[str] | list[None]:
        new_list = [f'{node}' for node in range(self.__num_of_nodes) if f'{node}' not in node_list[1:]]
        intersect = set(new_list) - set(node_list[1:])
        new_list = node_list[1:].extend(list(intersect)[:(self.__num_of_nodes - len(node_list[1:]))])
        return new_list


    def __init_graph(self, type_graph: str) -> nx.DiGraph | nx.Graph | None:
        G = {'g': nx.Graph(), 'd': nx.DiGraph()}.get(type_graph)
        
        if self.__edges or self.__nodes:
            G.add_edges_from(self.__edges)
            G.add_nodes_from(self.__nodes)

            for node in G.nodes:
                G.nodes[node]['color'] = 'red'

        return G
    