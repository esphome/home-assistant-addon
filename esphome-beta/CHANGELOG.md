## 2026.9.0b5

[**Read release announcement**](https://beta.esphome.io/changelog/2026.9.0)

- [pmsa003i] Fix read from uninitialized stack memory [esphome#19053](https://github.com/esphome/esphome/pull/19053) by [@j9brown](https://github.com/j9brown)
- [template] Stop water heater republishing when a temperature is unknown [esphome#19013](https://github.com/esphome/esphome/pull/19013) by [@tronikos](https://github.com/tronikos)
- [core] Mark filters, manual_ip and interlock as advanced [esphome#19272](https://github.com/esphome/esphome/pull/19272) by [@jesserockz](https://github.com/jesserockz)
- [number] Fix the default mode check so mode auto is no longer emitted [esphome#19231](https://github.com/esphome/esphome/pull/19231) by [@bdraco](https://github.com/bdraco)
- [web_server] Skip setters that pass the default port, log and include internal values [esphome#19226](https://github.com/esphome/esphome/pull/19226) by [@bdraco](https://github.com/bdraco)
- [output] Skip the power limit setters when they match the defaults [esphome#19225](https://github.com/esphome/esphome/pull/19225) by [@bdraco](https://github.com/bdraco)
- [light] Skip the flash transition setter and the empty effect list [esphome#19228](https://github.com/esphome/esphome/pull/19228) by [@bdraco](https://github.com/bdraco)
- [wifi] Skip setters that pass the default priority, timeouts, power save and auth mode [esphome#19229](https://github.com/esphome/esphome/pull/19229) by [@bdraco](https://github.com/bdraco)
- [logger] Skip the hardware UART setter when it matches the default [esphome#19230](https://github.com/esphome/esphome/pull/19230) by [@bdraco](https://github.com/bdraco)
- [esp8266_pwm] Skip the frequency setter when it matches the default [esphome#19224](https://github.com/esphome/esphome/pull/19224) by [@bdraco](https://github.com/bdraco)
- [bk72xx_ble] Keep wifi power save off while BLE is compiled in [esphome#19317](https://github.com/esphome/esphome/pull/19317) by [@Bl00d-B0b](https://github.com/Bl00d-B0b)
- [modbus] Add allow_broadcast_read and expect_broadcast_write_response options [esphome#19304](https://github.com/esphome/esphome/pull/19304) by [@exciton](https://github.com/exciton) (new-feature)
- [file] Keep resolved image paths as Path so config-hash normalizes them [esphome#19267](https://github.com/esphome/esphome/pull/19267) by [@cpruijsen](https://github.com/cpruijsen)

