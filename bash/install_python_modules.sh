#!/bin/bash

sudo apt udate
sudo apt upgrade -y

apps="
numpy
matplotlib
"

sudo pip3 install $apps
