#!/usr/bin/sh

if [ -x "poetry" ]; then
    pip3 install poetry
fi

git clone https://github.com/zalun/djpoe.git djpoe-installation
cd djpoe-installation
poetry install
app_name=$(poetry run python3 customize.py)

cd ..
mv djpoe-installation $app_name
