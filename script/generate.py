#!/usr/bin/env python3

import argparse
import yaml
from pathlib import Path
from enum import Enum
from shutil import copyfile
import sys


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

    with open(templ / "addon_config.yaml", "r") as f:
        config = yaml.safe_load(f)

    copyf = config["copy_files"]

    for channel in args.channels:
        conf = config[f"esphome-{channel.value}"]
        base_image = conf.pop("base_image", None)
        dir_ = root / conf.pop("directory")
        path = dir_ / "config.yaml"
        with open(path, "w") as f:
            yaml.dump(conf, f, indent=2, sort_keys=True, explicit_start=True)

        for file_, conf_ in copyf.items():
            if Path.exists(templ / channel.value / file_):
                copyfile(templ / channel.value / file_, dir_ / file_)
            else:
                copyfile(templ / file_, dir_ / file_)

        path = dir_ / "FILES ARE GENERATED DO NOT EDIT"
        with open(path, "w") as f:
            f.write("Any edits should be made to the files in the 'template' directory")

        if channel == Channel.dev:
            path = dir_ / "build.yaml"
            build_conf = {
                "build_from": {
                    arch: base_image.format(arch=arch) for arch in conf["arch"]
                }
            }
            with open(path, "w") as f:
                yaml.dump(build_conf, f, indent=2, sort_keys=True, explicit_start=True)


if __name__ == "__main__":
    main(sys.argv[1:])
