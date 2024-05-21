#! /usr/bin/sh

# Install dependencies
[ ! -f ./venv ] && python -m venv venv

venv/bin/pip install -r requirements.txt
clear
# Run the application
venv/bin/python -m obsidian_sync.install
