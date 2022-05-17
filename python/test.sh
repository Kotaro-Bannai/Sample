#!/usr/bin/bash

TESTPYTHON="main.py"

(sleep 10 ; ps ax | grep Python | grep $TESTPYTHON | tr -s " " | sed -e 's/^ //g' | cut -d " " -f 1 | xargs kill -SIGINT) &
# (sleep 10 ; ps ax | grep Python | grep $TESTPYTHON | tr -s " " | sed -e 's/^ //g' | cut -d " " -f 1) &
python3 $TESTPYTHON

exit 0
