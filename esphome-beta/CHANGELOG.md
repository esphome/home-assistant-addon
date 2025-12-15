## 2025.12.0b3

[**Read release announcement**](https://beta.esphome.io/changelog/2025.12.0)

- [core] Fix CORE.raw_config not updated after package merge [esphome#12456](https://github.com/esphome/esphome/pull/12456) by [@bdraco](https://github.com/bdraco)
- [packet_transport] Ensure retransmission at update intervals [esphome#12472](https://github.com/esphome/esphome/pull/12472) by [@clydebarrow](https://github.com/clydebarrow)
- [core] Fix polling_component_schema and type consistency [esphome#12478](https://github.com/esphome/esphome/pull/12478) by [@swoboda1337](https://github.com/swoboda1337)
- [cc1101] Add packet mode support [esphome#12474](https://github.com/esphome/esphome/pull/12474) by [@swoboda1337](https://github.com/swoboda1337) (new-feature)
- [dashboard] Add ESPHOME_TRUSTED_DOMAINS support to events WebSocket [esphome#12479](https://github.com/esphome/esphome/pull/12479) by [@bdraco](https://github.com/bdraco)
- [wifi_signal] Skip publishing disconnected RSSI value [esphome#12482](https://github.com/esphome/esphome/pull/12482) by [@bdraco](https://github.com/bdraco)
- [web_server_idf] Always enable LRU purge to prevent socket exhaustion [esphome#12481](https://github.com/esphome/esphome/pull/12481) by [@bdraco](https://github.com/bdraco)
- [ota] Match client timeout to device timeout to prevent premature failures [esphome#12484](https://github.com/esphome/esphome/pull/12484) by [@bdraco](https://github.com/bdraco)
- Fix progmem.h includes for host [esphome#12471](https://github.com/esphome/esphome/pull/12471) by [@guillempages](https://github.com/guillempages)
- [ethernet] fix used pins validation in configuration of RMII pins [esphome#12486](https://github.com/esphome/esphome/pull/12486) by [@mbohdal](https://github.com/mbohdal)
- [wifi] Fix WiFi recovery after failed connection attempts [esphome#12483](https://github.com/esphome/esphome/pull/12483) by [@bdraco](https://github.com/bdraco)

