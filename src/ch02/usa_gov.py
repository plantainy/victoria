__author__ = 'plantain'

import json
path = 'data/ch02/usagov_bitly_data2012-03-16-1331923249.txt'
records = [json.loads(line) for line in open(path, 'rb')]
time_zone = [rec['tz'] for rec in records if 'tz' in rec]


### Python standard library solution ###
########################################
from collections import defaultdict

def get_counts(sequence):
    counts = defaultdict(int) # values will initialize to 0
    for x in sequence:
        counts[x] += 1
    return counts

def top_counts(count_dict, n=10):
    value_key_pairs = [(count, tz) for tz, count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]

from collections import Counter

def top_counts2(count_dict, n=10):
    counts = Counter(count_dict)
    return counts.most_common(n)
########################################


### Pandas ###
########################################
from pandas import DataFrame, Series
frame = DataFrame(records)
tz_counts = frame['tz'].value_counts()
