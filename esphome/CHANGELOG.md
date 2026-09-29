## 2026.9.1

[**Read release announcement**](https://esphome.io/changelog/2026.9.0)

- [mipi_dsi] Let IDF pick the DPHY PLL reference clock [esphome#18984](https://github.com/esphome/esphome/pull/18984) by [@elwinloomis](https://github.com/elwinloomis)
- [ota] Skip the web_server plaintext warning when web_server ota is disabled [esphome#19348](https://github.com/esphome/esphome/pull/19348) by [@bdraco](https://github.com/bdraco)
- [mixer] Don't discard a start request while reaping a stopped task [esphome#19368](https://github.com/esphome/esphome/pull/19368) by [@rexmoriarty](https://github.com/rexmoriarty)
- [esp32][rp2] Print the previous boot crash report before the logger reads it [esphome#19351](https://github.com/esphome/esphome/pull/19351) by [@bdraco](https://github.com/bdraco)
- [espidf] Switch the Windows console to UTF-8 while idf.py runs [esphome#19352](https://github.com/esphome/esphome/pull/19352) by [@bdraco](https://github.com/bdraco)
- [esp32_hosted] Fix ESP32-P4 build without wifi, espnow or BLE [esphome#19374](https://github.com/esphome/esphome/pull/19374) by [@bdraco](https://github.com/bdraco)
- [esphome] Keep the OTA encryption key without the api server so safe mode uploads work [esphome#19349](https://github.com/esphome/esphome/pull/19349) by [@bdraco](https://github.com/bdraco)
- [esp32] Disable newlib nano printf formatting on ESP32-C2 [esphome#19418](https://github.com/esphome/esphome/pull/19418) by [@swoboda1337](https://github.com/swoboda1337)
- [web_server] Mask the value of a password text entity, not only its state [esphome#19385](https://github.com/esphome/esphome/pull/19385) by [@bdraco](https://github.com/bdraco)
- [nrf52] set WDT timeout to 30sec for Adafruit bootloader [esphome#19596](https://github.com/esphome/esphome/pull/19596) by [@tomaszduda23](https://github.com/tomaszduda23)
- [mipi_spi] Fix reversion in dc/cs sequence for spi_16 [esphome#19745](https://github.com/esphome/esphome/pull/19745) by [@clydebarrow](https://github.com/clydebarrow)
- [lvgl] Honor esphome build_flags when generating lv_conf.h [esphome#19743](https://github.com/esphome/esphome/pull/19743) by [@SulimanAbdulrazzaq](https://github.com/SulimanAbdulrazzaq)
- [ethernet] Move received frames to PSRAM on SPI ethernet chips [esphome#19377](https://github.com/esphome/esphome/pull/19377) by [@bdraco](https://github.com/bdraco)

