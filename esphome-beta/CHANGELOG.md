## 2026.11.0b7

[**Read release announcement**](https://beta.esphome.io/changelog/2026.11.0)

- [api] Make the event order backpressure test wait until the pipe is full [esphome#22112](https://github.com/esphome/esphome/pull/22112) by [@bdraco](https://github.com/bdraco)
- [mlx90393] Enable the Wire library on ESP32 Arduino [esphome#22801](https://github.com/esphome/esphome/pull/22801) by [@swoboda1337](https://github.com/swoboda1337)
- [climate] Don't fail on a platform entry that only holds nested climates [esphome#22844](https://github.com/esphome/esphome/pull/22844) by [@dwmw2](https://github.com/dwmw2)
- [logger] Qualify the host clock function [esphome#22838](https://github.com/esphome/esphome/pull/22838) by [@labodj](https://github.com/labodj)
- [cst816] Ignore idle 0xFF touch frames and invalid coordinates [esphome#22435](https://github.com/esphome/esphome/pull/22435) by [@Mattheinrichs](https://github.com/Mattheinrichs)
- [mqtt] Don't start the broker lookup before the network is up [esphome#22843](https://github.com/esphome/esphome/pull/22843) by [@dwmw2](https://github.com/dwmw2)
- [scd30] Stop overriding the I2C bus clock-stretch limit on ESP8266 [esphome#22512](https://github.com/esphome/esphome/pull/22512) by [@bdraco](https://github.com/bdraco)
- [modem] Wait for registration before attaching and recover SIM7670 data mode and CMUX [esphome#22816](https://github.com/esphome/esphome/pull/22816) by [@bdraco](https://github.com/bdraco)
- [i2c] Stop bus recovery clock pulses once SDA is released [esphome#22852](https://github.com/esphome/esphome/pull/22852) by [@bdraco](https://github.com/bdraco)

