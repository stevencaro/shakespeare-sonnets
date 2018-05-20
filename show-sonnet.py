#!/usr/bin/python3

from random import randint

import argparse
import json
import sys

with open('sonnets.json') as data:
    sonnets = json.load(data)

parser = argparse.ArgumentParser(description = 'Displays the sonnets of Shakespeare. If you don\'t specify a sonnet to display, displays a random sonnet.')
parser.add_argument('-l', action='store_true', help='list first lines of all 154 sonnets')
parser.add_argument('-n', type=int , help='number of sonnet to display')

options = parser.parse_args()

if options.l:
    print('listing sonnets')
    for num, sonnet in enumerate(sonnets, 1):
        print ('{:3} {}'.format(num, (sonnets[num - 1].partition('\n'))[0]))
    sys.exit()

if options.n is None:
    sonnet_number = randint(0, len(sonnets))
elif options.n >= 1 and options.n <= 154:
    sonnet_number = options.n
else:
    sys.exit('Select a number from 1 to 154')

print ('\t\tSonnet', sonnet_number,'\n')
print (sonnets[sonnet_number - 1])


