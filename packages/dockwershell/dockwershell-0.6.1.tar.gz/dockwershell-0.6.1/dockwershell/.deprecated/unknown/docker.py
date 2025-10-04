from functools import cached_property
from pathlib import Path

from loguru import logger as log


class DockerImage:
    instances = {}

    @staticmethod
    def to_wsl_path(pathlib_path: Path | str) -> str:
        if isinstance(pathlib_path, Path):
            pathlib_path = str(pathlib_path)
        return pathlib_path.replace(":", "").replace("\\", "/").replace("C", "/mnt/c")

    def __init__(self, dockerfile: Path, rebuild: bool = True, build_args: str | list = None):
        self.docker = Docker.get_instance()
        self.dockerfile_path = dockerfile
        self.dockerfile_str = self.to_wsl_path(self.dockerfile_path)
        self.dockerfile_parent_path = self.to_wsl_path(self.dockerfile_path.parent.resolve())
        self.image_name = self.dockerfile_path.name.replace("Dockerfile.", "")
        self.base_cmd = ["run", "-i", "--rm", self.image_name]
        found_image = self.find_image()

        self.raw_bargs = None
        if build_args:
            log.debug(f"{self}: Build args detected: {build_args}")
            self.raw_bargs = build_args
            _ = self.build_args
        if found_image is False or rebuild is True: self.build()

        log.success(f"{self}: Successfully initialized!")

    def __repr__(self):
        return f"[_Docker Image] <{self.image_name}>"

    @classmethod
    def get_instance(cls, dockerfile: Path, rebuild: bool = True, build_args: str | list = None):
        log.debug(cls.instances)
        if not dockerfile.exists():
            raise FileNotFoundError(f"Dockerfile not found at: {dockerfile}")

        dockerfile_str = str(dockerfile.resolve())
        image_name = dockerfile_str.replace("_Docker.", "")

        if image_name in cls.instances:
            return cls.instances[image_name]
        instance = cls(dockerfile, rebuild=rebuild, build_args=build_args)
        cls.instances[image_name] = instance
        return instance

    def find_image(self) -> bool:
        cmd = ["images", "--format", "{{.Repository}}"]
        log.info(f"Attempting to find image for {self.image_name}")
        result = self.docker.run(cmd, ignore_codes=[1])
        if self.image_name not in result:
            return False
        return True

    @cached_property
    def build_args(self):
        if not isinstance(self.raw_bargs, str | list): raise KeyError
        if isinstance(self.raw_bargs, str):
            rbargs = [self.raw_bargs]
        else:
            rbargs = self.raw_bargs
        bargs = []
        for arg in rbargs:
            arg = arg.strip().replace("--build_arg", "").replace("--build-arg", "")
            if "=" not in arg:
                raise ValueError(f"Invalid build arg: {arg}. Must be in KEY=VAL format.")
            bargs += ["--build-arg", arg]
        return bargs

    def build(self):
        cmd = ["build", "-f", str(self.dockerfile_str), "-t", self.image_name, str(self.dockerfile_parent_path)]
        if self.raw_bargs:
            bargs = self.build_args
            cmd.extend(bargs)
        try:
            log.debug(self.docker.run(cmd))
        except Exception as e:
            log.exception(f"[_Docker.build] Exception: {e}")
            raise

    def run(self, cmd: list = None):
        real_cmd = self.base_cmd + cmd
        if not cmd: real_cmd = self.base_cmd
        result = self.docker.run(real_cmd)
        return result


class _Docker:
    instance = None

    def __init__(self):
        from virtual_machines.wsl.wsl import wsl
        self.wsl = wsl
        # self.wsli_user = WSL.get_instance(root=False)
        self.base_cmd = ["docker"]
        self.check_docker_ready()
        log.success(f"{self}: Successfully Initialized!")

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = cls()
        return cls.instance

    def run(self, cmd: list, ignore_codes: list = None, host: str = None):
        if not isinstance(cmd, list): raise TypeError
        if ignore_codes is not None and not isinstance(ignore_codes, list):
            raise TypeError

        real_cmd = self.base_cmd.copy()

        if host:
            real_cmd += [f"--add-host=host.docker.internal:{host}"]

        real_cmd += cmd
        return self.wsl.run(real_cmd, ignore_codes=ignore_codes)

    INSTALL_DOCKER_COMMANDS = [
        ['apt-get', 'update'],
        ['apt-get', 'install', '-y', 'curl'],
        ["curl -fsSL https://get.docker.com -o get-docker.sh"],
        ["sudo sh get-docker.sh"],
        ["sudo usermod -aG docker mileslib"],
        ["docker --version"],
        ["docker compose version"]
    ]
    DOCKER_BOOT_CMDS = [
        ["grep -q '\\-WSL2' /proc/version || exit 0"],
        ['service docker status 2>&1 | grep -q "is not running"'],
        ['sudo service docker start'],
        ['docker info'],
        ['docker run hello-world']
    ]

    def check_docker_ready(self):
        check_cmd = self.base_cmd + ["version", "--format", "{{.Server.Version}}"]
        output = self.wsl.run(check_cmd, ignore_codes=[127, 1], debug=True)

        if "28.2.2" in output.lower():  # this is going to break eventually lol
            return

        if "command not found" or "'docker' could not be found" in output.lower():
            log.warning("_Docker not found. Installing...")
            try:
                output = self.wsl.looper(self.INSTALL_DOCKER_COMMANDS, ignore_codes=[1])
                log.debug(output)
            except Exception as e:
                raise RuntimeError(f"_Docker install failed: {e}")

        self.wsl.looper(self.DOCKER_BOOT_CMDS)