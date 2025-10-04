import asyncio
from pathlib import Path
from functools import cached_property
from asyncinit import asyncinit
from loguru import logger as log
from pywershell import CMDResult

from dockwershell import Docker, path_to_wsl


# from .path_to_mnt import path_to_wsl

class DockerImage:
    instances = {}

    def __init__(self, dockerfile: Path, rebuild: bool = False, run_args: str = None, **kwargs):
        self.docker: Docker = Docker()
        self.file = dockerfile
        self.rebuild = rebuild
        self.run_args = run_args
        self.name = dockerfile.name.replace("Dockerfile.", "")
        self.image = self.name

        if kwargs:
            pad = max(len(k) for k in kwargs)
            log.debug(f"{self}: Initializing with kwargs:\n" + "\n".join(
                f"  - {k.ljust(pad)} = {v}" for k, v in kwargs.items()))

        _ = self.build

    def __repr__(self):
        return f"[{self.image}.AsyncDockerImage]"

    # # parse build args once, cached
    # @cached_property
    # def build_args(self):
    #     if not self.args_raw:
    #         return []
    #     raw = self.args_raw if isinstance(self.args_raw, list) else [self.args_raw]
    #     out = []
    #     for s in raw:
    #         s = s.strip().lstrip("--build-arg").lstrip("--build_arg")
    #         if "=" not in s:
    #             raise ValueError("build arg must look like KEY=VAL")
    #         out.append(f"--build-arg {s}")
    #     return out

    @cached_property
    def build(self):
        images = self.docker.images
        if self.image in images and not self.rebuild:
            log.debug(f"{self}: Skipping build: '{self.image}' already exists")
            return f"run {self.run_args} {self.image}"

        cmd = f"build -f {path_to_wsl(self.file)} -t {self.image} {path_to_wsl(self.file.parent)}"
        # if self.build_args:
        #     cmd += " " + " ".join(self.build_args)
        self.docker.run(cmd)
        log.success(f"{self}: Successfully built {self.image}")
        return f"run {self.run_args} {self.image}"

    def run(self, cmd: str = "", headless: bool = True, **kwargs) -> CMDResult | None:
        args = " ".join(f"-{k} {v}" for k, v in kwargs.items())
        full = f"{self.build} {args} {cmd}".strip()
        log.debug(f"{self}: Sending request:\n   - receiver={self.docker}\n   - kwargs={kwargs}\n   - cmd={full}")
        return self.docker.run(cmd=full, headless=headless, **kwargs)


def debug():
    DockerImage(Path(r'/dockwershell/Dockerfile.foobar'))


if __name__ == "__main__":
    debug()
