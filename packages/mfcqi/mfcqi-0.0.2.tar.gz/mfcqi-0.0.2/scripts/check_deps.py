#!/usr/bin/env python3
"""Check for dependency conflicts in pyproject.toml minimum versions."""

import subprocess
import json
import re
import sys

try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib

with open("pyproject.toml", "rb") as f:
    data = tomllib.load(f)

deps = {}
for dep in data["project"]["dependencies"]:
    match = re.match(r"([a-zA-Z0-9_-]+)>=([0-9.]+)", dep)
    if match:
        pkg, ver = match.groups()
        deps[pkg] = ver

conflicts = []
for pkg, ver in deps.items():
    result = subprocess.run(
        f"curl -s https://pypi.org/pypi/{pkg}/{ver}/json",
        shell=True,
        capture_output=True,
        text=True,
    )
    if result.returncode == 0:
        try:
            pkg_data = json.loads(result.stdout)
            requires = pkg_data.get("info", {}).get("requires_dist", [])
            for req in requires:
                if "extra ==" in req:
                    continue
                for our_pkg, our_ver in deps.items():
                    if req.startswith(our_pkg + ">") or req.startswith(our_pkg + " "):
                        match = re.search(r">=(\d+\.\d+(?:\.\d+)?)", req)
                        if match:
                            required_ver = match.group(1)
                            req_parts = [int(x) for x in required_ver.split(".")]
                            our_parts = [int(x) for x in our_ver.split(".")]
                            while len(req_parts) < len(our_parts):
                                req_parts.append(0)
                            while len(our_parts) < len(req_parts):
                                our_parts.append(0)
                            if req_parts > our_parts:
                                conflicts.append(
                                    f"  ❌ {pkg}=={ver} requires {our_pkg}>={required_ver}, but we have >={our_ver}"
                                )
        except Exception:
            pass

if conflicts:
    print("\n⚠️  Dependency conflicts found:")
    for c in conflicts:
        print(c)
    sys.exit(1)
