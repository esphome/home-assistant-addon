## 2025.8.1

[**Read release announcement**](https://esphome.io/changelog/2025.8.0)

- [api] Add zero-copy StringRef methods for compilation_time and effect_name [esphome#10257](https://github.com/esphome/esphome/pull/10257) by [@bdraco](https://github.com/bdraco)
- [esp32_ble_client] Add log helper functions to reduce flash usage by 120 bytes [esphome#10243](https://github.com/esphome/esphome/pull/10243) by [@bdraco](https://github.com/bdraco)
- [api] Add ``USE_API_HOMEASSISTANT_SERVICES`` if using ``tag_scanned`` action [esphome#10316](https://github.com/esphome/esphome/pull/10316) by [@jesserockz](https://github.com/jesserockz)
- [http_request] Fix for host after ArduinoJson library bump [esphome#10348](https://github.com/esphome/esphome/pull/10348) by [@clydebarrow](https://github.com/clydebarrow)
- [core] Improve error reporting for entity name conflicts with non-ASCII characters [esphome#10329](https://github.com/esphome/esphome/pull/10329) by [@bdraco](https://github.com/bdraco)
- [pvvx_mithermometer] Fix race condition with BLE authentication [esphome#10327](https://github.com/esphome/esphome/pull/10327) by [@bdraco](https://github.com/bdraco)
- [esp32_ble_client] Optimize BLE connection parameters for different connection types [esphome#10356](https://github.com/esphome/esphome/pull/10356) by [@bdraco](https://github.com/bdraco)
- [esp32_ble] Increase GATT connection retry count to use full timeout window [esphome#10376](https://github.com/esphome/esphome/pull/10376) by [@bdraco](https://github.com/bdraco)
- [script] Fix parallel mode scripts with delays cancelling each other [esphome#10324](https://github.com/esphome/esphome/pull/10324) by [@bdraco](https://github.com/bdraco)
- [deep_sleep] Fix ESP32-C6 compilation error with gpio_deep_sleep_hold_en() [esphome#10345](https://github.com/esphome/esphome/pull/10345) by [@bdraco](https://github.com/bdraco)
- [esp32_ble_client] Reduce log level for harmless BLE timeout race conditions [esphome#10339](https://github.com/esphome/esphome/pull/10339) by [@bdraco](https://github.com/bdraco)
- [lvgl] Fix meter rotation [esphome#10342](https://github.com/esphome/esphome/pull/10342) by [@clydebarrow](https://github.com/clydebarrow)
- [esp32_ble_tracker] Fix on_scan_end trigger compilation without USE_ESP32_BLE_DEVICE [esphome#10399](https://github.com/esphome/esphome/pull/10399) by [@bdraco](https://github.com/bdraco)
- [test] Add integration test for light effect memory corruption fix [esphome#10417](https://github.com/esphome/esphome/pull/10417) by [@bdraco](https://github.com/bdraco)
- [web_server] Use oi.esphome.io for css and js assets [esphome#10296](https://github.com/esphome/esphome/pull/10296) by [@clydebarrow](https://github.com/clydebarrow)

