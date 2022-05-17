#!/usr/bin/bash

TESTPYTHON="main.py"

(sleep 10 ; ps a | grep Python | grep $TESTPYTHON | tr -s " " | sed -e 's/^ //g' | cut -d " " -f 1 | xargs kill -TERM) &
python3 $TESTPYTHON

exit 0
