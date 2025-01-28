import subprocess
from contextlib import suppress
from pathlib import Path
from setuptools import Command, setup
from setuptools.command.build import build

class CustomCommand(Command):
    def initialize_options(self) -> None:
        self.bdist_dir = None
        self.proto_msgs_path = None
        self.pkg_name = None

    def finalize_options(self) -> None:
        self.pkg_name = self.distribution.get_name().replace('-', '_')
        self.proto_msgs_path = Path("proto")
        with suppress(Exception):
            self.bdist_dir = Path(self.get_finalized_command("bdist_wheel").bdist_dir)

    def get_source_files(self) ->'list[str]':
        if self.proto_msgs_path.is_dir():
            return [str(path) for path in self.proto_msgs_path.glob('*.proto')]
        else:
            return []

    def run(self) -> None:
        if self.bdist_dir:
            # Create package structure
            output_dir = self.bdist_dir / self.pkg_name
            output_dir.mkdir(parents=True, exist_ok=True)
            # generate python classes
            protoc_call = [
                "python3",
                "-m",
                "grpc_tools.protoc",
                f"--proto_path={self.proto_msgs_path}",
                f"--python_out={output_dir}",
                f"--pyi_out={output_dir}",
                *self.get_source_files(),
            ]
            subprocess.call(protoc_call)
            with open(f"{output_dir}/__init__.py", "w"):
                pass

class CustomBuild(build):
    sub_commands = [('build_custom', None)] + build.sub_commands

setup(
   packages=[],
   cmdclass={'build': CustomBuild, 'build_custom': CustomCommand}
)