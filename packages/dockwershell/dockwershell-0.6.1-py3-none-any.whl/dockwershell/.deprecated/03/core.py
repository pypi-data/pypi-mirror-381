from functools import cached_property

from loguru import logger as log
from pywershell import Debian, CMDResult
from singleton_decorator import singleton

DEBUG = True


@singleton
class Docker:
    def __init__(self):
        self.debian = Debian()
        _ = self.version
        _ = self.images

    def __repr__(self):
        return "[Docker]"

    PREFIX = "docker"

    VERSION = "--version"

    INSTALL_DOCKER = [
        "'apt-get update'",
        "'apt-get install -y curl'",
        "'curl -fsSL https://get.docker.com -o get-docker.sh'",
        "'sudo sh get-docker.sh'",
        "'sudo usermod -aG docker mileslib'"
    ]

    BOOT_DOCKER = [
        "'grep -q WSL2 /proc/version'",
        "'sudo service docker start'",
        "'docker info'"
    ]

    def version(self):
        ver_cmd = "--version"
        try:
            resp = self.run(ver_cmd)
            version = resp.output
            if "Docker version" in version:
                log.info(f"{self}: {version}")
                return version
            else:
                raise Exception

        except Exception as e:
            log.warning(f"Docker not ready: {e}. Installing _Docker...")
            self.debian.run(self.INSTALL_DOCKER)
            self.debian.run(self.BOOT_DOCKER)

            resp = self.debian.run(ver_cmd)
            version = resp.output
            if "_Docker version" in version:
                log.success(f"{self}: {version}")
                return version
            raise Exception

    def run(self, cmd: str | list[str], headless: bool = True, **kwargs) -> CMDResult | None:
        if isinstance(cmd, str): cmd = [cmd]
        cmds = cmd

        for i, cmd in enumerate(cmds):
            log.debug(f"{self}: Executing command {i}...")
            cmds[i] = f"'{self.PREFIX} {cmd}'"

        return self.debian.run(cmds, headless=headless)

    @cached_property
    def images(self) -> list:
        log.debug(f"{self}: Retrieving images...")
        cmd = "images --format {{.Repository}}"
        resp = self.run(cmd)
        out_str = resp.output
        imgs = [line.strip() for line in out_str.splitlines() if line.strip()]
        if imgs:
            log.info(f"{self} Available Images:\n" + "\n".join(f"  - {img}" for img in imgs))
        else:
            log.warning(f"{self} No images found.")
        return imgs

    def uninstall(self, purge: bool = False):
        log.warning(f"{self}: Uninstalling _Docker from WSL...")
        cmds = [
            "'sudo service docker stop'",
            "'sudo apt-get remove -y docker docker-engine docker.io containerd runc docker-ce docker-ce-cli'",
        ]
        if purge:
            cmds += [
                "'sudo apt-get purge -y docker-ce docker-ce-cli containerd.io'",
                "'sudo rm -rf /var/lib/docker'",
                "'sudo rm -rf /var/lib/containerd'",
                "'sudo rm -rf /etc/docker'",
                "'sudo rm -rf ~/.docker'",
            ]
        out = self.debian.run(cmds)


_docker_singleton_instance = None


def docker(**kwargs) -> Docker:
    """
    Async Docker instance getter that handles singleton properly.

    Args:
        verbose: Enable verbose logging

    Returns:
        Initialized _Docker instance
    """
    global _docker_singleton_instance

    if _docker_singleton_instance is not None:
        if DEBUG: log.debug("[Docker]: Returning cached singleton instance")
        return _docker_singleton_instance

    try:
        if DEBUG: log.debug("[Docker]: Creating new singleton instance")
        _docker_singleton_instance = Docker(**kwargs)
        if DEBUG:
            log.success("[Docker]: Singleton instance created successfully")
        return _docker_singleton_instance
    except RuntimeError as e:
        if "cannot reuse already awaited coroutine" in str(e):
            if DEBUG: log.warning("[Docker]: Coroutine reuse detected, returning existing instance")
            return _docker_singleton_instance
        raise
