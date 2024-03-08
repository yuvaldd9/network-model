import click

from .loader import Loader
from .handlers import ModelHandler


class NetworkModel:
    def __init__(self, default_model_descriptor: str) -> None:
        self.model_descriptor: str = default_model_descriptor
        self.loader: Loader = Loader(self.model_descriptor)
        self.network_model: ModelHandler = self.loader.load()

    def model(self):
        self.network_model.play()


@click.command()
@click.option(
    "-f",
    "--network-descriptor",
    "network_descriptor_file",
    required=True,
    type=click.Path(exists=True),
    help="Path to the network descriptor file.",
)
def main(network_descriptor_file):
    network_model = NetworkModel(network_descriptor_file)
    network_model.model()


if __name__ == "__main__":
    main()
