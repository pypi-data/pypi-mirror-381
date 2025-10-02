import json


class CozoDbConfigurations:
    uri: str

    def __init__(
        self,
        configuration_file: str,
    ):
        with open(
            configuration_file,
        ) as file:
            json_model = json.load(file)
            self.uri = json_model["uri"]


example_configuration = {
    "uri": "mem://",
}
