FROM python:3.11.4 as backend

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8 \
  DJANGO_ENV=${DJANGO_ENV} \
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.6.1 \
  POETRY_VIRTUALENVS_CREATE=false \
  DJANGO_ENV=local

RUN apt update && apt install -y \
  curl \
  libffi-dev \
  openssl \
  gettext  \
  cron \
  musl-dev  \
  && rm -rf /var/lib/apt/lists/* \
  && pip install "poetry==$POETRY_VERSION"

WORKDIR /pysetup
COPY ./pyproject.toml ./poetry.lock*  /pysetup/
RUN echo $DJANGO_ENV
RUN poetry install --no-interaction --no-ansi
WORKDIR /app
COPY . /app
USER root

# set up cron
RUN export DJANGO_SETTINGS_MODULE=nba_fantasy_analyzer.settings
RUN chmod 0744 cron.py
COPY cron/scan_cities_cron /etc/cron.d/scan_cities_cron
RUN chmod 0644 /etc/cron.d/scan_cities_cron
RUN crontab /etc/cron.d/scan_cities_cron
RUN touch /var/log/cron.log

RUN chmod +x /app/entrypoint/entrypoint.sh
ENTRYPOINT ["/app/entrypoint/entrypoint.sh"]
