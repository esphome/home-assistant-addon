## 2025.8.0

[**Read release announcement**](https://esphome.io/changelog/2025.8.0)

## Release Overview

ESPHome 2025.8.0 expands platform support with the introduction of Nordic nRF52 devices,
adds mesh communication capabilities, and delivers significant performance improvements. This release
focuses on architectural innovation and memory optimization while introducing new hardware possibilities.

**Key Highlights:**

- **New nRF52 platform** based on Zephyr RTOS opens Nordic semiconductor ecosystem
- **ESP-NOW mesh communication** enables direct device-to-device connectivity
- **High-performance MIPI DSI displays** for ESP32-P4 professional applications
- **Extensive memory optimizations** with up to 10x performance improvements in key areas
- **Python 3.11+ requirement** (breaking change - Python 3.10 support dropped)


## NRF52 Platform Support


ESPHome 2025.8.0 introduces comprehensive support for Nordic nRF52 series microcontrollers through the new
[NRF52](https://esphome.io/components/nrf52) platform. This implementation is built on the Zephyr RTOS, providing a robust
foundation for Nordic semiconductor devices.

**Key Features:**

- **Complete platform integration** with ESPHome's component ecosystem
- **ADC support** for analog sensor reading with configurable resolution
- **GPIO functionality** with interrupt support and pin configuration
- **Zephyr debug component** for advanced debugging and development

The nRF52 platform opens up new possibilities for low-power, Bluetooth-enabled devices while maintaining
the familiar ESPHome configuration syntax and component compatibility.


## ESP-NOW Communication

The new [ESP-NOW](https://esphome.io/components/espnow) component brings device-to-device communication to ESP32 platforms without
requiring WiFi infrastructure. ESP-NOW enables direct communication between ESP32 devices using the 2.4GHz
band with minimal power consumption.

**Applications:**

- **Mesh sensor networks** - Sensors can communicate directly without WiFi routers
- **Remote control systems** - Direct device control with low latency
- **Backup communication** - Fallback when WiFi is unavailable
- **Battery-powered devices** - Efficient communication for power-constrained applications

This protocol is particularly valuable for distributed sensor networks and scenarios where traditional
WiFi infrastructure is impractical or unavailable.


## MIPI DSI Display Support

ESPHome now supports high-performance MIPI DSI displays through the new [MIPI DSI](https://esphome.io/components/display/mipi_dsi)
component, specifically designed for ESP32-P4 processors with DSI interfaces.

**Benefits:**

- **High-resolution displays** with excellent performance
- **Hardware acceleration** through dedicated DSI controllers
- **Reduced CPU overhead** compared to traditional SPI displays
- **Professional display quality** for advanced applications

This addition significantly expands ESPHome's display capabilities, enabling professional-grade user interfaces
and high-resolution graphics applications.


## Memory & Performance Optimizations

ESPHome 2025.8.0 includes extensive optimizations focused on reducing memory usage and improving performance:

**Flash Memory Savings:**

- Conditional compilation removes unused API features (thousands of bytes saved)
- Optimized protobuf implementations with zero-copy techniques
- Reduced code duplication across components
- Streamlined error handling and logging systems

**Runtime Performance:**

- 10x faster string encoding with optimized memcpy operations
- Enhanced scheduler with reduced millis() calls
- Improved BLE scanning with batched processing
- Zero-copy protobuf fields for reduced memory allocations


## Python 3.11+ Requirement

Starting with ESPHome 2025.8.0, **Python 3.11 or higher is required** to run ESPHome. This change enables us to:

- Utilize modern Python features and improvements
- Remove legacy compatibility code that was needed for older Python versions
- Maintain a more secure and efficient codebase

**Why This Change?**

Python 3.10 reaches its [end of life in October 2026](https://devguide.python.org/versions/). This
upgrade is necessary for the project to move forward with modern development practices and maintain
long-term security and maintainability.

**What You Need to Do**

Installation Method | Action Required
--------------------------|----------------------
Home Assistant Add-on | **No action needed** - Already uses Python 3.12
Container Images (Docker) | **No action needed** - Already uses Python 3.12
Direct Installation (pip) | **Upgrade Python to 3.11+** before updating ESPHome

> [!WARNING]
>
> If you're running ESPHome directly on your machine with Python 3.10 or older, running ``pip install -U esphome``
> will not upgrade beyond version 2025.7.x. You must upgrade your Python installation first.


## Breaking Changes

ESPHome 2025.8.0 includes several breaking changes that may require action on your part:

**Bluetooth and BLE Changes**
   - Bluetooth Proxy: Parsed advertisement support and V1 connection support removed to save memory
   - BLE: Conditional compilation for advertising and service classes may reduce available features if not explicitly enabled
   - May affect older components using deprecated Bluetooth features

**API Optimizations**
   - Deprecated protobuf fields removed (reduces flash usage)
   - Conditional compilation for Home Assistant state/service subscriptions
   - May affect custom API clients using deprecated fields

**Component Filter Changes**
   - [LD2410](https://esphome.io/components/sensor/ld2410) and [LD2450](https://esphome.io/components/sensor/ld2450) components now use native filters instead of ``throttle``
   - See the component documentation for updated filter configuration

**ESP32 Touch Sensor**
   - Workaround implemented for ESP-IDF v5.4 regression
   - May affect touch sensor behavior on newer ESP-IDF versions

Most of these changes are automatic optimizations that shouldn't affect typical usage, but custom components
or advanced configurations may need updates.
