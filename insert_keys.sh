#!/bin/sh

sed "s/<your_app_id>/$PUBLIC/g" script.py > script_temp
sed "s/<your_secret_key>/$PRIVATE/g" script_temp > script_travis.py

rm script_temp
