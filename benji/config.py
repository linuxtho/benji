import yaml

from os import path


def load_config(filepath):
    """Loads a benji configuration file."""
    if filepath is None:
        # This is probably a bad idea
        filepath = '/etc/benji.yml'

    with open(filepath) as config_file:
        return yaml.load(config_file)
