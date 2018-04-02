#!/usr/bin/env python3.5

#
# Generate new feedback data for the NLC service given some initial training
# data. This is to have more data available for the model that will reinforce
# certain relationships. Since we have very little data this may help us (or may
# not). For each training example in the seed data, a duplicate is made with
# probability p with no capitalization and no punctuation. After this, n random
# training examples will be chosen and duplicated.
#

import argparse
import csv
import random
import re
import string
import sys

PUNC_REGEX = r'[' + re.escape(string.punctuation) + ']+'

parser = argparse.ArgumentParser()
parser.add_argument('seed_data', help='The location of the seed data')
parser.add_argument('p', type=float,
    help='Probability with which to duplicate example')
parser.add_argument('n', type=int, help='Number of examples to duplicate.')
args = parser.parse_args()

rows = []
with open(args.seed_data, newline='') as f:
    f_reader = csv.reader(f, delimiter=',', quotechar='"')
    std_writer = csv.writer(sys.stdout, delimiter=',', quotechar='"')

    for row in f_reader:
        if random.random() < args.p:
            dupl = re.sub(PUNC_REGEX, '', row[0]).lower()
            new_row = [dupl, row[1]]
            std_writer.writerow(new_row)

            rows.append(new_row)

        std_writer.writerow(row)
        rows.append(row)

sample = random.sample(rows, args.n)
for row in sample:
    std_writer.writerow(row)
