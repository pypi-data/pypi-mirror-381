import subprocess

from hatchling.builders.hooks.plugin.interface import BuildHookInterface


class BuildSharedObjectd(BuildHookInterface):
    def initialize(self, version, build_data):
        build_data["pure_python"] = False

        subprocess.check_output(
            [
                "go",
                "build",
                "-C",
                "formatter",
                "-buildmode=c-shared",
                "-o",
                "../pkg/formatter.so",
                "formatter.go",
            ]
        )
