from matplotlib import pyplot as plt
import networkx as nx


class NetworkGraph:

    
    def __init__(self, edge_list: list[tuple], node_list: list[str]) -> None:
        self.__num_of_edges = int(edge_list[0])
        self.__num_of_nodes = int(node_list[0])
        self.__type_graph = {'G': nx.Graph(), 'D': nx.DiGraph()}.get(edge_list[1], nx.Graph())    
        self.__edges = self.__set_edge_list(edge_list)
        self.__nodes = self.__set_node_list(node_list)
        self.__graph = self.__init_graph_nx()
        self.__degree_dict = self.__degree_order()      


    def __set_edge_list(self, edge_list: list[tuple]) -> list[tuple] | list[None]:
        if len(edge_list) > 2:
            return sorted(edge_list[2:])
        return []
    

    def __set_node_list(self, node_list: list[str]) -> list[str] | list[None]:
        new_list = [f'{node}' for node in range(self.__num_of_nodes) if f'{node}' not in node_list[1:]]
        intersect = set(new_list) - set(node_list[1:])
        new_list = node_list[1:].extend(list(intersect)[:(self.__num_of_nodes - len(node_list[1:]))])
        return new_list


    def __init_graph_nx(self) -> nx.DiGraph | nx.Graph:
        G = self.__define_graph_nx()
        
        if self.__edges or self.__nodes:
            G.add_edges_from(self.__edges)
            G.add_nodes_from(self.__nodes)

            for node in G.nodes:
                G.nodes[node]['color'] = 'red'

        return G
                

    def __degree_order(self) -> dict[str: int] | None:
        if self.__num_of_nodes:

            nodes_degree = dict()

            if self.__type_graph == 'D':
                nodes_degree = {node: self.__graph.out_degree[node] for node in self.__graph.nodes}
            else:
                nodes_degree = {node: self.__graph.degree[node] for node in self.__graph.nodes}

            nodes_degree = dict(sorted(nodes_degree.items(),
                                key=lambda value: value[1],
                                reverse=True))
            return nodes_degree
        return None
    