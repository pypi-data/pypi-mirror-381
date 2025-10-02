"""
Ferrum: Python Project Package Manager
"""

# https://github.com/literal-gargoyle/ferrum

import os
import subprocess
import sys

__version__ = "0.1"

def forge(packages, verbose=False, summary=False):
    """
    Install the given list of Python packages using pip.
    Supports version pinning:
        - List: ["numpy", "scipy==1.10.1"]
        - Dict: {"numpy": "1.26.0", "scipy": "1.10.1"}
    Example: ferrum.forge(["numpy", "scipy==1.10.1"])
             ferrum.forge({"numpy": "1.26.0", "scipy": "1.10.1"})
    :param packages: list, tuple, or dict of packages
    :param verbose: if True, pip output is shown on error
    :param summary: If True, prints a summary of installed packages
    """
    pkgs = []
    if isinstance(packages, dict):
        for pkg, version in packages.items():
            pkgs.append(f"{pkg}=={version}")
    elif isinstance(packages, (list, tuple)):
        pkgs = [str(pkg) for pkg in packages]
    else:
        raise TypeError("Packages must be a list, tuple, or dict of package names")
    results = {}
    for pkg in pkgs:
        print(f"Forging {pkg}...")
        with open(os.devnull, "w") as devnull:
            try:
                subprocess.check_call(
                    [sys.executable, "-m", "pip", "install", pkg],
                    stdout=devnull,
                    stderr=devnull
                )
                results[pkg] = "success"
            except subprocess.CalledProcessError as e:
                results[pkg] = f"failed (exit code {e.returncode})"
                if verbose:
                    print(f"Error installing {pkg}:")
                    # Show error output by running again without silencing
                    subprocess.run(
                        [sys.executable, "-m", "pip", "install", pkg]
                    )
    if summary:
        print("Forge summary:")
        for pkg, status in results.items():
            print(f"  {pkg}: {status}")

def purge(packages, verbose=False, summary=False):
    """
    Uninstall the given list of Python packages using pip.
    Example: ferrum.purge(["numpy", "scipy"])
    :param packages: list or tuple of package names
    :param verbose: if True, pip output is shown on error
    :param summary: If True, prints a summary of installed packages
    """
    if not isinstance(packages, (list, tuple)):
        raise TypeError("Packages must be a list or tuple of package names")
    results = {}
    for pkg in packages:
        print(f"Purging {pkg}...")
        with open(os.devnull, "w") as devnull:
            try:
                subprocess.check_call(
                    [sys.executable, "-m", "pip", "uninstall", "-y", pkg],
                    stdout=devnull,
                    stderr=devnull
                )
                results[pkg] = "success"
            except subprocess.CalledProcessError as e:
                results[pkg] = f"failed (exit code {e.returncode})"
                if verbose:
                    print(f"Error uninstalling {pkg}:")
                    subprocess.run(
                        [sys.executable, "-m", "pip", "uninstall", "-y", pkg]
                    )
    if summary:
        print("Purge summary:")
        for pkg, status in results.items():
            print(f"  {pkg}: {status}")

# Example usage:
# ferrum.forge(["numpy", "scipy"], verbose=True)
# ferrum.purge(["numpy"], verbose=True, summary=True)