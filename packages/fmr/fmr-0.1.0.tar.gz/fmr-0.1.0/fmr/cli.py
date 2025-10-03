#!/usr/bin/env python3
import os
import sys
import json
import subprocess
from pathlib import Path

CONFIG_FILE = Path.home() / ".view_config.json"


def load_config():
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    return {}


def save_config(config):
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=4)


def get_root():
    config = load_config()
    root = config.get("repos_root")
    if not root:
        print("Repos root has not been set. Use '--set-root <path>' to set it.")
        sys.exit(1)
    return root


def set_root(path):
    if not os.path.isdir(path):
        print(f"Error: {path} is not a directory.")
        sys.exit(1)
    save_config({"repos_root": os.path.abspath(path)})
    print(f"Repos root set to {path}")

def reset_root():
    if CONFIG_FILE.exists():
        CONFIG_FILE.unlink()
        print(f"Repos root has been reset.")
    else:
        print(f"Repos root has been reset already.")

def open_repo(repo_name):
    root = get_root()
    repo_path = os.path.join(root, repo_name)
    if os.path.isdir(repo_path):
        subprocess.run(["code", repo_path])
    else:
        print(f"Repo '{repo_name}' not found in {root}")


def list_repos():
    root = get_root()
    if not os.path.isdir(root):
        print(f"Repos root '{root}' does not exist.")
        return
    repos = [f for f in os.listdir(root) if os.path.isdir(os.path.join(root, f))]
    print("Repos in root:")
    for r in repos:
        print(f"  - {r}")


def show_root():
    root = get_root()
    print(f"Current repos root: {root}")


def show_help():
    help_text = """
Usage: fmr [command] [arguments]

Commands:
  <repo_name>         Opens <repo_name> in VS Code.
  --list              Lists all repos in the root.
  --show-root         Shows the current repos root.
  --set-root <path>   Sets a new repos root directory.
  --reset-root        Resets the repos root.
  --help              Shows this help message.
"""
    print(help_text)


def main():
    if len(sys.argv) < 2:
        show_help()
        sys.exit(0)

    if sys.argv[1] == "--set-root" and len(sys.argv) == 3:
        set_root(sys.argv[2])
    elif sys.argv[1] == "--reset-root":
        reset_root()
    elif sys.argv[1] == "--list":
        list_repos()
    elif sys.argv[1] == "--show-root":
        show_root()
    elif sys.argv[1] == "--help":
        show_help()
    else:
        repo_name = sys.argv[1]
        open_repo(repo_name)


if __name__ == "__main__":
    main()
