from pywershell.pkg_wsl.mod_wsl import WSL

class Debian(WSL):
    """
    Convenience subclass with Debian and root defaults:
      wsl -d Debian -u root ...
    """
    def __init__(self, user: str = 'root', cwd: str | None = None):
        self.wsl = WSL()
        super().__init__(distribution='Debian', user=user, cwd=cwd)