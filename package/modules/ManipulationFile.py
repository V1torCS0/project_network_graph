from pathlib import Path


class ManipulationFile:

    def __init__(self, string_path: str) -> None:
        self.__name_file = string_path
        self.__document_access = Path('../project_network_graph/package/testing/' + self.__name_file)
        self.exists = self.__document_access.exists()
        self.__lines_document = self.__read_input_document()


    def get_input_document(self) -> Path:
        if self.exists:
            return self.__document_access
        return None
    

    def set_name_file(self, new_string_path: str) -> None:
        self.__name_file = new_string_path
        self.__set_input_document()

    
    def __set_input_document(self):
        self.__document_access = Path('../project_network_graph/package/testing/' + self.__name_file)
        self.__set_lines_input_document()


    def get_lines_input_document(self) -> list[str] | list[None]:
        return self.__lines_document
    

    def __set_lines_input_document(self) -> None:
        self.__lines_document = self.__read_input_document()


    def __read_input_document(self) -> list[str] | list[None]:
        if self.exists:
            with open(self.__document_access, 'r') as input_manager_file:
                if input_manager_file:
                    return input_manager_file.readlines()
        return []
    
    
    def generate_output(self, edge_types_dict: dict, d_array_step: dict, f_array_step: dict) -> None:
        if d_array_step is None and f_array_step is None:
            print("Invalid Input")
            return None
        self.__write_output_document(edge_types_dict, d_array_step, f_array_step)


    def __write_output_document(self, edge_dict: dict, d_array: dict, f_array: dict) -> None:
        path_write = Path(f'../project_network_graph/package/testing/OutPut_{self.__name_file.replace(".txt", "").replace(" ", "-")}.txt')
        
        if path_write.exists():
            print(f'OutPut already exists... access: {path_write}')
            return None
        
        with open(path_write, 'w') as output_manager_file:
            
            if not edge_dict is None:
                preview_edge_type = {'blue': 'Arvore', 'deeppink': 'Retorno',
                                   'orange': 'Avanco', 'red': 'Cruzamento'}
                for edge, edge_type in edge_dict.items():
                    output_manager_file.write(f'{edge}: {preview_edge_type[edge_type]}\n')

            else:
                output_manager_file.write('No edges in network graph...\n')
            output_manager_file.write('\n')
            output_manager_file.write(f'Vetor d: {list(map(lambda d_value: d_value[1], d_array.items()))}\n')
            output_manager_file.write(f'Vetor f: {list(map(lambda f_value: f_value[1], f_array.items()))}\n')
            print(f'Output Successfully, access: {path_write}')


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
