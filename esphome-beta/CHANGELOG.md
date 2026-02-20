## 2026.2.1

[**Read release announcement**](https://beta.esphome.io/changelog/2026.2.0)

- [esp32_ble_server] fix infinitely large characteristic value [esphome#14011](https://github.com/esphome/esphome/pull/14011) by [@Rapsssito](https://github.com/Rapsssito)
- [udp] Register socket consumption for CONFIG_LWIP_MAX_SOCKETS [esphome#14068](https://github.com/esphome/esphome/pull/14068) by [@bdraco](https://github.com/bdraco)
- [web_server] Double socket allocation to prevent connection exhaustion [esphome#14067](https://github.com/esphome/esphome/pull/14067) by [@bdraco](https://github.com/bdraco)
- [pulse_counter] Fix compilation on ESP32-C6/C5/H2/P4 [esphome#14070](https://github.com/esphome/esphome/pull/14070) by [@bdraco](https://github.com/bdraco)
- [web_server] Fix water_heater JSON key names and move traits to DETAIL_ALL [esphome#14064](https://github.com/esphome/esphome/pull/14064) by [@bdraco](https://github.com/bdraco)
- [ld2420] Use constexpr for compile-time constants [esphome#14079](https://github.com/esphome/esphome/pull/14079) by [@bdraco](https://github.com/bdraco)
- [e131] Fix E1.31 on ESP8266 and RP2040 by restoring WiFiUDP support [esphome#14086](https://github.com/esphome/esphome/pull/14086) by [@bdraco](https://github.com/bdraco)
- [socket] Fix IPv6 compilation error on host platform [esphome#14101](https://github.com/esphome/esphome/pull/14101) by [@swoboda1337](https://github.com/swoboda1337)
- [ethernet] Improve clk_mode deprecation warning with actionable YAML [esphome#14104](https://github.com/esphome/esphome/pull/14104) by [@swoboda1337](https://github.com/swoboda1337)
- [pulse_counter] Fix build failure when use_pcnt is false [esphome#14111](https://github.com/esphome/esphome/pull/14111) by [@swoboda1337](https://github.com/swoboda1337)
- [esp32_ble] Enable CONFIG_BT_RELEASE_IRAM on ESP32-C2 [esphome#14109](https://github.com/esphome/esphome/pull/14109) by [@bdraco](https://github.com/bdraco)
- [safe_mode] Log brownout as reset reason on OTA rollback [esphome#14113](https://github.com/esphome/esphome/pull/14113) by [@swoboda1337](https://github.com/swoboda1337)
- [wifi] Sync output_power with PHY max TX power to prevent brownout [esphome#14118](https://github.com/esphome/esphome/pull/14118) by [@swoboda1337](https://github.com/swoboda1337)
- [uart] Always call pin setup for UART0 default pins on ESP-IDF [esphome#14130](https://github.com/esphome/esphome/pull/14130) by [@bdraco](https://github.com/bdraco)
- [pulse_counter] Fix PCNT glitch filter calculation off by 1000x [esphome#14132](https://github.com/esphome/esphome/pull/14132) by [@swoboda1337](https://github.com/swoboda1337)
- [ld2450] Add frame header synchronization to readline_() [esphome#14135](https://github.com/esphome/esphome/pull/14135) by [@swoboda1337](https://github.com/swoboda1337)
- [ld2410] Add frame header synchronization to readline_() [esphome#14136](https://github.com/esphome/esphome/pull/14136) by [@swoboda1337](https://github.com/swoboda1337)
- [ld2420] Increase MAX_LINE_LENGTH to allow footer-based resync [esphome#14137](https://github.com/esphome/esphome/pull/14137) by [@swoboda1337](https://github.com/swoboda1337)
- [ld2410/ld2450] Replace header sync with buffer size increase for frame resync [esphome#14138](https://github.com/esphome/esphome/pull/14138) by [@swoboda1337](https://github.com/swoboda1337)

