## 2026.11.1

[**Read release announcement**](https://beta.esphome.io/changelog/2026.11.0)

- [esp32] Replace arduino-esp32's libsodium through the manifest overrides field [esphome#22799](https://github.com/esphome/esphome/pull/22799) by [@swoboda1337](https://github.com/swoboda1337)
- [wireguard][sendspin] Keep one libsodium when both are in a build [esphome#22897](https://github.com/esphome/esphome/pull/22897) by [@swoboda1337](https://github.com/swoboda1337)
- [esp32_hosted] Raise the watchdog around the coprocessor version request [esphome#22907](https://github.com/esphome/esphome/pull/22907) by [@swoboda1337](https://github.com/swoboda1337)
- [esp32_hosted] Fix the SDIO stall with coprocessor firmware older than 2.12.0 [esphome#22906](https://github.com/esphome/esphome/pull/22906) by [@swoboda1337](https://github.com/swoboda1337)
- [esp32_hosted] Warn about the ESP32-C5 partition table offset on coprocessor updates [esphome#22918](https://github.com/esphome/esphome/pull/22918) by [@swoboda1337](https://github.com/swoboda1337)
- [logger] Respect the global level when defaulting boot_log_level [esphome#22786](https://github.com/esphome/esphome/pull/22786) by [@labodj](https://github.com/labodj)
- [http_request] Extend the watchdog for the TLS handshake on ESP-IDF [esphome#23047](https://github.com/esphome/esphome/pull/23047) by [@bdraco](https://github.com/bdraco)
- [esp8266] Keep interrupts enabled while saving preferences to flash [esphome#23221](https://github.com/esphome/esphome/pull/23221) by [@bdraco](https://github.com/bdraco)
- [voice_assistant] Finish a response stopped before playback starts [esphome#22848](https://github.com/esphome/esphome/pull/22848) by [@maxi1134](https://github.com/maxi1134)
- [ota] Reject an ESP8266 web upload that lost bytes instead of flashing it [esphome#23225](https://github.com/esphome/esphome/pull/23225) by [@bdraco](https://github.com/bdraco)
- [image] Draw pixel by pixel with plain RGB colors [esphome#23229](https://github.com/esphome/esphome/pull/23229) by [@clydebarrow](https://github.com/clydebarrow)
- [modem] Power the SIM back up with CFUN=1 when the APN can't be set at CFUN=0 [esphome#23238](https://github.com/esphome/esphome/pull/23238) by [@randybb](https://github.com/randybb)
- [display] Use RGB luma for 4-bit grayscale [esphome#23226](https://github.com/esphome/esphome/pull/23226) by [@clydebarrow](https://github.com/clydebarrow)

