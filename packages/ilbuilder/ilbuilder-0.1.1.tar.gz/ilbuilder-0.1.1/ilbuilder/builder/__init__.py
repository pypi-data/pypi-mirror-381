from abc import ABC, abstractmethod
from pathlib import Path


class Builder(ABC):
    def __init__(self, name: str):
        self._name = name
        self._venv = '.venv'

    @property
    def name(self) -> str:
        return self._name

    @property
    def venv(self) -> str:
        return self._venv

    @property
    def base_output_dir(self) -> Path:
        return Path("ilbuilder-build")

    def set_name(self, name: str) -> "Builder":
        self._name = name
        return self

    def set_venv(self, venv: str) -> "Builder":
        self._venv = venv
        return self

    @staticmethod
    @abstractmethod
    def from_data(*args, **kwargs):
        pass

    @abstractmethod
    def _validate(self) -> bool:
        pass

    @abstractmethod
    def build(self):
        pass
