#!/usr/bin/env python3

import argparse
from pathlib import Path
from enum import Enum
from shutil import copyfile
import sys
import os

import yaml


class Channel(Enum):
    stable = "stable"
    beta = "beta"
    dev = "dev"


def main(args):
    parser = argparse.ArgumentParser(
        description="Generate ESPHome Home Assistant config.json"
    )
    parser.add_argument("channels", nargs="+", type=Channel, choices=list(Channel))
    args = parser.parse_args(args)

    root = Path(__file__).parent.parent
    templ = root / "template"

    with open(templ / "addon_config.yaml", "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    copyf = config["copy_files"]

    for channel in args.channels:
        conf = config[f"esphome-{channel.value}"]
        dir_ = root / conf.pop("directory")
        path = dir_ / "config.yaml"
        with open(path, "w", encoding="utf-8") as f:
            yaml.dump(conf, f, indent=2, sort_keys=False, explicit_start=True)

        for file_ in copyf:
            os.makedirs(dir_ / Path(file_).parent, exist_ok=True)
            if Path.exists(templ / channel.value / file_):
                copyfile(templ / channel.value / file_, dir_ / file_)
            else:
                copyfile(templ / file_, dir_ / file_)

        path = dir_ / "FILES ARE GENERATED DO NOT EDIT"
        with open(path, "w", encoding="utf-8") as f:
            f.write("Any edits should be made to the files in the 'template' directory")


if __name__ == "__main__":
    main(sys.argv[1:])
