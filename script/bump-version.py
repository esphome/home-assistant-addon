#!/usr/bin/env python3

import argparse
import re
import subprocess
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
    dev: bool = False

    def __str__(self):
        return f'{self.major}.{self.minor}.{self.full_patch}'

    @property
    def full_patch(self):
        res = f'{self.patch}'
        if self.beta > 0:
            res += f'b{self.beta}'
        if self.dev:
            res += '-dev'
        return res

    @classmethod
    def parse(cls, value):
        match = re.match(r'(\d+).(\d+).(\d+)(b\d+)?(-dev)?', value)
        assert match is not None
        major = int(match[1])
        minor = int(match[2])
        patch = int(match[3])
        beta = int(match[4][1:]) if match[4] else 0
        dev = bool(match[5])
        return Version(
            major=major, minor=minor, patch=patch,
            beta=beta, dev=dev
        )


def sub(path, pattern, repl, expected_count=1):
    with open(path) as fh:
        content = fh.read()
    content, count = re.subn(pattern, repl, content, flags=re.MULTILINE)
    if expected_count is not None:
        assert count == expected_count, f"Pattern {pattern} replacement failed!"
    with open(path, "wt") as fh:
        fh.write(content)


def write_version(target: str, version: Version):
    #  version: '1.14.5'  # BETA
    #  version: '1.14.5'  # STABLE
    sub(
        'template/addon_config.yaml',
        r"  version: '[^']+'  # {}".format(target.upper()),
        f"  version: '{version}'  # {target.upper()}"
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('new_version', type=str)
    args = parser.parse_args()

    version = Version.parse(args.new_version)
    assert not version.dev

    print(f"Bumping to {version}")
    if version.beta:
        write_version('beta', version)
        generate.main(['beta'])
    else:
        assert not version.beta
        write_version('stable', version)
        write_version('beta', version)
        generate.main(['stable', 'beta'])
    return 0


if __name__ == "__main__":
    sys.exit(main() or 0)
