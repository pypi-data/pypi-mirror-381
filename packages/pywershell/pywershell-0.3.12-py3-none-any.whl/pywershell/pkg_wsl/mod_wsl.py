import json
import re
import subprocess
import tempfile
import os
import time
from typing import Any

from annotated_dict import AnnotatedDict

from pywershell.pkg_wsl.mod_util import _smart_decode


class WSLResponse(AnnotatedDict):
    success: bool
    output: str
    error: str
    returncode: int
    argv: Any

    @property
    def json(self):
        if not self.output:
            return None

        json_pattern = r'\{(?:[^{}]|(?:\{(?:[^{}]|(?:\{[^{}]*\}))*\}))*\}|\[(?:[^\[\]]|(?:\[(?:[^\[\]]|(?:\[[^\[\]]*\]))*\]))*\]'
        matches = re.findall(json_pattern, self.output, re.DOTALL)

        parsed_results = []
        for match in matches:
            try:
                parsed_results.append(json.loads(match))
            except json.JSONDecodeError:
                continue

        if len(parsed_results) == 0:
            return None
        elif len(parsed_results) == 1:
            return parsed_results[0]
        else:
            return parsed_results



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

    def run(self, args: list[str] | str, timeout: float | None = None, headless: bool = True, **kwargs) -> WSLResponse:
        if isinstance(args, str):
            import shlex
            extra = shlex.split(args, posix=True)
        else:
            extra = list(args)

        argv = self._build_base_argv() + extra

        if not headless:
            res = self._run_headed(argv, timeout)
            return WSLResponse(**res)

        try:
            res = subprocess.run(
                argv,
                capture_output=True,
                text=False,
                cwd=self.cwd,
                timeout=timeout
            )
            return WSLResponse(
                success=res.returncode == 0,
                output=_smart_decode(res.stdout),
                error=_smart_decode(res.stderr),
                returncode=res.returncode,
                argv=argv,
            )
        except subprocess.TimeoutExpired as e:
            return WSLResponse(
                success=False,
                output="",
                error=f"Timeout after {timeout}s",
                returncode=-1,
                argv=argv,
            )
        except Exception as e:
            return WSLResponse(
                success=False,
                output="",
                error=str(e),
                returncode=-1,
                argv=argv,
            )

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
                 headless: bool = True) -> WSLResponse:
        bash_args = ['--', 'bash']
        if login_shell:
            bash_args.append('-l')
        bash_args += ['-c', bash_command]
        return self.run(bash_args, timeout=timeout, headless=headless)

    def version(self) -> dict:
        return self.run(['--version'])