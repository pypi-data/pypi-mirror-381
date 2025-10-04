from pathlib import Path, PureWindowsPath
from functools import cached_property
from typing import Union

from .mod_docker import Docker

def path_to_mnt(p: Union[str, Path], verbose: bool = False) -> str:
    """
    Convert a Windows path into a WSL-compatible path.

    - "C:\\Foo\\Bar"   → "/mnt/c/Foo/Bar"
    - "C:/Foo/Bar"     → "/mnt/c/Foo/Bar"
    - "\\\\host\\share"→ "//host/share"
    - "relative\\path" → "relative/path"

    Args:
        p:       Windows path (str or PureWindowsPath).
        verbose: If true, emit a debug log of the conversion.

    Returns:
        A POSIX-style path suitable for WSL or _Docker-on-WSL.
    """
    win = PureWindowsPath(p)
    # If there's a drive letter (e.g. "C:")
    if win.drive:
        drive = win.drive.rstrip(":").lower()
        # win.parts is like ("C:\\", "Users", "…"), so skip the first element
        tail = win.parts[1:]
        wsl_path = "/" + "/".join(["mnt", drive, *tail])
    else:
        # No drive letter → just normalize separators
        wsl_path = "/".join(win.parts)

    return wsl_path

path_to_wsl = path_to_mnt

class DockerImage:
    instances = {}

    def __init__(self, dockerfile: Path, rebuild: bool = False, run_args: str = None, **kwargs):
        try:
            self.docker: Docker = Docker()
            self.file = dockerfile
            self.rebuild = rebuild
            self.run_args = run_args or ""
            self.name = dockerfile.name.replace("Dockerfile.", "")
            self.image = self.name
            _ = self.build
        except Exception as e:
            raise Exception(f"__init__ failed: {e}")

    def __repr__(self):
        return f"[{self.image}.DockerImage]"

    @cached_property
    def build(self):
        try:
            try:
                result = self.docker.run("images --format {{.Repository}}")

                if not result or not result["success"]:
                    raise Exception("Failed to check existing images")

                out_str = result["output"]
                images = [line.strip() for line in out_str.splitlines() if line.strip()]
            except Exception as e:
                raise Exception(f"Image check failed: {e}")

            if self.image in images and not self.rebuild:
                return f"run {self.run_args} {self.image}"

            try:
                cmd = f"build -f {path_to_wsl(self.file)} -t {self.image} {path_to_wsl(self.file.parent)}"
                result = self.docker.run(cmd)

                if not result or not result["success"]:
                    raise Exception(f"Build failed for {self.image}")
            except Exception as e:
                raise Exception(f"Build execution failed: {e}")

            return f"run {self.run_args} {self.image}"

        except Exception as e:
            raise Exception(f"build failed: {e}")

    def run(self, cmd: str = "", headless: bool = True, **kwargs) -> dict | None:
        try:
            args = " ".join(f"-{k} {v}" for k, v in kwargs.items())
            full = f"{self.build} {args} {cmd}".strip()

            try:
                return self.docker.run(cmd=full, headless=headless, **kwargs)
            except Exception as e:
                raise Exception(f"Docker run failed: {e}")

        except Exception as e:
            raise Exception(f"run failed: {e}")