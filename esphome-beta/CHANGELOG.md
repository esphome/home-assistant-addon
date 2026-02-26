## 2026.2.2

[**Read release announcement**](https://beta.esphome.io/changelog/2026.2.0)

- [max7219digit] Fix typo in action names [esphome#14162](https://github.com/esphome/esphome/pull/14162) by [@swoboda1337](https://github.com/swoboda1337)
- [mipi_dsi] Disallow swap_xy [esphome#14124](https://github.com/esphome/esphome/pull/14124) by [@clydebarrow](https://github.com/clydebarrow)
- [dsmr] Add deprecated std::string overload for set_decryption_key [esphome#14180](https://github.com/esphome/esphome/pull/14180) by [@bdraco](https://github.com/bdraco)
- [api] Fix build error when lambda returns StringRef in homeassistant.event data [esphome#14187](https://github.com/esphome/esphome/pull/14187) by [@bdraco](https://github.com/bdraco)
- [haier] Fix uninitialized HonSettings causing API connection failures [esphome#14188](https://github.com/esphome/esphome/pull/14188) by [@bdraco](https://github.com/bdraco)
- [bme68x_bsec2] Fix compilation on ESP32 Arduino [esphome#14194](https://github.com/esphome/esphome/pull/14194) by [@bdraco](https://github.com/bdraco)
- [network] Improve IPAddress::str() deprecation warning with usage example [esphome#14195](https://github.com/esphome/esphome/pull/14195) by [@bdraco](https://github.com/bdraco)
- [water_heater] Fix device_id missing from state responses [esphome#14212](https://github.com/esphome/esphome/pull/14212) by [@bdraco](https://github.com/bdraco)
- [mipi_dsi] Allow transform disable; fix warnings [esphome#14216](https://github.com/esphome/esphome/pull/14216) by [@clydebarrow](https://github.com/clydebarrow) (new-feature)
- [http_request.ota] Percent-encode credentials in URL [esphome#14257](https://github.com/esphome/esphome/pull/14257) by [@swoboda1337](https://github.com/swoboda1337)
- Don't get stuck forever on a failed component can_proceed [esphome#14267](https://github.com/esphome/esphome/pull/14267) by [@jesserockz](https://github.com/jesserockz)
- [pid] Fix deadband threshold conversion for Fahrenheit [esphome#14268](https://github.com/esphome/esphome/pull/14268) by [@swoboda1337](https://github.com/swoboda1337)
- [ld2420] Fix sizeof vs value bug in register memcpy [esphome#14286](https://github.com/esphome/esphome/pull/14286) by [@swoboda1337](https://github.com/swoboda1337)
- [rtttl] Fix speaker playback bugs [esphome#14280](https://github.com/esphome/esphome/pull/14280) by [@swoboda1337](https://github.com/swoboda1337)
- [hmc5883l] Fix wrong gain for 88uT range [esphome#14281](https://github.com/esphome/esphome/pull/14281) by [@swoboda1337](https://github.com/swoboda1337)
- [sensor] Fix delta filter percentage mode regression [esphome#14302](https://github.com/esphome/esphome/pull/14302) by [@swoboda1337](https://github.com/swoboda1337)

