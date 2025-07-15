## 2025.7.0b4

[**Read release announcement**](https://beta.esphome.io/changelog/2025.7.0)

- Suppress spurious volatile and Python syntax warnings during builds [esphome#9488](https://github.com/esphome/esphome/pull/9488) by [@bdraco](https://github.com/bdraco)
- [online_image] Support ``byte_order`` [esphome#9502](https://github.com/esphome/esphome/pull/9502) by [@clydebarrow](https://github.com/clydebarrow)
- [json] Bump ArduinoJson library to 7.4.2 [esphome#8857](https://github.com/esphome/esphome/pull/8857) by [@kahrendt](https://github.com/kahrendt) (breaking-change)
- [fan] Do not save state for fan if configured as NO_RESTORE [esphome#9472](https://github.com/esphome/esphome/pull/9472) by [@skyegecko](https://github.com/skyegecko)
- Fix LibreTiny compilation error by updating ESPAsyncWebServer and dependencies [esphome#9492](https://github.com/esphome/esphome/pull/9492) by [@bdraco](https://github.com/bdraco)
- [captive_portal] Add test case for libretiny [esphome#9457](https://github.com/esphome/esphome/pull/9457) by [@clydebarrow](https://github.com/clydebarrow)
- [opentherm.output] Fix ``lerp`` [esphome#9506](https://github.com/esphome/esphome/pull/9506) by [@kbx81](https://github.com/kbx81)
- [servo] Fix ``lerp`` [esphome#9507](https://github.com/esphome/esphome/pull/9507) by [@kbx81](https://github.com/kbx81)
- Add missing clang-tidy NOLINT comments for ArduinoJson v7 in IDF webserver [esphome#9508](https://github.com/esphome/esphome/pull/9508) by [@bdraco](https://github.com/bdraco)
- [core] Don't issue -Wno-volatile for host platform [esphome#9511](https://github.com/esphome/esphome/pull/9511) by [@clydebarrow](https://github.com/clydebarrow)
- [component] Fix ``is_ready`` flag when loop disabled [esphome#9501](https://github.com/esphome/esphome/pull/9501) by [@jesserockz](https://github.com/jesserockz)
- [ms8607] Fix humidity calc [esphome#9499](https://github.com/esphome/esphome/pull/9499) by [@LorbusChris](https://github.com/LorbusChris)

