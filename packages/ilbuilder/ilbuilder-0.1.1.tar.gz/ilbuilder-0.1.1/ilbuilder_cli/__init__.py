from rushclis import RushCli

from ilbuilder_cli.command import build
from ilbuilder.version import __version__


class Cli(RushCli):
    def __init__(self):
        super().__init__("ilbuilder", __version__)

        self.add_command("build")
        self.set_sub_main_func('build', build)

        self.add_sub_argument('build', 'name')
        self.add_sub_argument('build', 'script')
