import csv
import ipaddress
import json


def parse_csv_file2(filename='iran_raw_data.csv'):
    ranges = set()
    with open(filename) as csvfile:
        csv_reader = csv.DictReader(csvfile)
        return {
            str(address)
            for row in csv_reader
            for address in ipaddress.summarize_address_range(
                ipaddress.IPv4Address(row['start']),
                ipaddress.IPv4Address(row['end']))
        }

def generate_json(ranges):
    with open('iran_ip_range.json', 'wt') as outfile:
        json.dump(list(ranges), outfile, sort_keys=True, indent=4)

def generate_txt(ranges):
    with open('iran_ip_range.txt', 'wt') as fp:
        for rng in ranges:
            fp.write(f"{rng}")

def main():
    ranges = parse_csv_file2()
    generate_json(ranges)
    generate_txt(ranges)

if __name__ == '__main__':
    main()
