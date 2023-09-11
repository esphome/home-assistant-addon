FROM ghcr.io/home-assistant/devcontainer:addons

RUN \
  apt-get update \
  && apt-get install -y --no-install-recommends \
    python3-pip \
    python3-venv

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY script/requirements.txt /

RUN pip install -r /requirements.txt
