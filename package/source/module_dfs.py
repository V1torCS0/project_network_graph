import networkx as nx
from matplotlib import pyplot as plt
from pathlib import Path


class NetworkGraphFile:

    def __init__(self, string_path) -> None:
        self.__document_access = Path(string_path)
        self.__lines_document = self.__read_document()


    def get_document(self) -> Path:
        if self.__document_access.exists():
            return self.__document_access
        return None
    

    def set_document(self, new_string_path) -> None:
        self.__document_access = Path(new_string_path)
        self.__set_lines_document()


    def get_lines_document(self) -> list[str] | list[None]:
        return self.__lines_document
    

    def __set_lines_document(self) -> None:
        self.__lines_document = self.__read_document()


    def __read_document(self) -> list[str] | list[None]:
        if self.__document_access.exists():
            with open(self.__document_access, 'r') as file_network_graph:
                if file_network_graph:
                    return file_network_graph.readlines()
        return []


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
    

class ReadNetworkGraphFile (NetworkGraphFile):
    ...
# Uma instância desta classe fará a leitura do arquivo e retornará a lista de 
# vértices e arestas para repassá-lo a um objeto da classe NetworkGraph

class WriteNetworkGraphFile (NetworkGraphFile):
    ...
# Já esta classe é responsável pela criação de um arquivo, ao final das execuções, 
# que conterá a lista de nomenclatura para cada aresta e os vetores d, f resultantes

class NetworkGraph:
    ...
# Como dito anteriormente, essa classe irá fazer a criação do grafo a partir da lib Networkx,
# seja ele direcionado ou não, como também a visualização dele e do algoritmo DFS com a lib
# Matplotlib.pyplot

class DFS:
    ...
# A classe DFS é responsável pelo algoritmo do DFS, modularizando exclusivamente sua execução
#  e as informações que cada passo carrega (vetores d, f e os tipos de arestas)
