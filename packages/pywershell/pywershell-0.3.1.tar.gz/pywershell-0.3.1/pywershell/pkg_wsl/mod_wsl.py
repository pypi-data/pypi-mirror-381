import subprocess
import tempfile
import os
import time

from pywershell.pkg_wsl.mod_util import _smart_decode


class WSL:
    def __init__(self, distribution: str | None = None, user: str | None = None, cwd: str | None = None):
        self.distribution = distribution
        self.user = user
        self.cwd = cwd

    def _build_base_argv(self) -> list[str]:
        argv = ['wsl']
        if self.distribution: argv += ['-d', self.distribution]
        if self.user: argv += ['-u', self.user]
        return argv

    def run(self, args: list[str] | str, timeout: float | None = None, headed: bool = False) -> dict:
        if isinstance(args, str):
            import shlex
            extra = shlex.split(args, posix=True)
        else:
            extra = list(args)

        argv = self._build_base_argv() + extra

        if headed:
            return self._run_headed(argv, timeout)

        try:
            res = subprocess.run(
                argv,
                capture_output=True,
                text=False,
                cwd=self.cwd,
                timeout=timeout
            )
            return {
                "success": res.returncode == 0,
                "output": _smart_decode(res.stdout),
                "error": _smart_decode(res.stderr),
                "returncode": res.returncode,
                "argv": argv,
            }
        except subprocess.TimeoutExpired as e:
            return {
                "success": False,
                "output": "",
                "error": f"Timeout after {timeout}s",
                "returncode": -1,
                "argv": argv,
            }
        except Exception as e:
            return {
                "success": False,
                "output": "",
                "error": str(e),
                "returncode": -1,
                "argv": argv,
            }

    def _run_headed(self, argv: list[str], timeout: float | None = None) -> dict:
        import shlex

        wsl_command = ' '.join(shlex.quote(arg) for arg in argv)
        wsl_command += ' && echo. && echo Command completed successfully. && pause'

        try:
            result = subprocess.run(
                ['cmd', '/c', 'start', '/wait', 'cmd', '/c', wsl_command],
                cwd=self.cwd,
                timeout=timeout
            )

            return {
                "success": result.returncode == 0,
                "output": "",
                "error": "",
                "returncode": result.returncode,
                "argv": argv,
            }
        except subprocess.TimeoutExpired:
            return {
                "success": False,
                "output": "",
                "error": f"Timeout after {timeout}s",
                "returncode": -1,
                "argv": argv,
            }
        except Exception as e:
            return {
                "success": False,
                "output": "",
                "error": str(e),
                "returncode": -1,
                "argv": argv,
            }

    def run_bash(self, bash_command: str, login_shell: bool = False, timeout: float | None = None,
                 headed: bool = False) -> dict:
        bash_args = ['--', 'bash']
        if login_shell:
            bash_args.append('-l')
        bash_args += ['-c', bash_command]
        return self.run(bash_args, timeout=timeout, headed=headed)

    def version(self) -> dict:
        return self.run(['--version'])