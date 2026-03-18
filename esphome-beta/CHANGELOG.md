## 2026.3.0b4

[**Read release announcement**](https://beta.esphome.io/changelog/2026.3.0)

- [core] Small improvements [esphome#14884](https://github.com/esphome/esphome/pull/14884) by [@diorcety](https://github.com/diorcety)
- [api] Fix ProtoMessage protected destructor compile error on host platform [esphome#14882](https://github.com/esphome/esphome/pull/14882) by [@bdraco](https://github.com/bdraco)
- [speaker] Fix media playlist using announcement delay [esphome#14889](https://github.com/esphome/esphome/pull/14889) by [@swoboda1337](https://github.com/swoboda1337)
- [core] Add back deprecated set_internal() for external projects [esphome#14887](https://github.com/esphome/esphome/pull/14887) by [@bdraco](https://github.com/bdraco)
- [espnow] Fix EventPool/LockFreeQueue sizing off-by-one [esphome#14893](https://github.com/esphome/esphome/pull/14893) by [@bdraco](https://github.com/bdraco)
- [usb_cdc_acm] Fix EventPool/LockFreeQueue sizing off-by-one [esphome#14894](https://github.com/esphome/esphome/pull/14894) by [@bdraco](https://github.com/bdraco)
- [usb_host] Fix EventPool/LockFreeQueue sizing off-by-one [esphome#14896](https://github.com/esphome/esphome/pull/14896) by [@bdraco](https://github.com/bdraco)
- [usb_uart] Fix EventPool/LockFreeQueue sizing off-by-one [esphome#14895](https://github.com/esphome/esphome/pull/14895) by [@bdraco](https://github.com/bdraco)
- [esp32_ble] Fix EventPool/LockFreeQueue sizing off-by-one [esphome#14892](https://github.com/esphome/esphome/pull/14892) by [@bdraco](https://github.com/bdraco)
- [esp32_ble_server] Remove vestigial semaphore from BLECharacteristic [esphome#14900](https://github.com/esphome/esphome/pull/14900) by [@bdraco](https://github.com/bdraco)
- [mqtt] Fix data race on inbound event queue [esphome#14891](https://github.com/esphome/esphome/pull/14891) by [@bdraco](https://github.com/bdraco)
- [scheduler] Fix UB in cross-thread counter/vector reads, add atomic fast-path [esphome#14880](https://github.com/esphome/esphome/pull/14880) by [@bdraco](https://github.com/bdraco)

