from matplotlib import pyplot as plt
import networkx as nx


class NetworkGraph:
    
    def __init__(self, edge_list: list, node_list: list) -> None:
        self.__type_graph = edge_list[1]
        self.__edges = edge_list[2:]
        self.__nodes = node_list[1:]
        self.__graph = self.__init_Graph_nx()
        self.__edges_type_dict = self.__define_type_edge()
        self.__degree_dict = self.__degree_order()        
        self.__d_dict = self.__define_vector_step()
        self.__f_dict = self.__define_vector_step()
        self.__mark = 0
        self.__plot_axes = plt.gca()

    def __init_Graph_nx(self) -> nx.DiGraph | nx.Graph:
        G = self.__define_Graph_nx()
        G.add_edges_from(self.__edges)
        G.add_nodes_from(self.__nodes)

        for node in G.nodes:
            G.nodes[node]['color'] = 'red'

        return G


    def __define_Graph_nx(self) -> nx.DiGraph | nx.Graph:
        if self.__type_graph == 'D':
            return nx.DiGraph()
        else:
            return nx.Graph()
                

    def get_all(self):
        return (self.__d_dict, self.__f_dict)

    
    def __degree_order(self) -> dict[str: int]:
        nodes_degree = dict()

        if self.__type_graph == 'D':
            nodes_degree = {node: self.__graph.out_degree[node] for node in self.__graph.nodes}
        else:
            nodes_degree = {node: self.__graph.degree[node] for node in self.__graph.nodes}

        nodes_degree = dict(sorted(nodes_degree.items(),
                               key=lambda value: value[1],
                               reverse=True))
        return nodes_degree


    def __define_type_edge(self) -> dict[str: str]:
        if (self.__graph):
            return {edge: 'black' for edge in self.__graph.edges}
    

    def __define_vector_step(self) -> dict[str: int]:
        if (self.__graph):
            return {node: 0 for node in self.__graph.nodes}


    def __plot_Graph(self, only_view= False) -> None:
        position = nx.shell_layout(self.__graph)
        
        if only_view:
            plt.title('Network Graph Original')
            nx.draw(self.__graph, position, with_labels= True, node_size= 650,
                    node_color= [self.__graph.nodes[node]['color'] for node in self.__graph],
                    edgecolors= 'black', ax= self.__plot_axes)
            plt.pause(2.0)

        if not only_view:
            self.__plot_axes.clear()
            plt.title('DFS Visualization')

            for node, (x, y) in position.items():
                self.__plot_axes.text(x, y, f'{self.__d_dict[node]}/{self.__f_dict[node]}',
                    color= 'white' if self.__graph.nodes[node]['color'] != 'white' else 'black',
                    fontsize= 10, ha= 'center', va= 'center')
                
            nx.draw(self.__graph, position, node_size= 650,
                    node_color= [self.__graph.nodes[node]['color'] for node in self.__graph.nodes],
                    edgecolors= 'black', edge_color= [edge[1] for edge in self.__edges_type_dict.items()],
                    ax= self.__plot_axes)
        plt.pause(0.75)


    def __set_edge_type(self, node_out, node_in):
        if self.__graph.nodes[node_in]['color'] == 'white':
            self.__edges_type_dict[(node_out, node_in)] = 'blue'
        elif self.__graph.nodes[node_in]['color'] == 'gray':
            self.__edges_type_dict[(node_out, node_in)] = 'deeppink'
        else:
            if self.__d_dict[node_out] < self.__d_dict[node_in]:
                self.__edges_type_dict[(node_out, node_in)] = 'orange'
            else:
                self.__edges_type_dict[(node_out, node_in)] = 'red'


    def dfs(self) -> None:

        self.__plot_Graph(only_view= True)
        
        for node in self.__graph.nodes:
            self.__graph.nodes[node]['color'] = 'white'
        
        for accessed_node in self.__degree_dict.items():
            if self.__graph.nodes[accessed_node[0]]['color'] == 'white':
                self.__dfs_step(accessed_node[0])
        self.__plot_Graph()
        plt.pause(2.5)
    

    def __dfs_step(self, node) -> None:
        self.__plot_Graph()

        self.__graph.nodes[node]['color'] = 'gray'
        self.__mark += 1
        self.__d_dict[node] = self.__mark

        for adjancency_node in self.__graph.neighbors(node):
            if self.__graph.nodes[adjancency_node]['color'] == 'white':
                self.__set_edge_type(node, adjancency_node)
                self.__dfs_step(adjancency_node)
            else:
                self.__set_edge_type(node, adjancency_node)

        self.__plot_Graph()

        self.__graph.nodes[node]['color'] = 'black'
        self.__mark += 1
        self.__f_dict[node] = self.__mark
