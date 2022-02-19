#!/usr/bin/python3.8
# coding: utf-8

pairs = []
days = 2
for m in range(days):
    for n in range(days):
        # if m < n:
        if m != n:
            pairs.append((m, n))

print(pairs)
