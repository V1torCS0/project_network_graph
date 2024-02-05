from pathlib import Path


class OutputFile:
    
    def __init__(self, output_name_file: str) -> None:
        self.__name_file = output_name_file
        self.__path = Path(f'/project_network_graph/package/output/{self.get_name_file}')