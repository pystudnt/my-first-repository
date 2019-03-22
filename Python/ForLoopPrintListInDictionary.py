#!/usr/bin/env python
neighbors = ['s1', 's2', 's3']
facts = {'hostname': 'cisco', 'os': '7.0.3', 'neighbors': neighbors}
i = 0
for item in facts:
    print facts['neighbors'][i]
    i += 1
