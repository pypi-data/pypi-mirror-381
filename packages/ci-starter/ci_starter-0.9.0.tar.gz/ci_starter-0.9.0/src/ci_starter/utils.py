from collections.abc import Mapping
from typing import TextIO

from ruamel.yaml import YAML as Yaml

from ci_starter.step import Step


def step_yaml() -> Yaml:
    yaml = Yaml()
    yaml.register_class(Step)
    return yaml


def from_yaml(s: str) -> dict:
    yaml = step_yaml()
    obj = yaml.load(s)
    return obj


def dump(obj: Mapping, filelike: TextIO) -> None:
    yaml = step_yaml()
    yaml.dump(obj, filelike)
