from pathlib import Path


class InputFile:
    
    def __init__(self, input_name_file: str) -> None:
        self.set_name_file(input_name_file)
        self.set_path(self.__name_file)


    def set_name_file(self, validate_name: str) -> None:
        if validate_name or ('.txt' in validate_name):
            self.__name_file = validate_name
            return None
        raise ValueError('File Name or Extension Invalid')

    def set_path(self, validate_path: str) -> None:
        path = Path(f'/project_network_graph/package/testing/{validate_path}')

        if path.exists:
            self.__path = path
            return None
        raise ValueError('Invalid Path')
    
