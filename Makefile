SHELL := /bin/bash
.PHONY: all test build run down

help:
	@$(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$'

all: all test build run down

test:
	docker-compose run web --test

build:
	docker-compose build

run:
	docker-compose up

down:
	docker-compose down

init:
	cp .env.template .env
	make build
