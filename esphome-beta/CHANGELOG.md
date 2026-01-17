## 2026.1.0b3

[**Read release announcement**](https://beta.esphome.io/changelog/2026.1.0)

- [i2s_audio] Bugfix: Buffer overflow in software volume control [esphome#13190](https://github.com/esphome/esphome/pull/13190) by [@kahrendt](https://github.com/kahrendt)
- [sprinkler] Fix scheduler deprecation warnings and heap churn with FixedVector [esphome#13251](https://github.com/esphome/esphome/pull/13251) by [@bdraco](https://github.com/bdraco)
- [dallas_temp] Use const char* for set_timeout to fix deprecation warning and heap churn [esphome#13250](https://github.com/esphome/esphome/pull/13250) by [@bdraco](https://github.com/bdraco)
- [api] Fix clock conflicts when multiple clients connected to homeassistant time [esphome#13253](https://github.com/esphome/esphome/pull/13253) by [@bdraco](https://github.com/bdraco)
- [esp32_ble_client] Reduce GATT data event logging to prevent firmware update failures [esphome#13252](https://github.com/esphome/esphome/pull/13252) by [@bdraco](https://github.com/bdraco)
- [ntc, resistance] change log level to verbose [esphome#13268](https://github.com/esphome/esphome/pull/13268) by [@mrtoy-me](https://github.com/mrtoy-me)
- [api] Use subtraction for protobuf bounds checking [esphome#13306](https://github.com/esphome/esphome/pull/13306) by [@bdraco](https://github.com/bdraco)
- [hmac_sha256] Replace unsafe sprintf with format_hex_to [esphome#13290](https://github.com/esphome/esphome/pull/13290) by [@bdraco](https://github.com/bdraco)
- [hub75] Bump esp-hub75 version to 0.3.0 [esphome#13243](https://github.com/esphome/esphome/pull/13243) by [@stuartparmenter](https://github.com/stuartparmenter) (breaking-change)
- [http_request] Unable to handle chunked responses [esphome#7884](https://github.com/esphome/esphome/pull/7884) by [@HLFCode](https://github.com/HLFCode)

