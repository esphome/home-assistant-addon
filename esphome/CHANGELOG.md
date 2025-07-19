## 2025.7.2

[**Read release announcement**](https://esphome.io/changelog/2025.7.0)

- Fix template event web_server crash [esphome#9618](https://github.com/esphome/esphome/pull/9618) by [@AzonInc](https://github.com/AzonInc)
- [api] Fix compilation error with char* lambdas in HomeAssistant services [esphome#9638](https://github.com/esphome/esphome/pull/9638) by [@bdraco](https://github.com/bdraco)
- [wireguard] Fix boot loop when CONFIG_LWIP_TCPIP_CORE_LOCKING is enabled [esphome#9637](https://github.com/esphome/esphome/pull/9637) by [@bdraco](https://github.com/bdraco)
- [scheduler] Fix cancellation of timers with empty string names [esphome#9641](https://github.com/esphome/esphome/pull/9641) by [@bdraco](https://github.com/bdraco)
- [logger] fix on_message [esphome#9642](https://github.com/esphome/esphome/pull/9642) by [@ssieb](https://github.com/ssieb)
- esp32_camera: deprecate i2c_pins; throw error if combined with i2c: block [esphome#9615](https://github.com/esphome/esphome/pull/9615) by [@RubenKelevra](https://github.com/RubenKelevra)
- [scheduler] Fix DelayAction cancellation in restart mode scripts [esphome#9646](https://github.com/esphome/esphome/pull/9646) by [@bdraco](https://github.com/bdraco)
- [lvgl] Fix meter rotation [esphome#9605](https://github.com/esphome/esphome/pull/9605) by [@clydebarrow](https://github.com/clydebarrow)
- [libretiny] Remove unsupported lock-free queue and event pool implementations [esphome#9653](https://github.com/esphome/esphome/pull/9653) by [@bdraco](https://github.com/bdraco)
- [lvgl] Prevent keyerror on min/max value widgets with no default [esphome#9660](https://github.com/esphome/esphome/pull/9660) by [@jesserockz](https://github.com/jesserockz)
- Fix AsyncTCP version mismatch between platformio.ini and async_tcp component [esphome#9676](https://github.com/esphome/esphome/pull/9676) by [@bdraco](https://github.com/bdraco)
- [speaker] Media player's pipeline properly returns playing state near end of file [esphome#9668](https://github.com/esphome/esphome/pull/9668) by [@kahrendt](https://github.com/kahrendt)
- [voice_assistant] Use media player callbacks to track TTS response status [esphome#9670](https://github.com/esphome/esphome/pull/9670) by [@kahrendt](https://github.com/kahrendt)
- [gpio] Disable interrupt mode by default for LibreTiny platforms [esphome#9687](https://github.com/esphome/esphome/pull/9687) by [@bdraco](https://github.com/bdraco)

