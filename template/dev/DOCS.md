# ESPHome DEV add on

This is **development** version of the ESPHome add on.

To deploy production nodes please use mainstream release add on.

The add on uses a version of ESPHome built automatically every day at 02:00 UTC. and is used to test components in development. See the `esphome_fork` configuration below to properly configure the add on. Once you update the configuration make sure to rebuild the image.

## Configuration

**Note**: _Remember to restart the add-on when the configuration is changed._

### Option: `esphome_fork`

Install ESPHome from a fork or branch.
For example to test a pull request, use `pull/XXXX/head` where `XXXX` is the PR number,
or you can specify the username of the fork owner and branch `username:branch` which
assumes the repository is named `esphome` still.

If you need to test the latest commit on dev branch before the image is updated you can enter `dev` here.

Please note that the fork or branch you are using **must** be up to date with ESPHome dev
or the add-on **will not start**.


## General ESPHome add on configurations

General options also available in other versions.

### Option: `ssl`

Enables or disables encrypted SSL/TLS (HTTPS) connections to the web server of this add-on.
Set it to `true` to encrypt communications, `false` otherwise.
Please note that if you set this to `true` you must also generate the key and certificate
files for encryption. For example using [Let's Encrypt](https://www.home-assistant.io/addons/lets_encrypt/)
or [Self-signed certificates](https://www.home-assistant.io/docs/ecosystem/certificates/tls_self_signed_certificate/).

### Option: `certfile`

The certificate file to use for SSL. If this file doesn't exist, the add-on start will fail.

**Note**: The file MUST be stored in `/ssl/`, which is the default for Home Assistant

### Option: `keyfile`

The private key file to use for SSL. If this file doesn't exist, the add-on start will fail.

**Note**: The file MUST be stored in `/ssl/`, which is the default for Home Assistant

### Option: `leave_front_door_open`

Adding this option to the add-on configuration allows you to disable
authentication by setting it to `true`.

### Option: `relative_url`

Host the ESPHome dashboard under a relative URL, so that it can be integrated
into existing web proxies like NGINX under a relative URL. Defaults to `/`.

### Option: `status_use_ping`

By default the dashboard uses mDNS to check if nodes are online. This does
not work across subnets unless your router supports mDNS forwarding or avahi.

Setting this to `true` will make ESPHome use ICMP ping requests to get the node status. Use this if all nodes always have offline status even when they're connected.

### Option: `streamer_mode`

If set to `true`, this will enable streamer mode, which makes ESPHome hide all
potentially private information. So for example WiFi (B)SSIDs (which could be
used to find your location), usernames, etc. Please note that you need to use
the `!secret` tag in your YAML file to also prevent these from showing up
while editing and validating.
