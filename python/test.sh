#!/usr/bin/bash

TESTPYTHON="main.py"

# (sleep 10 ; ps aux | grep Python | grep $TESTPYTHON | tr -s " " | sed -e 's/^ //g' | cut -d " " -f 1 | xargs kill -TERM) &
(sleep 10 ; ps aux | grep Python | grep $TESTPYTHON | tr -s " " | sed -e 's/^ //g' | cut -d " " -f 1) &
python3 $TESTPYTHON

exit 0
