import yaml
from dataclasses import dataclass

@dataclass
class App:
    Token: str
    Url: str
    
    def __init__(self) -> None:
        with open("./config/config.yaml") as stream:
            try:
                config = yaml.safe_load(stream)
                self.Token = config["token"]
                self.Url = config["url"]
            except yaml.YAMLError as exc:
                print(exc)
        