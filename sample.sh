#!/bin/sh

run()
{
    echo "\$ $@"
    $@
    ret=$?
    echo

    return $?
}

run python3 python/sample.py
