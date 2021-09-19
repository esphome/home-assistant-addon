ARG BUILD_FROM=esphome/esphome-hassio-amd64:dev
FROM ${BUILD_FROM}

# Copy root filesystem
COPY rootfs /

# Labels
LABEL \
    io.hass.type="addon" \
    io.hass.version=dev
