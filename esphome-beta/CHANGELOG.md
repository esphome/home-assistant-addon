## 2026.3.2

[**Read release announcement**](https://beta.esphome.io/changelog/2026.3.0)

- [time] Point to valid IANA timezone list on validation failure [esphome#15110](https://github.com/esphome/esphome/pull/15110) by [@bdraco](https://github.com/bdraco)
- [wifi] Fix roaming attempt counter reset on disconnect during scan [esphome#15099](https://github.com/esphome/esphome/pull/15099) by [@bdraco](https://github.com/bdraco)
- [wifi] Reduce ESP8266 roaming scan dwell time to match ESP32 [esphome#15127](https://github.com/esphome/esphome/pull/15127) by [@bdraco](https://github.com/bdraco)
- [sx127x] Fix FIFO read corruption [esphome#15114](https://github.com/esphome/esphome/pull/15114) by [@swoboda1337](https://github.com/swoboda1337)
- [datetime] Fix state_as_esptime() returning invalid timestamp [esphome#15128](https://github.com/esphome/esphome/pull/15128) by [@bdraco](https://github.com/bdraco)
- [wifi] Fix roaming counter reset from delayed disconnect and successful retry [esphome#15126](https://github.com/esphome/esphome/pull/15126) by [@bdraco](https://github.com/bdraco)
- [wifi] Filter fast_connect by band_mode and use background scan for roaming [esphome#15152](https://github.com/esphome/esphome/pull/15152) by [@swoboda1337](https://github.com/swoboda1337)
- [uart] Fix debug callback missing peeked byte and reading past end [esphome#15169](https://github.com/esphome/esphome/pull/15169) by [@swoboda1337](https://github.com/swoboda1337)
- [sgp4x] Fix NOx index_offset default (should be 1, not 100) [esphome#15212](https://github.com/esphome/esphome/pull/15212) by [@swoboda1337](https://github.com/swoboda1337)
- [esp32_ble_server] Fix set_value action with static data lists [esphome#15285](https://github.com/esphome/esphome/pull/15285) by [@bdraco](https://github.com/bdraco)
- [esp8266] Add enable_scanf_float option [esphome#15284](https://github.com/esphome/esphome/pull/15284) by [@bdraco](https://github.com/bdraco) (new-feature)
- [thermostat] Fix stale `max_runtime_exceeded` causing spurious supplemental heating/cooling [esphome#15274](https://github.com/esphome/esphome/pull/15274) by [@kbx81](https://github.com/kbx81)
- [haier] Fix hOn half-degree temperature setting [esphome#15312](https://github.com/esphome/esphome/pull/15312) by [@swoboda1337](https://github.com/swoboda1337)
- [tormatic] Fix UART stream desync on ESP32 [esphome#15337](https://github.com/esphome/esphome/pull/15337) by [@swoboda1337](https://github.com/swoboda1337)
- [uart] fix baud rate not applied on `load_settings()` for ESP32 (IDF) [esphome#15341](https://github.com/esphome/esphome/pull/15341) by [@edwardtfn](https://github.com/edwardtfn)
- [mixer] Fix memory leak in mixer task on stop/start cycles [esphome#15185](https://github.com/esphome/esphome/pull/15185) by [@kahrendt](https://github.com/kahrendt)
- [esp32_ble_tracker] Restart BLE scan after OTA failure [esphome#15308](https://github.com/esphome/esphome/pull/15308) by [@bdraco](https://github.com/bdraco)

