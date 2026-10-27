## 2026.10.1

[**Read release announcement**](https://esphome.io/changelog/2026.10.0)

- [esp32_hosted] Keep the OTA watchdog timeout through the coprocessor end call [esphome#21300](https://github.com/esphome/esphome/pull/21300) by [@swoboda1337](https://github.com/swoboda1337)
- [core] Emit generated lambda code after the user includes [esphome#21307](https://github.com/esphome/esphome/pull/21307) by [@bdraco](https://github.com/bdraco)
- [light] Add a StringRef overload for LightCall::set_effect [esphome#21358](https://github.com/esphome/esphome/pull/21358) by [@bdraco](https://github.com/bdraco)
- [mqtt] Resend the fan state when its first publish fails [esphome#21328](https://github.com/esphome/esphome/pull/21328) by [@bdraco](https://github.com/bdraco)
- [http_request] Copy a manifest URL set at run time and keep the config literal by pointer [esphome#21373](https://github.com/esphome/esphome/pull/21373) by [@bdraco](https://github.com/bdraco)
- [climate] Add StringRef overloads for ClimateCall::set_fan_mode and set_preset [esphome#21359](https://github.com/esphome/esphome/pull/21359) by [@bdraco](https://github.com/bdraco)
- [core] Keep the color codes of a filtered build output line [esphome#21396](https://github.com/esphome/esphome/pull/21396) by [@swoboda1337](https://github.com/swoboda1337)
- [ledc] Reset the peripheral through the HAL on targets without the legacy periph API [esphome#21397](https://github.com/esphome/esphome/pull/21397) by [@swoboda1337](https://github.com/swoboda1337)
- [core] Resolve version-less library dependencies like PlatformIO [esphome#21317](https://github.com/esphome/esphome/pull/21317) by [@bdraco](https://github.com/bdraco)
- [esp32_ble] Ignore unhandled BLE key GAP events [esphome#21457](https://github.com/esphome/esphome/pull/21457) by [@minimicro34](https://github.com/minimicro34)
- [core] Generate valid C++ for infinite float values [esphome#21625](https://github.com/esphome/esphome/pull/21625) by [@swoboda1337](https://github.com/swoboda1337)
- [core] Avoid division by zero in Color::random_color() [esphome#21623](https://github.com/esphome/esphome/pull/21623) by [@swoboda1337](https://github.com/swoboda1337)
- [core] Turn off the precompiled header with ccache older than 4.7 [esphome#21627](https://github.com/esphome/esphome/pull/21627) by [@bdraco](https://github.com/bdraco)
- [ci] Stop saving an empty apt cache when the install fails [esphome#21713](https://github.com/esphome/esphome/pull/21713) by [@bdraco](https://github.com/bdraco)

