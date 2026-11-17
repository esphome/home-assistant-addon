## 2026.11.0b6

[**Read release announcement**](https://beta.esphome.io/changelog/2026.11.0)

- [api] Make the event order backpressure test wait until the pipe is full [esphome#22112](https://github.com/esphome/esphome/pull/22112) by [@bdraco](https://github.com/bdraco)
- [i2c] Refuse RP2040 writes larger than the Wire buffer instead of leaving the bus stuck [esphome#22791](https://github.com/esphome/esphome/pull/22791) by [@bdraco](https://github.com/bdraco)
- [esp32_ble] Replace Bluedroid's sscanf callers on ESP-IDF 6 too [esphome#22805](https://github.com/esphome/esphome/pull/22805) by [@swoboda1337](https://github.com/swoboda1337)
- [esp32_ble] Apply the Bluedroid workarounds to the ESP-IDF 6.1 releases that need them [esphome#22806](https://github.com/esphome/esphome/pull/22806) by [@swoboda1337](https://github.com/swoboda1337)
- [wifi] Clear the error flag when the adapter restart is skipped [esphome#22797](https://github.com/esphome/esphome/pull/22797) by [@adamsthws](https://github.com/adamsthws)
- [zephyr] Count micros() in microseconds and busy-wait in delayMicroseconds() [esphome#22612](https://github.com/esphome/esphome/pull/22612) by [@bdraco](https://github.com/bdraco)
- [api] Send queued entity states before DisconnectRequest on shutdown [esphome#22625](https://github.com/esphome/esphome/pull/22625) by [@bdraco](https://github.com/bdraco)
- [uart] Stop ESP8266 software serial TX from tripping the Wi-Fi watchdog at 57600 baud [esphome#22641](https://github.com/esphome/esphome/pull/22641) by [@bdraco](https://github.com/bdraco)
- [esp32_power_management] Clamp the tick step after light sleep so it cannot trip vTaskStepTick [esphome#22637](https://github.com/esphome/esphome/pull/22637) by [@bdraco](https://github.com/bdraco)
- [esp32_ble] Stop Bluedroid re-running a failed queued MTU or execute write request [esphome#22670](https://github.com/esphome/esphome/pull/22670) by [@bdraco](https://github.com/bdraco)
- [core] Release only the lwIP core lock a LwIPLock took [esphome#22683](https://github.com/esphome/esphome/pull/22683) by [@bdraco](https://github.com/bdraco)
- [esp32][libretiny] Make delay() wait at least the requested time [esphome#22822](https://github.com/esphome/esphome/pull/22822) by [@swoboda1337](https://github.com/swoboda1337)
- [wifi] Join the next network after a failed hidden network probe on ESP32 [esphome#22764](https://github.com/esphome/esphome/pull/22764) by [@bdraco](https://github.com/bdraco)
- [modem] Set the APN while the SIM is powered down [esphome#22817](https://github.com/esphome/esphome/pull/22817) by [@bdraco](https://github.com/bdraco)

