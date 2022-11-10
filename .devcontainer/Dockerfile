FROM ghcr.io/home-assistant/devcontainer:addons

RUN \
  apt-get update \
  && apt-get install -y --no-install-recommends \
    python3-pip

COPY script/requirements.txt /

RUN pip install -r /requirements.txt
