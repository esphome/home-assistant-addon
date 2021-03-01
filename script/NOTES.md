# Maintainer notes

This repository is pulled by all Hassio installs and contains
the Hassio config for each type of install: latest, beta and dev.

- `latest` always points to the most recent full release.
- `beta` points to the most recent full release or beta release (whichever is newer). This is so that beta image users automatically get upgraded to the stable install once it gets released.
- `dev` is an image that Hassio builds itself and contains the latest ESPHome version straigt from dev branch.

The config.json files are all automatically written with the script in this directory and the `template/addon_config.yaml` file.

To update one of the images: use

```bash
$ pip3 install -r script/requirements.txt
$ python3 script/generate.py [dev|beta|latest]
```

The `esphome-dev/rootfs` folder is shared with the `docker/rootfs` folder in the esphome repo.
This could be solved better, but currently `rsync` is used to copy the files over:

```bash
rsync -av ../esphome/docker/rootfs esphome-dev/
```
