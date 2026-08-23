## 2026.8.1

[**Read release announcement**](https://esphome.io/changelog/2026.8.0)

- [wifi] Take the lwIP core lock around sntp_servermode_dhcp() [esphome#18511](https://github.com/esphome/esphome/pull/18511) by [@SoundGoof](https://github.com/SoundGoof)
- Bump bundled esphome-device-builder to 1.12.1 [esphome#18541](https://github.com/esphome/esphome/pull/18541) by [@esphome[bot]](https://github.com/apps/esphome)
- [nrf52] Rebuild the Python env when its interpreter symlink dangles [esphome#18540](https://github.com/esphome/esphome/pull/18540) by [@bdraco](https://github.com/bdraco)
- [core] Keep templated !include filenames as strings so Windows path normalization cannot corrupt them [esphome#18549](https://github.com/esphome/esphome/pull/18549) by [@bdraco](https://github.com/bdraco)
- Bump bundled esphome-device-builder to 1.12.2 [esphome#18573](https://github.com/esphome/esphome/pull/18573) by [@esphome[bot]](https://github.com/apps/esphome)
- [espnow] Fix dump_config crash when enable_on_boot is false [esphome#18572](https://github.com/esphome/esphome/pull/18572) by [@bdraco](https://github.com/bdraco)
- [emontx] Fix sensor state_class defaults not being applied correctly [esphome#17610](https://github.com/esphome/esphome/pull/17610) by [@FredM67](https://github.com/FredM67)
- [esp32_hosted] Fire on_update_available trigger when update is detected [esphome#18591](https://github.com/esphome/esphome/pull/18591) by [@swoboda1337](https://github.com/swoboda1337)
- Bump bundled esphome-device-builder to 1.12.3 [esphome#18601](https://github.com/esphome/esphome/pull/18601) by [@esphome[bot]](https://github.com/apps/esphome)
- Bump bundled esphome-device-builder to 1.12.4 [esphome#18651](https://github.com/esphome/esphome/pull/18651) by [@esphome[bot]](https://github.com/apps/esphome)
- [bk72xx_ble] Block BK7238 until the LibreTiny bonding partition fix lands [esphome#18649](https://github.com/esphome/esphome/pull/18649) by [@bdraco](https://github.com/bdraco)
- [esp32_ble] Log connection parameter update results [esphome#18607](https://github.com/esphome/esphome/pull/18607) by [@bdraco](https://github.com/bdraco)
- [esp8266] Don't report stale crash state after hardware WDT resets [esphome#18597](https://github.com/esphome/esphome/pull/18597) by [@bdraco](https://github.com/bdraco)
- [core] Dump the main.cpp config comment with sorted keys [esphome#18653](https://github.com/esphome/esphome/pull/18653) by [@bdraco](https://github.com/bdraco)
- [esp32] Report abort and task watchdog panics correctly in crash handler [esphome#18575](https://github.com/esphome/esphome/pull/18575) by [@bdraco](https://github.com/bdraco)
- [core] Retry transient network errors when downloading external files [esphome#18538](https://github.com/esphome/esphome/pull/18538) by [@bdraco](https://github.com/bdraco)
- [api] Fix loop stall that triggers the task watchdog when entity list sends block [esphome#18577](https://github.com/esphome/esphome/pull/18577) by [@bdraco](https://github.com/bdraco)
- [esp32_ble_tracker] Scan at the default window while a GATT connection is active [esphome#18609](https://github.com/esphome/esphome/pull/18609) by [@bdraco](https://github.com/bdraco)

