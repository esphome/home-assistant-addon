ARG BUILD_FROM=esphome/esphome-hassio-base-amd64:1.1.0
FROM ${BUILD_FROM}

RUN \
    apt-get update \
    && apt-get install -y --no-install-recommends \
        python-pil \
    && rm -rf \
        /tmp/* \
        /var/{cache,log}/* \
        /var/lib/apt/lists/*

# Copy root filesystem
COPY rootfs /

RUN \
    pip2 install --no-cache-dir --no-binary :all: https://github.com/esphome/esphome/archive/dev.zip

# Build arguments
ARG BUILD_VERSION=dev

# Labels
LABEL \
    io.hass.name="ESPHome" \
    io.hass.description="Manage and program ESP8266/ESP32 microcontrollers through YAML configuration files" \
    io.hass.type="addon" \
    io.hass.version=dev
