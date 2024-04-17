#!/usr/bin/env python3

import argparse
import re
from dataclasses import dataclass
import sys
import os

sys.path.append(os.path.dirname(__file__))
import generate


@dataclass
class Version:
    major: int
    minor: int
    patch: int
    beta: int = 0
    dev: str = ""

    def __str__(self):
        return f"{self.major}.{self.minor}.{self.full_patch}"

    @property
    def full_patch(self):
        res = f"{self.patch}"
        if self.beta > 0:
            res += f"b{self.beta}"
        if self.dev:
            res += f"-dev{self.dev}"
        return res

    @classmethod
    def parse(cls, value):
        match = re.match(r"(\d+).(\d+).(\d+)(b\d+)?(-dev\d+)?", value)
        assert match is not None
        major = int(match[1])
        minor = int(match[2])
        patch = int(match[3])
        beta = int(match[4][1:]) if match[4] else 0
        dev = str(match[5][4:]) if match[5] else ""
        return Version(major=major, minor=minor, patch=patch, beta=beta, dev=dev)


def _sub(path, pattern, repl, expected_count=1):
    with open(path, encoding="utf-8") as fh:
        content = fh.read()
    content, count = re.subn(pattern, repl, content, flags=re.NOFLAG)
    if expected_count is not None:
        assert count == expected_count, f"Pattern {pattern} replacement failed!"
    with open(path, "wt", encoding="utf-8") as fh:
        fh.write(content)


def _write_version(target: str, version: Version):
    #  version: "2024.5.0-dev20240412"  # DEV
    #  version: "1.14.5"  # BETA
    #  version: "1.14.5"  # STABLE
    _sub(
        "template/addon_config.yaml",
        f'  version: "[^"]+"  # {target.upper()}',
        f'  version: "{version}"  # {target.upper()}',
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("new_version", type=str)
    args = parser.parse_args()

    version = Version.parse(args.new_version)

    print(f"Bumping to {version}")
    if version.dev:
        _write_version("dev", version)
        generate.main(["dev"])
    elif version.beta:
        _write_version("beta", version)
        generate.main(["beta"])
    else:
        _write_version("stable", version)
        _write_version("beta", version)
        generate.main(["stable", "beta"])
    return 0


if __name__ == "__main__":
    sys.exit(main() or 0)
