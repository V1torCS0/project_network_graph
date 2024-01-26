from matplotlib import pyplot as plt
import networkx as nx

class GraphVisualization:
    
    def __init__(self, graph: nx.DiGraph() | nx.Graph()) -> None:
        self.__graph = graph
        self.__plot_axes = plt.gca()

    def DFS_Visualize(self, graph, only_view= False) -> None:
        position = nx.shell_layout(self.__graph)
        
        if only_view:
            self.__plot_axes.clear()
            plt.title('Network Graph Original')
            nx.draw(self.__graph, position, with_labels= True, node_size= 650,
                    node_color= [self.__graph.nodes[node]['color'] for node in self.__graph],
                    edgecolors= 'black', ax= self.__plot_axes)
            plt.pause(2.0)
            return None

        self.__plot_axes.clear()
        plt.title('DFS Visualization')

        edges_subtitle = [
            plt.Line2D([0], [0], color= 'blue', linewidth= 2, label= 'Árvore'),
            plt.Line2D([0], [0], color= 'deeppink', linewidth= 2, label= 'Retorno'),
            plt.Line2D([0], [0], color= 'orange', linewidth= 2, label= 'Avanço'),
            plt.Line2D([0], [0], color= 'red', linewidth= 2, label= 'Cruzamento')
        ]
        plt.legend(handles= edges_subtitle, loc='best')

        for node, (x, y) in position.items():
            self.__plot_axes.text(x, y, f'{self.__d_dict[node]}/{self.__f_dict[node]}',
                color= 'white' if self.__graph.nodes[node]['color'] != 'white' else 'black',
                fontsize= 10, ha= 'center', va= 'center')
                
        nx.draw(self.__graph, position, node_size= 650,
                node_color= [self.__graph.nodes[node]['color'] for node in self.__graph.nodes],
                edgecolors= 'black',
                edge_color= None if self.__edge_types_dict is None else [edge[1] for edge in self.__edge_types_dict.items()],
                ax= self.__plot_axes)
        plt.pause(0.5)

    def BFS_Visualize(self):
        ...
    