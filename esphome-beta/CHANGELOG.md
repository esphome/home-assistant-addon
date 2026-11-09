## 2026.11.0b3

[**Read release announcement**](https://beta.esphome.io/changelog/2026.11.0)

- [vl53l0x] Recover from a failed I2C read instead of stalling [esphome#19235](https://github.com/esphome/esphome/pull/19235) by [@teklabania](https://github.com/teklabania)
- [ht16k33] Rename display_off method [esphome#22352](https://github.com/esphome/esphome/pull/22352) by [@guillempages](https://github.com/guillempages)
- [core] Add cg.static_buffer for config-sized static buffers [esphome#22326](https://github.com/esphome/esphome/pull/22326) by [@bdraco](https://github.com/bdraco)
- [ht16k33_char] Name the I2C bus in the component test [esphome#22372](https://github.com/esphome/esphome/pull/22372) by [@bdraco](https://github.com/bdraco)
- [tsl2591][seeed_mr24hpc1] Drop device classes from unitless sensors [esphome#22375](https://github.com/esphome/esphome/pull/22375) by [@swoboda1337](https://github.com/swoboda1337)
- [ld2410][ld2412][ld2420] Drop device classes from unitless gate and light entities [esphome#22374](https://github.com/esphome/esphome/pull/22374) by [@swoboda1337](https://github.com/swoboda1337)
- [wifi] Create the IPv6 link-local through lwIP on connect [esphome#22364](https://github.com/esphome/esphome/pull/22364) by [@randybb](https://github.com/randybb)
- [i2s_audio] Fix APLL clock source on ESP32-P4 [esphome#22402](https://github.com/esphome/esphome/pull/22402) by [@jalr](https://github.com/jalr)
- [libretiny] Read pins in interrupts without detaching the interrupt on Realtek [esphome#22400](https://github.com/esphome/esphome/pull/22400) by [@bdraco](https://github.com/bdraco)
- [light] Keep power estimation state in codegen static storage [esphome#22370](https://github.com/esphome/esphome/pull/22370) by [@bdraco](https://github.com/bdraco)
- [i2c] Mask I2C interrupts after an error on classic ESP32 [esphome#22396](https://github.com/esphome/esphome/pull/22396) by [@bdraco](https://github.com/bdraco)
- [libretiny] Run millis(), micros() and delays on real time on RTL8710B [esphome#22404](https://github.com/esphome/esphome/pull/22404) by [@bdraco](https://github.com/bdraco)
- [libretiny] Interrupt on both edges for any edge pins on RTL8710B [esphome#22403](https://github.com/esphome/esphome/pull/22403) by [@bdraco](https://github.com/bdraco)

