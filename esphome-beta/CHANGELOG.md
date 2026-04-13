## 2026.4.0b2

[**Read release announcement**](https://beta.esphome.io/changelog/2026.4.0)

- [api] Fix ListEntitiesRequest not read due to LWIP rcvevent tracking [esphome#15589](https://github.com/esphome/esphome/pull/15589) by [@bdraco](https://github.com/bdraco)
- Bump aioesphomeapi from 44.12.0 to 44.13.1 [esphome#15600](https://github.com/esphome/esphome/pull/15600) by [@dependabot[bot]](https://github.com/apps/dependabot)
- [gdk101] Increase reset retries for slow-booting sensor MCU [esphome#15584](https://github.com/esphome/esphome/pull/15584) by [@bdraco](https://github.com/bdraco)
- [sx127x][cc1101] Disable loop when packet mode is inactive [esphome#15606](https://github.com/esphome/esphome/pull/15606) by [@swoboda1337](https://github.com/swoboda1337)
- [hbridge] Move light pin switching to loop [esphome#15615](https://github.com/esphome/esphome/pull/15615) by [@jesserockz](https://github.com/jesserockz)
- [tca9555] Add interrupt pin support [esphome#15613](https://github.com/esphome/esphome/pull/15613) by [@bdraco](https://github.com/bdraco) (new-feature)
- [pca6416a] Add interrupt pin support [esphome#15614](https://github.com/esphome/esphome/pull/15614) by [@bdraco](https://github.com/bdraco) (new-feature)
- [mcp23016] Add interrupt pin support [esphome#15616](https://github.com/esphome/esphome/pull/15616) by [@bdraco](https://github.com/bdraco) (new-feature)
- [api] Add (inline_encode) proto option for sub-message inlining [esphome#15599](https://github.com/esphome/esphome/pull/15599) by [@bdraco](https://github.com/bdraco)
- [micro_wake_word] Pin esp-nn version [esphome#15628](https://github.com/esphome/esphome/pull/15628) by [@kahrendt](https://github.com/kahrendt)
- [sx127x][cc1101][sx126x] Use GPIO interrupt to wake loop [esphome#15627](https://github.com/esphome/esphome/pull/15627) by [@swoboda1337](https://github.com/swoboda1337)
- [rp2040] Fix W5500 Ethernet pbuf corruption by mirroring LWIPMutex semantics [esphome#15624](https://github.com/esphome/esphome/pull/15624) by [@bdraco](https://github.com/bdraco)
- Bump aioesphomeapi from 44.13.1 to 44.13.2 [esphome#15637](https://github.com/esphome/esphome/pull/15637) by [@dependabot[bot]](https://github.com/apps/dependabot)
- Bump aioesphomeapi from 44.13.2 to 44.13.3 [esphome#15641](https://github.com/esphome/esphome/pull/15641) by [@dependabot[bot]](https://github.com/apps/dependabot)
- [mdns] Bump espressif/mdns to 1.11.0 [esphome#15670](https://github.com/esphome/esphome/pull/15670) by [@swoboda1337](https://github.com/swoboda1337)
- [canbus] Fix canbus.send can_id compile error [esphome#15668](https://github.com/esphome/esphome/pull/15668) by [@swoboda1337](https://github.com/swoboda1337)
- [esp32] Bump platform to 55.03.38, Arduino to 3.3.8, ESP-IDF to 5.5.4 [esphome#15666](https://github.com/esphome/esphome/pull/15666) by [@swoboda1337](https://github.com/swoboda1337)
- [packages] Fix false deprecation warning and wrong error paths in nested packages [esphome#15605](https://github.com/esphome/esphome/pull/15605) by [@bdraco](https://github.com/bdraco) (breaking-change)
- [lvgl] Fix use of rotation on host SDL [esphome#15611](https://github.com/esphome/esphome/pull/15611) by [@clydebarrow](https://github.com/clydebarrow)

