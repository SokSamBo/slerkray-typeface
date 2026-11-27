VENV := .venv
PY := $(VENV)/bin/python

.PHONY: setup source build test clean

setup:
	python3 -m venv $(VENV)
	$(VENV)/bin/pip install -r requirements.txt

source:
	$(PY) scripts/make_source.py

build:
	$(VENV)/bin/fontmake -u sources/Slerkray-Regular.ufo -o otf ttf --output-dir fonts

test: build
	$(VENV)/bin/fontbakery check-universal fonts/*.ttf || true

clean:
	rm -rf fonts master_ufo instance_ufo
