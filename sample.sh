#!/bin/sh

run()
{
    echo "\$ $@"
    $@
    ret=$?
    echo

    return $?
}

run python3.8 python/sample.py
