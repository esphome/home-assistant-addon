## 2025.11.0b3

[**Read release announcement**](https://beta.esphome.io/changelog/2025.11.0)

- [esp32] Make esp-idf default framework for P4 [esphome#11884](https://github.com/esphome/esphome/pull/11884) by [@clydebarrow](https://github.com/clydebarrow)
- [esp32] Add sdkconfig flag to make OTA work for 32MB flash [esphome#11883](https://github.com/esphome/esphome/pull/11883) by [@clydebarrow](https://github.com/clydebarrow)
- [light] Fix missing `ColorMode::BRIGHTNESS` case in logging [esphome#11836](https://github.com/esphome/esphome/pull/11836) by [@edwardtfn](https://github.com/edwardtfn)
- [wifi] Allow `use_psram` with Arduino [esphome#11902](https://github.com/esphome/esphome/pull/11902) by [@edwardtfn](https://github.com/edwardtfn)
- [uart] Improve error handling and validate buffer size [esphome#11895](https://github.com/esphome/esphome/pull/11895) by [@swoboda1337](https://github.com/swoboda1337)
- [ld2412] Fix stuck targets by adding timeout filter [esphome#11919](https://github.com/esphome/esphome/pull/11919) by [@bdraco](https://github.com/bdraco)
- [ld2410] Add timeout filter to prevent stuck targets [esphome#11920](https://github.com/esphome/esphome/pull/11920) by [@bdraco](https://github.com/bdraco)
- [scheduler] Fix timing breakage after 49 days of uptime on ESP8266/RP2040 [esphome#11924](https://github.com/esphome/esphome/pull/11924) by [@bdraco](https://github.com/bdraco)
- [analyze-memory] Show all core symbols > 100 B instead of top 15 [esphome#11909](https://github.com/esphome/esphome/pull/11909) by [@bdraco](https://github.com/bdraco)
- [sntp] Merge multiple instances to fix crash and undefined behavior [esphome#11904](https://github.com/esphome/esphome/pull/11904) by [@bdraco](https://github.com/bdraco)
- [web_server.ota] Merge multiple instances to prevent undefined behavior [esphome#11905](https://github.com/esphome/esphome/pull/11905) by [@bdraco](https://github.com/bdraco)
- [web_server_idf] Fix lwIP assertion crash by shutting down sockets on connection close [esphome#11937](https://github.com/esphome/esphome/pull/11937) by [@bdraco](https://github.com/bdraco)
- [uart] Setup uart pins only if flags are set [esphome#11914](https://github.com/esphome/esphome/pull/11914) by [@asergunov](https://github.com/asergunov)

