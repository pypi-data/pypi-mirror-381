import argparse
import subprocess
import sys
import importlib
from help50lite.engine import get_help
from pathlib import Path


def load_helpers():
    helpers_path = Path(__file__).parent / "helpers"
    for file in helpers_path.glob("*.py"):
        if file.name == "__init__.py":
            continue
        module_name = f"help50lite.helpers.{file.stem}"
        importlib.import_module(module_name)


def run_command(command):
    proc = subprocess.Popen(command, shell=True,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT)
    out, _ = proc.communicate()
    return out.decode()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command", nargs=argparse.REMAINDER)
    args = parser.parse_args()

    if not args.command:
        print("Careful, you forgot to tell me with which command you need help!")
        sys.exit(1)

    load_helpers()

    script = run_command(" ".join(args.command))
    print("\nAsking for help...\n")
    help_msg = get_help(script, domain="make")

    if help_msg:
        before, after = help_msg
        print(before)
        print(after)
    else:
        print("Sorry, I don't know how to help with this yet.")
