## 2026.11.0b4

[**Read release announcement**](https://beta.esphome.io/changelog/2026.11.0)

- [sendspin] Add bits_per_sample to the media source [esphome#22313](https://github.com/esphome/esphome/pull/22313) by [@kahrendt](https://github.com/kahrendt) (new-feature)
- [core] Inline InterruptLock on ESP8266 [esphome#22455](https://github.com/esphome/esphome/pull/22455) by [@bdraco](https://github.com/bdraco)
- [esp32_ble_server] Size the BLE2902 value buffer to its 2 byte value [esphome#22454](https://github.com/esphome/esphome/pull/22454) by [@bdraco](https://github.com/bdraco)
- [ota] Skip the auth request when the password is empty at run time [esphome#22485](https://github.com/esphome/esphome/pull/22485) by [@swoboda1337](https://github.com/swoboda1337)
- [dsmr] Update dsmr_parser to 1.11.0 [esphome#22530](https://github.com/esphome/esphome/pull/22530) by [@PolarGoose](https://github.com/PolarGoose)
- [esp8266] Skip other devices' known mDNS answers without allocating (Arduino core 3.1.2-esphome.4) [esphome#22533](https://github.com/esphome/esphome/pull/22533) by [@bdraco](https://github.com/bdraco)
- [mipi_dsi] Keep the panel running while flash is written [esphome#22535](https://github.com/esphome/esphome/pull/22535) by [@clydebarrow](https://github.com/clydebarrow)
- [espectre] Update to SDK 3.2.0 [esphome#22570](https://github.com/esphome/esphome/pull/22570) by [@francescopace](https://github.com/francescopace)
- [esp32_ble][ble_device_base][improv_ble] Send advertising as raw packets and keep Improv in the advertising packet [esphome#22499](https://github.com/esphome/esphome/pull/22499) by [@bdraco](https://github.com/bdraco)
- [wifi] Apply power save when the AP starts without networks [esphome#22564](https://github.com/esphome/esphome/pull/22564) by [@bdraco](https://github.com/bdraco)
- [uart] Lock interrupts per bit in ESP8266 software serial TX at 19200 baud and below [esphome#22450](https://github.com/esphome/esphome/pull/22450) by [@bdraco](https://github.com/bdraco)
- [zigbee] Rejoin only after the parent missed several polls [esphome#22405](https://github.com/esphome/esphome/pull/22405) by [@jabla](https://github.com/jabla)
- [remote_transmitter] Lock interrupts only near each edge on ESP8266 [esphome#22453](https://github.com/esphome/esphome/pull/22453) by [@bdraco](https://github.com/bdraco)
- [esp32_ble_tracker] Scan at the short window while the wifi AP is running [esphome#22566](https://github.com/esphome/esphome/pull/22566) by [@bdraco](https://github.com/bdraco)
- [esp32_ble] Keep bond keys when a bonded device re-encrypts on ESP-IDF 5.5.6 [esphome#22559](https://github.com/esphome/esphome/pull/22559) by [@bdraco](https://github.com/bdraco)
- [gpio] Lock interrupts per slot on the one_wire bus [esphome#22452](https://github.com/esphome/esphome/pull/22452) by [@bdraco](https://github.com/bdraco)
- [esp32_ble] Sort GATT discovery responses by handle for ESP-IDF 5.5.6 and 6.0.3 [esphome#22576](https://github.com/esphome/esphome/pull/22576) by [@bdraco](https://github.com/bdraco)

