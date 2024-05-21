#! /usr/bin/sh

GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

BOLD=$(tput bold)
NORMAL=$(tput sgr0)

# Install dependencies
[ ! -f ./venv ] && python3 -m venv venv

venv/bin/pip install -r requirements.txt
clear
# Run the application
venv/bin/python -m obsidian_sync.install

echo 
echo "${GREEN}${BOLD}Installing the systemd service..."

sudo cp systemd/obsidian_sync.service /etc/systemd/system/obsidian_sync.service

sudo systemctl daemon-reload
sudo systemctl enable obsidian_sync
sudo systemctl start obsidian_sync

echo "Service started!${NORMAL}${NC}"
echo
echo "${GREEN}You can check the status of the service by running '${BLUE}${BOLD}sudo systemctl status obsidian_sync${NORMAL}${NC}'"