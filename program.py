# -*- coding: utf-8 -*-

import fileinput

lines = []

for line in fileinput.input():
    lines.append(line)
    
print(lines)