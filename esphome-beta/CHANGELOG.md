## 2026.1.1

[**Read release announcement**](https://beta.esphome.io/changelog/2026.1.0)

- [wifi] Process scan results one at a time to avoid heap allocation [esphome#13400](https://github.com/esphome/esphome/pull/13400) by [@bdraco](https://github.com/bdraco)
- [lvgl] Validate LVGL dropdown symbols require Unicode codepoint ≥ 0x100 [esphome#13394](https://github.com/esphome/esphome/pull/13394) by [@Copilot](https://github.com/apps/copilot-swe-agent)
- [http_request] Fix verify_ssl: false not working on ESP32 [esphome#13422](https://github.com/esphome/esphome/pull/13422) by [@swoboda1337](https://github.com/swoboda1337)
- [esp32] Add warning for experimental 400MHz on ESP32-P4 [esphome#13433](https://github.com/esphome/esphome/pull/13433) by [@swoboda1337](https://github.com/swoboda1337)
- [wifi] Fix bk72xx manual_ip preventing API connection [esphome#13426](https://github.com/esphome/esphome/pull/13426) by [@bdraco](https://github.com/bdraco)
- [spi] Fix display init failure by marking displays as write-only for half-duplex mode [esphome#13431](https://github.com/esphome/esphome/pull/13431) by [@bdraco](https://github.com/bdraco)
- [http_request] Fix OTA failures on ESP8266/Arduino by making read semantics consistent [esphome#13435](https://github.com/esphome/esphome/pull/13435) by [@bdraco](https://github.com/bdraco)
- [dht] Increase delay for DHT22 and RHT03 [esphome#13446](https://github.com/esphome/esphome/pull/13446) by [@rguca](https://github.com/rguca)
- [api] Limit Nagle batching for log messages to reduce LWIP buffer pressure [esphome#13439](https://github.com/esphome/esphome/pull/13439) by [@bdraco](https://github.com/bdraco)
- [wifi] Fix stale error_from_callback_ causing immediate connection failures [esphome#13450](https://github.com/esphome/esphome/pull/13450) by [@bdraco](https://github.com/bdraco)
- [fingerprint_grow] Use buffer-based dump_summary to fix deprecation warnings [esphome#13447](https://github.com/esphome/esphome/pull/13447) by [@swoboda1337](https://github.com/swoboda1337)
- [aqi] Remove unit_of_measurement to fix Home Assistant warning [esphome#13448](https://github.com/esphome/esphome/pull/13448) by [@swoboda1337](https://github.com/swoboda1337)
- [time] Always call time sync callbacks even when time unchanged [esphome#13456](https://github.com/esphome/esphome/pull/13456) by [@bdraco](https://github.com/bdraco)

