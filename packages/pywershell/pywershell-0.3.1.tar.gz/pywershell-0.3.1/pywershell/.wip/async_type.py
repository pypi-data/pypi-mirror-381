import os
import subprocess
import threading
import queue
import json
import re
import sys
import time


class SessionedTerminal:
    def __init__(self, process='cmd', headless=True, cwd=None, prefix=None):
        self.headless = headless
        self.cwd = cwd
        self.process_type = process
        self.prefix = prefix

        process_commands = {
            'cmd': 'cmd.exe',
            'powershell': 'powershell.exe -NoLogo'
        }

        if process not in process_commands:
            raise ValueError(f"Invalid process type. Must be one of: cmd, powershell")

        self.command = process_commands[process]

        self.default_encoding = {
            'cmd': 'cp437',
            'powershell': 'utf-8'
        }[process]

        if headless:
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            startupinfo.wShowWindow = subprocess.SW_HIDE

            self.process = subprocess.Popen(
                self.command,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                shell=True,
                bufsize=0,
                universal_newlines=False,
                startupinfo=startupinfo,
                cwd=cwd
            )
            self.output_queue = queue.Queue()
            self.running = True
            self.read_thread = threading.Thread(target=self._read_loop, daemon=True)
            self.read_thread.start()
            self.command_counter = 0
            self.read_all(timeout=1.0)
        else:
            self.process = None
            self.output_queue = None
            self.running = False
            self.read_thread = None
            self.command_counter = 0

    def _read_loop(self):
        while self.running:
            try:
                char = self.process.stdout.read(1)
                if char:
                    self.output_queue.put(char)
                else:
                    break
            except Exception as e:
                if self.running:
                    print(f"Read error: {e}")
                break

    def write(self, data):
        if isinstance(data, str):
            data = data.encode()
        self.process.stdin.write(data)
        self.process.stdin.flush()

    def _extract_json(self, text):
        json_pattern = r'\{(?:[^{}]|(?:\{(?:[^{}]|(?:\{[^{}]*\}))*\}))*\}'

        matches = re.findall(json_pattern, text, re.DOTALL)

        for match in matches:
            try:
                parsed = json.loads(match)
                return parsed
            except json.JSONDecodeError:
                continue

        array_pattern = r'\[(?:[^\[\]]|(?:\[(?:[^\[\]]|(?:\[[^\[\]]*\]))*\]))*\]'
        matches = re.findall(array_pattern, text, re.DOTALL)

        for match in matches:
            try:
                parsed = json.loads(match)
                return parsed
            except json.JSONDecodeError:
                continue

        return None

    def execute(self, command, timeout=2.0, encoding=None, verbose=False, auto_close=None):
        if encoding is None:
            encoding = self.default_encoding

        if auto_close is None:
            auto_close = self.headless

        if not self.headless:
            return self._execute_headed(command, timeout, auto_close)

        if self.prefix:
            command = f"{self.prefix} {command}"

        self.command_counter += 1
        marker = f"__CMD_END_{self.command_counter}__"

        if not command.endswith('\n'):
            command += '\n'

        self.write(command)
        self.write(f'echo {marker}\n')

        raw_output = self.read_until_marker_string(marker, timeout=timeout, verbose=verbose, encoding=encoding)
        json_data = self._extract_json(raw_output)

        if auto_close:
            self.close()

        return (raw_output, json_data)

    def read_until_marker_string(self, marker, timeout=2.0, verbose=False, encoding='utf-8'):
        start_time = time.time()
        raw_bytes = b''

        while time.time() - start_time < timeout:
            try:
                data = self.output_queue.get(timeout=0.1)
                raw_bytes += data

                text_buffer = raw_bytes.decode(encoding, errors='ignore')

                if verbose:
                    decoded = data.decode(encoding, errors='ignore')
                    if decoded.strip():
                        sys.stdout.write(decoded)
                        sys.stdout.flush()

                if marker in text_buffer:
                    marker_pos = text_buffer.find(marker)
                    return text_buffer[:marker_pos]

            except queue.Empty:
                continue

        return raw_bytes.decode(encoding, errors='ignore')

    def _execute_headed(self, command, timeout=2.0, auto_close=True):
        if self.prefix:
            command = f"{self.prefix} {command}"

        cd_command = f"cd /d {self.cwd} && " if self.cwd else ""

        if self.process_type == 'powershell':
            full_command = f'start powershell -NoExit -Command "{cd_command}{command}"'
        else:
            if auto_close:
                full_command = f'start cmd /C "{cd_command}{command} & pause"'
            else:
                full_command = f'start cmd /K "{cd_command}{command}"'

        process = subprocess.Popen(
            full_command,
            shell=True
        )

        if auto_close:
            process.wait()

        return ("Command executed in visible window", None)

    def read_all(self, timeout=0.5):
        time.sleep(timeout)
        output = []
        while True:
            try:
                data = self.output_queue.get_nowait()
                output.append(data)
            except queue.Empty:
                break
        return b''.join(output)

    def close(self):
        if self.headless and self.process:
            self.running = False
            self.process.terminate()
            self.process.wait()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()


def simple_example():
    print("=== CMD ===\n")
    term = SessionedTerminal(process='cmd', headless=True)
    text, json_data = term.execute("echo Hello from CMD", verbose=True)
    print(f"\nText: {text}\n")

    print("\n=== PowerShell ===\n")
    term = SessionedTerminal(process='powershell', headless=True)
    text, json_data = term.execute("Write-Host 'Hello from PowerShell'", verbose=True)
    print(f"\nText: {text}\n")

    print("\n=== CMD with prefix ===\n")
    term = SessionedTerminal(process='cmd', headless=True, prefix='python -c')
    text, json_data = term.execute('"print(1+1)"', verbose=True)
    print(f"\nText: {text}\n")

if __name__ == "__main__":
    simple_example()

if __name__ == "__main__":
    # Example usage of the new classes
    print("\n=== New WSL classes demo ===\n")
    wsl = WSL()
    ver = wsl.version()
    print("WSL version:", ver)

    deb = DebianWSL()
    hello = deb.run_bash("echo hello")
    print("Debian echo:", hello)

    docker = deb.run_bash("docker --version")
    print("Docker version:", docker)
