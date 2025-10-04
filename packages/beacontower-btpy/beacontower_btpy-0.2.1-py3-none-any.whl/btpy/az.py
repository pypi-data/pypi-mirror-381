import shlex
import subprocess
import json


def az(command: str):
    args = ["az", *shlex.split(command), "--output", "json"]
    program = subprocess.run(args, capture_output=True, text=True)

    return program.returncode, json.loads(program.stdout), program.stderr
