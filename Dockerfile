FROM python:3.9-alpine as deps

RUN pip install --upgrade pip && \
    apk add --update --no-cache \
    build-base \
    openssl-dev \
    libffi-dev \
    libxml2-dev \
    libxslt-dev \
    postgresql-dev \
    musl-dev \
    python3-dev \
    cargo 


# Create a user for the application so it's not running as root
RUN addgroup -S todoapp && adduser -S todoapp -G todoapp && mkdir -p /home/todoapp/src/app && chown -R todoapp:todoapp /home/todoapp/src

ENV PATH="/home/todoapp/.local/bin:${PATH}"

USER todoapp

ADD requirements.txt /tmp

# System deps and python deps are seperated into two steps for caching
RUN pip install --no-cache-dir -r /tmp/requirements.txt

FROM deps

USER root

ADD docker-entrypoint.sh /usr/local/bin/

RUN chmod +x /usr/local/bin/docker-entrypoint.sh

USER todoapp

ADD src /home/todoapp/src/

WORKDIR /home/todoapp/src/

ENTRYPOINT [ "/usr/local/bin/docker-entrypoint.sh" ]
