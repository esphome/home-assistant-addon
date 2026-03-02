## 2026.2.3

[**Read release announcement**](https://beta.esphome.io/changelog/2026.2.0)

- [mqtt] Remove broken ESP8266 ssl_fingerprints option [esphome#14182](https://github.com/esphome/esphome/pull/14182) by [@bdraco](https://github.com/bdraco) (breaking-change)
- [sprinkler] Fix millis overflow and underflow bugs [esphome#14299](https://github.com/esphome/esphome/pull/14299) by [@swoboda1337](https://github.com/swoboda1337)
- [cc1101] Transition through IDLE in begin_tx/begin_rx for reliable state changes [esphome#14321](https://github.com/esphome/esphome/pull/14321) by [@swoboda1337](https://github.com/swoboda1337)
- [zigbee] Fix codegen ordering for basic/identify attribute lists [esphome#14343](https://github.com/esphome/esphome/pull/14343) by [@swoboda1337](https://github.com/swoboda1337)
- [uart] Revert UART0 default pin workarounds (fixed in ESP-IDF 5.5.2) [esphome#14363](https://github.com/esphome/esphome/pull/14363) by [@bdraco](https://github.com/bdraco)
- [mipi_dsi] Fix Waveshare P4 7B board config [esphome#14372](https://github.com/esphome/esphome/pull/14372) by [@clydebarrow](https://github.com/clydebarrow)
- [core] Defer entity automation codegen to prevent sibling ID deadlocks [esphome#14381](https://github.com/esphome/esphome/pull/14381) by [@swoboda1337](https://github.com/swoboda1337)
- [improv_serial] Add missing USE_IMPROV_SERIAL define to fix WiFi scan filtering [esphome#14359](https://github.com/esphome/esphome/pull/14359) by [@bdraco](https://github.com/bdraco)
- [uart] Fix flow_control_pin inverted flag ignored on ESP-IDF [esphome#14410](https://github.com/esphome/esphome/pull/14410) by [@swoboda1337](https://github.com/swoboda1337)

