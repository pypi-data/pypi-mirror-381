from typing import List
from functools import cached_property

from loguru import logger as log
from singleton_decorator import singleton

from gowershell import Gowershell, Response

class Pywersl:
    """
    Pywershell Windows System for Linux
    """
    PREFIX = "powershell.exe wsl"

    @cached_property
    def version(self):
        # key = "wslinit"
        # cmd = " ".join(["echo", key])
        resp: Response = Gowershell().execute("wsl --version")
        ver = resp.output.splitlines()
        wsl_vers: str = ver[0]
        item = f"{wsl_vers}"
        if not item in wsl_vers:
            raise RuntimeError
        wsl_vers_num: str = wsl_vers.replace("WSL version: ", "")
        log.success(f"{self}: Running WSL Version: {wsl_vers_num}")
        return wsl_vers_num

    def run(self, cmd: str | list, headless: bool = True, verbose: bool = None) -> Response | List[Response]:
        if isinstance(cmd, str):
            cmd = [cmd]
        resps: list[Response] = []
        for command in cmd:
            resp = Gowershell().execute(
                f"{self.PREFIX} {command}",
                headless=headless,
                persist_window=False,
                verbose=verbose
            )
            resps.append(resp)
            if verbose is None or verbose:
                log.debug(resp)
        if len(resps) == 1:
            return resps[0]
        else:
            return resps


@singleton
class Debian(Pywersl):
    CHECK = "--list --quiet"
    INSTALL = "--install Debian"
    POST_INSTALL = [
        '-d Debian -u root -- bash -c "apt update && apt upgrade -y"',
        '-d Debian -u root -- bash -c "apt install -y docker.io docker-compose && usermod -aG docker $USER"',
        '-d Debian -u root -- bash -c "echo Post-install complete"',
    ]
    UNINSTALL = ["--unregister Debian"]

    def __init__(self):
        _ = self.setup  # Trigger setup property
        self.PREFIX = "wsl -d Debian -u root -- bash -c"

    def __repr__(self):
        return f"[Pywersl.Debian]"

    @property
    def users(self):
        return (Gowershell().execute("wsl -d Debian getent passwd")).output

    @cached_property
    def setup(self):
        resp = self.run(self.CHECK)
        out = resp.output
        if "Debian" in out:
            log.success(f"{self}: Successfully initialized Debian!")
        else:
            self.run(self.INSTALL, headless=False)
            self.run(self.POST_INSTALL)
        return True

    def uninstall(self):
        out = self.run(self.UNINSTALL)
        if "The operation completed successfully." in out.str:
            log.warning(f"{self}: Successfully uninstalled!")
            return
        raise RuntimeWarning(f"{self}: Could not uninstall!")