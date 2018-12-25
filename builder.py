import csv
import json
from netaddr import iprange_to_cidrs

ranges = set()

with open('iran.csv', newline='') as csvfile:
    r = csv.reader(csvfile)
    for row in r:
        cidrs = iprange_to_cidrs(row[0], row[1])
        for ip_range in cidrs:
            ranges.add(str(ip_range))

with open('iran_ip_range.json', 'w') as outfile:
    json.dump(list(ranges), outfile)

with open('iran_ip_range.txt', 'w') as fp:
    for r in ranges:
        fp.write("%s," % r)

