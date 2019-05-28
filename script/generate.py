#!/usr/bin/env python3

import argparse
import yaml
from pathlib import Path
from enum import Enum
import json
from shutil import copyfile

class Channel(Enum):
    stable = 'stable'
    beta = 'beta'
    dev = 'dev'

parser = argparse.ArgumentParser(description='Generate ESPHome Hass.io config.json')
parser.add_argument('channels', nargs='+', type=Channel, choices=list(Channel))
args = parser.parse_args()

root = Path(__file__).parent.parent
templ = root / 'template'

with open(templ / "config.yaml", 'r') as f:
    config = yaml.safe_load(f)

copyf = config['copy_files']

for channel in args.channels:
    conf = config[f'esphome-{channel.value}']
    base_image = conf.pop('base_image')
    dir_ = root / conf.pop('directory')
    path = dir_ / 'config.json'
    with open(path, 'w') as f:
        json.dump(conf, f, indent=2, sort_keys=True)

    for file_, conf_ in copyf.items():
        copyfile(templ / file_, dir_ / file_)

    if channel == Channel.dev:
        path = dir_ / 'build.json'
        build_conf = {
            'squash': False,
            "build_from": {arch: base_image.format(arch=arch) for arch in conf['arch']},
            "args": {}
        }
        with open(path, 'w') as f:
            json.dump(build_conf, f, indent=2, sort_keys=True)

    print(f"Wrote {path}")
