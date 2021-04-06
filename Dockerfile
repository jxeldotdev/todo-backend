FROM python:3.9-alpine as deps

ADD app/requirements.txt /tmp

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

# System deps and python deps are seperated into two steps for caching
RUN pip install --no-cache-dir -r /tmp/requirements.txt && rm -f /tmp/requirements.txt

# Create a user for the application so it's not running as root
RUN addgroup -S todoapp && adduser -S todoapp -G todoapp && mkdir -p /home/todoapp/src/app && chown -R todoapp:todoapp /home/todoapp/src

FROM deps

ADD docker-entrypoint.sh /usr/local/bin/

RUN chmod +x /usr/local/bin/docker-entrypoint.sh

USER todoapp

ADD app /home/todoapp/

WORKDIR /home/todoapp/src/

ENTRYPOINT [ "/usr/local/bin/docker-entrypoint.sh" ]
