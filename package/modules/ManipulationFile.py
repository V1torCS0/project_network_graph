from pathlib import Path


class ManipulationFile:

    def __init__(self, string_path) -> None:
        self.__document_access = Path(string_path)
        self.__lines_document = self.__read_input_document()


    def get_input_document(self) -> Path:
        if self.__document_access.exists():
            return self.__document_access
        return None
    

    def set_input_document(self, new_string_path) -> None:
        self.__document_access = Path(new_string_path)
        self.__set_lines_input_document()


    def get_lines_input_document(self) -> list[str] | list[None]:
        return self.__lines_document
    

    def __set_lines_input_document(self) -> None:
        self.__lines_document = self.__read_input_document()


    def __read_input_document(self) -> list[str] | list[None]:
        if self.__document_access.exists():
            with open(self.__document_access, 'r') as input_manager_file:
                if input_manager_file:
                    return input_manager_file.readlines()
        return []
    
    
    def __write_output_document(self) -> None:
        # with open(f'../project_network_graph/package/testing/OutPut ({self.__document_access}).txt', 'w') as output_manager_file:
        ...


    def edges_in_Graph(self) -> list[str] | list[None]:

        if self.__lines_document:
            edge_list = []

            for line in self.__lines_document:

                if line is self.__lines_document[0]:
                    edge_list.append(line.split()[1])
                    edge_list.append(line.split()[2])
                else:
                    edge_list.append(tuple(line.split()))
            return edge_list
        return []


    def nodes_in_Graph(self) -> list[str] | list[None]:

        if self.__lines_document:
            node_list = []
            node_set = set()

            for line in self.__lines_document:
                
                if not line is self.__lines_document[0]:
                    node_set.add(line.split()[0])
                    node_set.add(line.split()[1])
                else:
                    node_list.append(line.split()[0])

            node_list.extend(list(node_set))
            return node_list
        return []

