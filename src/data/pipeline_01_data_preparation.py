import os
import argparse
import yaml
import logging


def read_parameters(config_path):
    with open(config_path) as yaml_file:
        config =yaml.safe_load(yaml_file)
    return config

def main(config_path, datasource):
    config = read_parameters(config_path)
    




if __name__ == "__main__":
    default_config_path = os.path.join("config", "params.yaml")

    args = argparse.ArgumentParser()
    args.add_argument("--config", default=default_config_path)
    args.add_argument("--datasource", default=None)

    parsed_args = args.parse_args()
    main(config_path=parsed_args.config, datasource=parsed_args.datasource)