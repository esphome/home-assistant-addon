# ESPHome DEV App

This is **development** version of the ESPHome App.

To deploy production nodes please use mainstream release App.

The App uses a version of ESPHome built automatically every day at 02:00 UTC. and is used to test components in development. See the `esphome_fork` configuration below to properly configure the App. Once you update the configuration make sure to rebuild the image.

## Configuration

**Note**: _Remember to restart the App when the configuration is changed._

### Option: `esphome_fork`

Install ESPHome from a fork or branch.
For example to test a pull request, use `pull/XXXX/head` where `XXXX` is the PR number,
or you can specify the username of the fork owner and branch `username:branch` which
assumes the repository is named `esphome` still.

If you need to test the latest commit on dev branch before the image is updated you can enter `dev` here.

Please note that the fork or branch you are using **must** be up to date with ESPHome dev
or the App **will not start**.


## General ESPHome App configurations

General options also available in other versions.

### Option: `leave_front_door_open`

Adding this option to the App configuration allows you to disable
authentication by setting it to `true`.
