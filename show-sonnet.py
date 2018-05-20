#!/usr/bin/python3

from random import randint

import json
import sys

data = open('sonnets.json')
sonnets = json.load(data)

try:
    sonnet_number = int(sys.argv[1])
    if sonnet_number > 0 and sonnet_number < len(sonnets) + 1:
        pass
    else:
        sys.exit()
except ValueError:
    sys.exit()
except IndexError:
    sonnet_number = randint(0, len(sonnets))

print ('\t\tSonnet', sonnet_number,'\n')
print (sonnets[sonnet_number - 1])


