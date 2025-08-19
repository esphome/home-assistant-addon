## 2025.8.0b3

[**Read release announcement**](https://beta.esphome.io/changelog/2025.8.0)

- [esp32_ble] Add ``USE_ESP32_BLE_UUID`` when advertising is desired [esphome#10230](https://github.com/esphome/esphome/pull/10230) by [@jesserockz](https://github.com/jesserockz)
- Improve error reporting for add_library [esphome#10226](https://github.com/esphome/esphome/pull/10226) by [@stellar-aria](https://github.com/stellar-aria)
- [wifi] Automatically disable Enterprise WiFi support when EAP is not configured [esphome#10242](https://github.com/esphome/esphome/pull/10242) by [@bdraco](https://github.com/bdraco)
- [core] Trigger clean build when components are removed from configuration [esphome#10235](https://github.com/esphome/esphome/pull/10235) by [@bdraco](https://github.com/bdraco)
- [bluetooth_proxy] Remove redundant connection type check after V1 removal [esphome#10208](https://github.com/esphome/esphome/pull/10208) by [@bdraco](https://github.com/bdraco)
- [esp32_ble] Optimize BLE event memory usage by eliminating std::vector overhead [esphome#10247](https://github.com/esphome/esphome/pull/10247) by [@bdraco](https://github.com/bdraco)
- [web_server] fix cover_all_json_generator wrong detail [esphome#10252](https://github.com/esphome/esphome/pull/10252) by [@RFDarter](https://github.com/RFDarter)
- [esp32_ble] Store GATTC/GATTS param and small data inline to nearly eliminate heap allocations [esphome#10249](https://github.com/esphome/esphome/pull/10249) by [@bdraco](https://github.com/bdraco)
- [senseair] Discard 0 ppm readings with "Out Of Range" bit set. [esphome#10275](https://github.com/esphome/esphome/pull/10275) by [@raineth](https://github.com/raineth)
- [core] Fix post-OTA logs display when using esphome run and MQTT [esphome#10274](https://github.com/esphome/esphome/pull/10274) by [@raineth](https://github.com/raineth)
- [core] Fix scheduler race condition where cancelled items still execute [esphome#10268](https://github.com/esphome/esphome/pull/10268) by [@bdraco](https://github.com/bdraco)
- [esp32] Write variant to sdkconfig file [esphome#10267](https://github.com/esphome/esphome/pull/10267) by [@jesserockz](https://github.com/jesserockz)
- [nextion] Don't include terminating NUL in nextion text_sensor states [esphome#10273](https://github.com/esphome/esphome/pull/10273) by [@raineth](https://github.com/raineth)

