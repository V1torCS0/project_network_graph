from matplotlib import pyplot as plt
import networkx as nx


class NetworkGraph:
    
    def __init__(self, edge_list: list, node_list: list) -> None:
        self.__num_of_edges = int(edge_list[0])
        self.__type_graph = edge_list[1]        
        self.__num_of_nodes = int(node_list[0])
        self.__edges = self.__set_edge_list(edge_list)
        self.__nodes = self.__set_node_list(node_list)
        self.__graph = self.__init_Graph_nx()
        self.__edges_type_dict = self.__define_type_edge()
        self.__degree_dict = self.__degree_order()        
        self.__d_dict = self.__define_vector_step()
        self.__f_dict = self.__define_vector_step()
        self.__mark = 0
        self.__plot_axes = plt.gca()


    def __set_edge_list(self, edge_list):
        if len(edge_list) > 2:
            return edge_list[2:]
        return []
    

    def __set_node_list(self, node_list):
        if len(node_list) > 1:
            return node_list[1:]
        return [nodes for nodes in range(self.__num_of_nodes)] 


    def __init_Graph_nx(self) -> nx.DiGraph | nx.Graph:
        G = self.__define_Graph_nx()
        
        if self.__edges or self.__nodes:
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
                

    def __degree_order(self) -> dict[str: int]:
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


    def __define_type_edge(self) -> dict[str: str]:
        if self.__graph and self.__num_of_edges:
            return {edge: 'black' for edge in self.__graph.edges}
        return None
    
    def get_type_edge_dict(self):
        return self.__degree_dict

    def __define_vector_step(self) -> dict[str: int]:
        if self.__graph and self.__num_of_nodes:
            return {node: 0 for node in self.__graph.nodes}
        return None


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
                    edgecolors= 'black',
                    edge_color= None if self.__edges_type_dict is None else [edge[1] for edge in self.__edges_type_dict.items()],
                    ax= self.__plot_axes)
        plt.pause(0.5)

    
    def __edge_type_exists(self, node_out, node_in) -> None:
        if (node_out, node_in) in self.__edges_type_dict:
            return (node_out, node_in)
        return (node_in, node_out)


    def __set_edge_type(self, node_out, node_in) -> None:
        if not self.__edges_type_dict is None:

            if self.__graph.nodes[node_in]['color'] == 'white':
                self.__edges_type_dict[(node_out, node_in)] = 'blue'

            elif self.__graph.nodes[node_in]['color'] == 'gray' and self.__edges_type_dict[self.__edge_type_exists(node_out, node_in)] == 'black':
                self.__edges_type_dict[self.__edge_type_exists(node_out, node_in)] = 'deeppink'

            elif self.__edges_type_dict[self.__edge_type_exists(node_out, node_in)] == 'black':
                
                if self.__d_dict[node_out] < self.__d_dict[node_in]:
                    self.__edges_type_dict[self.__edge_type_exists(node_out, node_in)] = 'orange'
                    return None

                self.__edges_type_dict[self.__edge_type_exists(node_out, node_in)] = 'red'
        return None


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

        self.__plot_Graph()

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

