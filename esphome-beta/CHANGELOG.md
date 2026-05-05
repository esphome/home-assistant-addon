## 2026.4.4

[**Read release announcement**](https://beta.esphome.io/changelog/2026.4.0)

- [automation] Fix codegen type for component.resume update_interval [esphome#16069](https://github.com/esphome/esphome/pull/16069) by [@bharvey88](https://github.com/bharvey88)
- [mcp23xxx_base] Reject unsupported interrupt_pin options (inverted, allow_other_uses) [esphome#16149](https://github.com/esphome/esphome/pull/16149) by [@bdraco](https://github.com/bdraco)
- [core] Strip \\?\ prefix from sys.executable for PlatformIO subprocess [esphome#16158](https://github.com/esphome/esphome/pull/16158) by [@jesserockz](https://github.com/jesserockz)
- [esp32] Replace 512B stack buffer in printf wraps with picolibc cookie FILE [esphome#16170](https://github.com/esphome/esphome/pull/16170) by [@bdraco](https://github.com/bdraco)
- [lvgl] Clamp values for meter line indicators [esphome#16180](https://github.com/esphome/esphome/pull/16180) by [@clydebarrow](https://github.com/clydebarrow)
- [esp32] Drop printf wrap on IDF 6.0+ (picolibc no longer needs it) [esphome#16189](https://github.com/esphome/esphome/pull/16189) by [@bdraco](https://github.com/bdraco)
- [api] Fall back to owning types for service array args used after a delay [esphome#16140](https://github.com/esphome/esphome/pull/16140) by [@bdraco](https://github.com/bdraco)
- [api] Use safe_print for log output and fix safe_print bytes-repr fallback [esphome#16160](https://github.com/esphome/esphome/pull/16160) by [@jesserockz](https://github.com/jesserockz)

