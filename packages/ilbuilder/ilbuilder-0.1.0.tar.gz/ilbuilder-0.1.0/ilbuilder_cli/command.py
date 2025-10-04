from ilbuilder_cli.build import TestBuilder


def build(args):
    name = getattr(args, "name")
    script = getattr(args, "script")

    b = TestBuilder(name, script)
    b.build()