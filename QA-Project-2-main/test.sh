#!/bin/bash

# sudo apt install python3.8-venv

# source venv/bin/activate

# pip3 install -r requirements.txt

# python3 -m pytest --cov=.
python3 -m venv venv
ls -l
source venv/bin/activate
declare -a directories=("front_end_1" "gun_gen_2" "perk_one_3" "perk_two_4")
for dir in "${directories[@]}"
do
  cd ${dir}
  python3 -m pytest --cov=.
  cd ..
done