from ilbuilder.builder.builder import IlBuilder


class TestBuilder(IlBuilder):
    def __init__(self, name, script, icon=None):
        super().__init__(name, script, icon)

        self._console = True

    @staticmethod
    def from_data(root: str) -> 'IlBuilder':
        pass