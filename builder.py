from csv import reader
from json import dump
from netaddr import iprange_to_cidrs

ranges = set()

with open('iran_raw_data.csv', newline='') as csvfile:
    r = reader(csvfile)
    for row in r:
        cidrs = iprange_to_cidrs(row[0], row[1])
        for ip_range in cidrs:
            ranges.add(str(ip_range))

with open('iran_ip_range.json', 'w') as outfile:
    dump(list(ranges), outfile, sort_keys=True, indent=4)

with open('iran_ip_range.txt', 'w') as fp:
    for r in ranges:
        fp.write("%s," % r)
