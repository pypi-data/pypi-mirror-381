from functools import cached_property
from loguru import logger as log
from pywershell import Debian

DEBUG = True


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
        "apt-get update",
        "apt-get install -y curl",
        "curl -fsSL https://get.docker.com -o get-docker.sh",
        "sudo sh get-docker.sh",
        "sudo usermod -aG docker mileslib"
    ]

    BOOT_DOCKER = [
        "grep -q WSL2 /proc/version",
        "sudo service docker start",
        "docker info"
    ]

    @cached_property
    def version(self):
        ver_cmd = "docker --version"
        try:
            resp = self.debian.run_bash(ver_cmd)
            version = resp["output"]
            if resp["success"] and "Docker version" in version:
                log.info(f"{self}: {version}")
                return version
            else:
                raise Exception("Docker not found")

        except Exception as e:
            log.warning(f"Docker not ready: {e}. Installing Docker...")

            for cmd in self.INSTALL_DOCKER:
                result = self.debian.run_bash(cmd, headed=True)
                if not result["success"]:
                    log.error(f"Failed to execute: {cmd}")
                    log.error(result["error"])

            for cmd in self.BOOT_DOCKER:
                result = self.debian.run_bash(cmd)
                if not result["success"]:
                    log.warning(f"Boot command failed: {cmd}")

            resp = self.debian.run_bash(ver_cmd)
            version = resp["output"]
            if resp["success"] and "Docker version" in version:
                log.success(f"{self}: {version}")
                return version
            raise Exception("Failed to install Docker")

    def run(self, cmd: str | list[str], headless: bool = True, **kwargs) -> dict | None:
        if isinstance(cmd, str):
            cmd = [cmd]
        cmds = cmd

        results = []
        for i, single_cmd in enumerate(cmds):
            full_cmd = f"{self.PREFIX} {single_cmd}"
            log.debug(f"{self}: Executing command {i}/{len(results)}: {full_cmd}...")
            result = self.debian.run_bash(full_cmd, headless=headless, **kwargs)
            results.append(result)

            if not result["success"] and not headless:
                log.error(f"Command failed: {full_cmd}")
                log.error(result["error"])

        return results[-1] if results else None

    @cached_property
    def images(self) -> list:
        log.debug(f"{self}: Retrieving images...")
        cmd = "images --format {{.Repository}}"
        resp = self.run(cmd)

        if not resp or not resp["success"]:
            log.warning(f"{self} Failed to retrieve images.")
            return []

        out_str = resp["output"]
        imgs = [line.strip() for line in out_str.splitlines() if line.strip()]

        if imgs:
            log.info(f"{self} Available Images:\n" + "\n".join(f"  - {img}" for img in imgs))
        else:
            log.warning(f"{self} No images found.")
        return imgs

    def uninstall(self, purge: bool = False):
        log.warning(f"{self}: Uninstalling Docker from WSL...")
        cmds = [
            "sudo service docker stop",
            "sudo apt-get remove -y docker docker-engine docker.io containerd runc docker-ce docker-ce-cli",
        ]
        if purge:
            cmds += [
                "sudo apt-get purge -y docker-ce docker-ce-cli containerd.io",
                "sudo rm -rf /var/lib/docker",
                "sudo rm -rf /var/lib/containerd",
                "sudo rm -rf /etc/docker",
                "sudo rm -rf ~/.docker",
            ]

        for cmd in cmds:
            result = self.debian.run_bash(cmd)
            if not result["success"]:
                log.warning(f"Uninstall command failed: {cmd}")