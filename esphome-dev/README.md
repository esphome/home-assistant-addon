# ESPHome Dev Add-On

[![ESPHome logo][logo]][website]

[![GitHub stars][github-stars-shield]][repository]
[![Discord][discord-shield]][discord]

## About

This add-on allows you to manage and program your ESP8266 and ESP32 based microcontrollers
directly through Home Assistant **with no programming experience required**. All you need to do
is write YAML configuration files; the rest (over-the-air updates, compiling) is all
handled by ESPHome.

<p align="center">
<img title="ESPHome dashboard screenshot" src="https://github.com/esphome/home-assistant-addon/raw/main/esphome-dev/images/screenshot.png" width="700px"></img>
</p>

[View the ESPHome documentation][website]

## Example

With ESPHome, you can go from a few lines of YAML straight to a custom-made
firmware. For example, to include a [DHT22][dht22].
temperature and humidity sensor, you just need to include 8 lines of YAML
in your configuration file:

<img title="ESPHome DHT configuration example" src="https://github.com/esphome/home-assistant-addon/raw/main/esphome-dev/images/dht-example.png" width="500px"></img>

Then just click UPLOAD and the sensor will magically appear in Home Assistant:

<img title="ESPHome Home Assistant discovery" src="https://github.com/esphome/home-assistant-addon/raw/main/esphome-dev/images/temperature-humidity.png" width="600px"></img>

[discord]: https://discord.gg/KhAMKrd
[repository]: https://github.com/esphome/esphome
[discord-shield]: https://img.shields.io/discord/429907082951524364.svg
[github-stars-shield]: https://img.shields.io/github/stars/esphome/esphome.svg?style=social&label=Star&maxAge=2592000
[dht22]: https://next.esphome.io/components/sensor/dht.html
[releases]: https://next.esphome.io/changelog/index.html
[logo]: https://github.com/esphome/home-assistant-addon/raw/main/esphome-dev/logo.png
[website]: https://next.esphome.io/
