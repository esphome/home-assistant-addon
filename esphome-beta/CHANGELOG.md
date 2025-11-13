## 2025.11.0b2

[**Read release announcement**](https://beta.esphome.io/changelog/2025.11.0)

- [ci] Reduce release time by removing 21 redundant ESP32-S3 IDF tests [esphome#11850](https://github.com/esphome/esphome/pull/11850) by [@bdraco](https://github.com/bdraco)
- [esp32] Update the recommended platform to 55.03.31-2 [esphome#11865](https://github.com/esphome/esphome/pull/11865) by [@swoboda1337](https://github.com/swoboda1337)
- [core] Fix wait_until hanging when used in on_boot automations [esphome#11869](https://github.com/esphome/esphome/pull/11869) by [@bdraco](https://github.com/bdraco)
- [api] Eliminate heap allocations when transmitting Event types [esphome#11773](https://github.com/esphome/esphome/pull/11773) by [@bdraco](https://github.com/bdraco)
- [esp32_ble_tracker] Use initializer_list to eliminate compiler warning and reduce flash usage [esphome#11861](https://github.com/esphome/esphome/pull/11861) by [@bdraco](https://github.com/bdraco)
- [api][event] Send events immediately to prevent loss during rapid triggers [esphome#11777](https://github.com/esphome/esphome/pull/11777) by [@bdraco](https://github.com/bdraco)
- [thermostat] Replace std::map with FixedVector, reduce flash usage [esphome#11875](https://github.com/esphome/esphome/pull/11875) by [@bdraco](https://github.com/bdraco)
- [mqtt] Fix crash with empty broker during upload/logs [esphome#11866](https://github.com/esphome/esphome/pull/11866) by [@bdraco](https://github.com/bdraco)
- [light] Fix dangling reference in compute_color_mode causing memory corruption [esphome#11868](https://github.com/esphome/esphome/pull/11868) by [@bdraco](https://github.com/bdraco)
- [wifi][ethernet] Fix spurious warnings and unclear status after PR #9823 [esphome#11871](https://github.com/esphome/esphome/pull/11871) by [@bdraco](https://github.com/bdraco)
- [wifi] Fix slow reconnection after connection loss for all network types [esphome#11873](https://github.com/esphome/esphome/pull/11873) by [@bdraco](https://github.com/bdraco)

