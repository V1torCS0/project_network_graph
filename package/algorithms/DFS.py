from package.algorithms.Base import Base

class DFS(Base):

    def __init__(self) -> None:
        ...

    def exec(self) -> None:
        return "DFS executing..."

        """ if not self.__nodes:
            print("This is a Null Network Graph, DFS doesn't work")
            return None
        
        for node in self.__graph.nodes:
            self.__graph.nodes[node]['color'] = 'white'
        
        for accessed_node in self.__degree_dict.items():
            if self.__graph.nodes[accessed_node[0]]['color'] == 'white':
                self.__step(accessed_node[0]) """
    

    def __step(self, node: str) -> None:

        self.__graph.nodes[node]['color'] = 'gray'
        self.__mark += 1
        self.__d_dict[node] = self.__mark

        for adjancency_node in self.__graph.neighbors(node):
            if self.__graph.nodes[adjancency_node]['color'] == 'white':
                self.__set_edge_type(node, adjancency_node)
                self.__step(adjancency_node)
            self.__set_edge_type(node, adjancency_node)

        self.__graph.nodes[node]['color'] = 'black'
        self.__mark += 1
        self.__f_dict[node] = self.__mark
    
    
    def __edge_type_exists(self, node_out: str, node_in: str) -> tuple[str]:
        if (node_out, node_in) in self.__edge_types_dict:
            return (node_out, node_in)
        return (node_in, node_out)


    def __set_edge_type(self, node_out: str, node_in: str) -> None:
        if not self.__edge_types_dict is None:

            if self.__graph.nodes[node_in]['color'] == 'white':
                self.__edge_types_dict[(node_out, node_in)] = 'blue'

            elif self.__graph.nodes[node_in]['color'] == 'gray' and self.__edge_types_dict[self.__edge_type_exists(node_out, node_in)] == 'black':
                self.__edge_types_dict[self.__Edge_Type_Exists(node_out, node_in)] = 'deeppink'

            elif self.__edge_types_dict[self.__Edge_Type_Exists(node_out, node_in)] == 'black':
                
                if self.__d_dict[node_out] < self.__d_dict[node_in]:
                    self.__edge_types_dict[self.__Edge_Type_Exists(node_out, node_in)] = 'orange'
                    return None

                self.__edge_types_dict[self.__Edge_Type_Exists(node_out, node_in)] = 'red'
        return None
