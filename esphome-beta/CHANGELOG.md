## 2025.3.0

## Full list of changes

### New Components

- [ld2450] Add new component [esphome#5674](https://github.com/esphome/esphome/pull/5674) by @hareeshmu (new-integration)
- Adding support for chsc6x touch controller [esphome#8258](https://github.com/esphome/esphome/pull/8258) by @kkosik20 (new-integration)
- MSA311 and MSA301 accelerometer support [esphome#6795](https://github.com/esphome/esphome/pull/6795) by @latonita (new-integration)
- Cover component for Tormatic and Novoferm garage doors [esphome#5933](https://github.com/esphome/esphome/pull/5933) by @ti-mo (new-integration)

### Breaking Changes

- [mlx90393] Fix inverted gain and resolution. Expose temperature_compensation and hallconf. [esphome#7635](https://github.com/esphome/esphome/pull/7635) by @functionpointer (breaking-change)
- [touchscreen] Axis swap bugfix [esphome#8376](https://github.com/esphome/esphome/pull/8376) by @clydebarrow (breaking-change)
- [cst816] Remove binary sensor [esphome#8377](https://github.com/esphome/esphome/pull/8377) by @clydebarrow (breaking-change)

### Beta Changes

- Bump mdns library to 1.8.0 [esphome#8378](https://github.com/esphome/esphome/pull/8378) by @bdraco
- [audio, mixer] Memory and CPU performance improvements [esphome#8387](https://github.com/esphome/esphome/pull/8387) by @kahrendt
- [speaker, resampler, mixer] Make volume and mute getters virtual [esphome#8391](https://github.com/esphome/esphome/pull/8391) by @kahrendt
- [core] add reallocation support to RAMAllocator [esphome#8390](https://github.com/esphome/esphome/pull/8390) by @kahrendt
- [api] add voice assistant announce to the api [esphome#8395](https://github.com/esphome/esphome/pull/8395) by @kahrendt
- Bump aioesphomeapi to 29.6.0 [esphome#8396](https://github.com/esphome/esphome/pull/8396) by @bdraco
- Rework pyproject.toml to make it parseable by dependabot [esphome#8397](https://github.com/esphome/esphome/pull/8397) by @bdraco
- Bump cryptography to 44.0.2 [esphome#8399](https://github.com/esphome/esphome/pull/8399) by @bdraco
- Bump tornado from 6.4 to 6.4.2 [esphome#8398](https://github.com/esphome/esphome/pull/8398) by @dependabot[bot]
- [font] Fix issues with bitmap fonts [esphome#8407](https://github.com/esphome/esphome/pull/8407) by @clydebarrow
- Added getters for graphs ymin and ymax [esphome#8112](https://github.com/esphome/esphome/pull/8112) by @Duckle29
- [docker] Bump curl, git, openssh-client, libopenjp2-7, nginx-light [esphome#8419](https://github.com/esphome/esphome/pull/8419) by @kbx81
- [docker] Bump libfreetype [esphome#8426](https://github.com/esphome/esphome/pull/8426) by @kbx81
- [core] Handle mis-typed platform name more cleanly [esphome#8424](https://github.com/esphome/esphome/pull/8424) by @clydebarrow
- [audio] Bugfix: fix flac decoding glitches by using esp-audio-libs v1.1.3 [esphome#8431](https://github.com/esphome/esphome/pull/8431) by @kahrendt

### All changes

- [modbus_controller] Extend tests [esphome#8245](https://github.com/esphome/esphome/pull/8245) by @kbx81
- Switch to native arm runners for docker CI [esphome#8262](https://github.com/esphome/esphome/pull/8262) by @bdraco
- Use the process CPU count to determine how many children to create [esphome#8268](https://github.com/esphome/esphome/pull/8268) by @bdraco
- Bump actions/cache from 4.2.0 to 4.2.1 in /.github/actions/restore-python [esphome#8273](https://github.com/esphome/esphome/pull/8273) by @dependabot[bot]
- Bump actions/cache from 4.2.0 to 4.2.1 [esphome#8271](https://github.com/esphome/esphome/pull/8271) by @dependabot[bot]
- Ruff format for CI [esphome#8276](https://github.com/esphome/esphome/pull/8276) by @stellar-aria
- [ld2450] Add new component [esphome#5674](https://github.com/esphome/esphome/pull/5674) by @hareeshmu (new-integration)
- Bump docker/build-push-action from 6.13.0 to 6.14.0 in /.github/actions/build-image [esphome#8281](https://github.com/esphome/esphome/pull/8281) by @dependabot[bot]
- Finish up transition from black-format to ruff [esphome#8294](https://github.com/esphome/esphome/pull/8294) by @stellar-aria
- [core, dashboard] load external component to get get_download_types [esphome#8139](https://github.com/esphome/esphome/pull/8139) by @tomaszduda23
- [ota] set USE_OTA_VERSION 2 in defines [esphome#8299](https://github.com/esphome/esphome/pull/8299) by @tomaszduda23
- [socket] add connect method [esphome#8308](https://github.com/esphome/esphome/pull/8308) by @kahrendt
- Bump peter-evans/create-pull-request from 7.0.6 to 7.0.7 [esphome#8314](https://github.com/esphome/esphome/pull/8314) by @dependabot[bot]
- Bump actions/upload-artifact from 4.6.0 to 4.6.1 [esphome#8295](https://github.com/esphome/esphome/pull/8295) by @dependabot[bot]
- [api] ensure fair network sharing + prevent lost state changes via deferred publish at high event load [esphome#7547](https://github.com/esphome/esphome/pull/7547) by @nkinnan
- ili9xxx: Add support for GC9D01N circle display [esphome#8302](https://github.com/esphome/esphome/pull/8302) by @rforro
- web_server: ensure fair network sharing + prevent lost state changes via deferred publish at high event load [esphome#7538](https://github.com/esphome/esphome/pull/7538) by @nkinnan
- [i2c] python code style [esphome#8311](https://github.com/esphome/esphome/pull/8311) by @tomaszduda23
- Adding support for chsc6x touch controller [esphome#8258](https://github.com/esphome/esphome/pull/8258) by @kkosik20 (new-integration)
- [core] make upload_program more generic [esphome#8321](https://github.com/esphome/esphome/pull/8321) by @tomaszduda23
- [i2c] Fix i2c issue on idf 5.3 [esphome#8283](https://github.com/esphome/esphome/pull/8283) by @swoboda1337
- [core] SplitDefault unit test [esphome#8324](https://github.com/esphome/esphome/pull/8324) by @tomaszduda23
- Add option to include vars in remote packages [esphome#7606](https://github.com/esphome/esphome/pull/7606) by @pszafer
- [ld2450] Fix for "unknown" sensor states [esphome#8305](https://github.com/esphome/esphome/pull/8305) by @kbx81
- Update arduino-heatpumpir and add new protocol for Panasonic AC [esphome#8309](https://github.com/esphome/esphome/pull/8309) by @barchasse38
- MSA311 and MSA301 accelerometer support [esphome#6795](https://github.com/esphome/esphome/pull/6795) by @latonita (new-integration)
- Include the bluetooth mac address in the device info when proxy is enabled [esphome#8203](https://github.com/esphome/esphome/pull/8203) by @bdraco
- dashboard: Implement automatic ping fallback [esphome#8263](https://github.com/esphome/esphome/pull/8263) by @bdraco
- [ld2450] Fix misplaced ``ifdef`` and related logic [esphome#8335](https://github.com/esphome/esphome/pull/8335) by @kbx81
- Bump the docker-actions group with 2 updates [esphome#8330](https://github.com/esphome/esphome/pull/8330) by @dependabot[bot]
- Bump actions/download-artifact from 4.1.8 to 4.1.9 [esphome#8331](https://github.com/esphome/esphome/pull/8331) by @dependabot[bot]
- Bump docker/build-push-action from 6.14.0 to 6.15.0 in /.github/actions/build-image [esphome#8332](https://github.com/esphome/esphome/pull/8332) by @dependabot[bot]
- [mlx90393] Fix inverted gain and resolution. Expose temperature_compensation and hallconf. [esphome#7635](https://github.com/esphome/esphome/pull/7635) by @functionpointer (breaking-change)
- [font] Use freetype instead of Pillow for font rendering [esphome#8300](https://github.com/esphome/esphome/pull/8300) by @clydebarrow
- Bump actions/cache from 4.2.1 to 4.2.2 [esphome#8336](https://github.com/esphome/esphome/pull/8336) by @dependabot[bot]
- Bump actions/cache from 4.2.1 to 4.2.2 in /.github/actions/restore-python [esphome#8337](https://github.com/esphome/esphome/pull/8337) by @dependabot[bot]
- [zeroconf] Ruff formatting [esphome#8338](https://github.com/esphome/esphome/pull/8338) by @jesserockz
- [nrf52, core] unified way how all platforms handle SplitDefault [esphome#7715](https://github.com/esphome/esphome/pull/7715) by @tomaszduda23
- Cover component for Tormatic and Novoferm garage doors [esphome#5933](https://github.com/esphome/esphome/pull/5933) by @ti-mo (new-integration)
- [io_bus] Initial implementation [esphome#8227](https://github.com/esphome/esphome/pull/8227) by @clydebarrow (new-integration)
- [tmp1075] fix component for TMP1075N [esphome#8317](https://github.com/esphome/esphome/pull/8317) by @ssieb
- Bump docker/setup-qemu-action from 3.5.0 to 3.6.0 in the docker-actions group [esphome#8346](https://github.com/esphome/esphome/pull/8346) by @dependabot[bot]
- [dashboard] Rename trash/delete to archive [esphome#8357](https://github.com/esphome/esphome/pull/8357) by @jesserockz
- [helpers] Allow RAMAllocator to be told the size of the object manually [esphome#8356](https://github.com/esphome/esphome/pull/8356) by @jesserockz
- [ld2450] fix null exception & zone target_count not published [esphome#8348](https://github.com/esphome/esphome/pull/8348) by @mistic100
- [bmp085] Fix error in read of pressure [esphome#8359](https://github.com/esphome/esphome/pull/8359) by @gusdleon
- [udp] fix clang tidy [esphome#8351](https://github.com/esphome/esphome/pull/8351) by @tomaszduda23
- [i2s_audio] Bugfix: Speaker incorrectly delays when sending data [esphome#8361](https://github.com/esphome/esphome/pull/8361) by @kahrendt
- Initialise h-bridge switch to requested initial state [esphome#8363](https://github.com/esphome/esphome/pull/8363) by @AnyOldName3
- [lvgl] Fix initialisation race condition (Bugfix) [esphome#8369](https://github.com/esphome/esphome/pull/8369) by @clydebarrow
- [time] fix recalc_timestamp_local [esphome#8239](https://github.com/esphome/esphome/pull/8239) by @qraynaud
- allow touchscreen buttons outside of display dimensions [esphome#8296](https://github.com/esphome/esphome/pull/8296) by @zendes
- [touchscreen] Axis swap bugfix [esphome#8376](https://github.com/esphome/esphome/pull/8376) by @clydebarrow (breaking-change)
- [cst816] Remove binary sensor [esphome#8377](https://github.com/esphome/esphome/pull/8377) by @clydebarrow (breaking-change)
- Revert "[io_bus] Initial implementation" [esphome#8384](https://github.com/esphome/esphome/pull/8384) by @clydebarrow
- Bump aioesphomeapi to 29.5.1 [esphome#8364](https://github.com/esphome/esphome/pull/8364) by @bdraco
- Bump esptool to 4.8.1latest [esphome#8367](https://github.com/esphome/esphome/pull/8367) by @shvmm
- Bump zeroconf to 0.146.1 [esphome#8365](https://github.com/esphome/esphome/pull/8365) by @bdraco
- mcp2515: Add missing CFG1 assignment to be able to use 50kbps with a 16MHz crystal. [esphome#8375](https://github.com/esphome/esphome/pull/8375) by @djasper-ha
